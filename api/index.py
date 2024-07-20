from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
import genanki
import io
import re

app = FastAPI()

logging.basicConfig(level=logging.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def sanitize_tag(tag):
    # Replace spaces with underscores and remove any invalid characters
    return re.sub(r'\W+', '_', tag)

def parse_markdown(content):
    lines = content.split('\n')
    deck_name = None
    tags = []
    questions = []
    current_question = None
    current_answer = []
    cloze = False

    for line in lines:
        logging.debug(f"Processing line: {line}")
        if line.startswith('# '):
            deck_name = line[2:].strip()
            logging.debug(f"Found deck name: {deck_name}")
        elif line.startswith('## '):
            continue
        elif line.startswith('### '):
            tags = [sanitize_tag(line[4:].strip())]
            logging.debug(f"Found tags: {tags}")
        elif line.startswith('#### '):
            if current_question:
                questions.append((current_question, '\n'.join(current_answer).strip(), cloze))
                logging.debug(f"Added question: {current_question}, cloze: {cloze}")
            current_question = line[5:].strip()
            current_answer = []
            cloze = '[Cloze]' in current_question
            if cloze:
                current_question = current_question.replace('[Cloze]', '').strip()
            logging.debug(f"Found question: {current_question}, cloze: {cloze}")
        else:
            if line.strip():  # Only append non-empty lines
                current_answer.append(line)
                logging.debug(f"Appending to current answer: {line}")

    if current_question:
        questions.append((current_question, '\n'.join(current_answer).strip(), cloze))
        logging.debug(f"Added final question: {current_question}, cloze: {cloze}")

    logging.debug(f"Deck name after parsing: {deck_name}")
    logging.debug(f"Tags after parsing: {tags}")
    logging.debug(f"Questions after parsing: {questions}")

    return deck_name, tags, questions

def create_anki_deck(deck_name, tags, questions):
    model_basic = genanki.Model(
        1607392319,
        'Basic Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

    model_cloze = genanki.Model(
        998877661,
        'Cloze Model',
        fields=[
            {'name': 'Text'},
        ],
        templates=[
            {
                'name': 'Cloze Card',
                'qfmt': '{{cloze:Text}}',
                'afmt': '{{cloze:Text}}',
            },
        ],
        css="""
        .card {
         font-family: arial;
         font-size: 20px;
         text-align: left;
         color: black;
         background-color: white;
        }
        .cloze {
         font-weight: bold;
         color: blue;
        }
        """
    )

    if not deck_name:
        raise ValueError("Deck name is required and was not found in the uploaded file")

    deck = genanki.Deck(
        deck_id=2059400110,
        name=deck_name
    )

    for question, answer, cloze in questions:
        logging.debug(f"Creating note for question: {question} with answer: {answer}")
        if not question or not answer:
            logging.warning(f"Skipping note with empty question or answer. Question: {question}, Answer: {answer}")
            continue

        if cloze:
            parts = answer.split('\n')
            for i, part in enumerate(parts):
                # Remove leading dashes and whitespace from list items
                cloze_lines = [f'{{{{c{j+1}::{line.strip().lstrip("-").strip()}}}}}' if j == i else line.strip().lstrip("-").strip() for j, line in enumerate(parts)]
                cloze_text = f"{question}<br><ul><li>" + "</li><li>".join(cloze_lines) + "</li></ul>"
                note = genanki.Note(
                    model=model_cloze,
                    fields=[cloze_text])
                if tags:
                    note.tags = tags
                deck.add_note(note)
        else:
            # Only format as list if answer has multiple lines
            if '\n' in answer:
                lines = [line.strip().lstrip("-").strip() for line in answer.split('\n')]
                answer_text = "<ul><li>" + "</li><li>".join(lines) + "</li></ul>"
            else:
                answer_text = answer
            note = genanki.Note(
                model=model_basic,
                fields=[question, answer_text])

            if tags:
                note.tags = tags

            deck.add_note(note)

    return deck

@app.post("/api/uploadfile")
async def create_anki_deck_from_markdown(file: UploadFile = File(...)):
    try:
        # Read the content of the uploaded file
        content = await file.read()
        content = content.decode('utf-8')

        # Parse the Markdown content
        deck_name, tags, questions = parse_markdown(content)

        # Log the parsed data for debugging
        logging.debug(f"Deck name: {deck_name}")
        logging.debug(f"Tags: {tags}")
        logging.debug(f"Questions: {questions}")

        # Ensure the deck name is not None or empty
        if not deck_name:
            raise ValueError("Deck name is required and was not found in the uploaded file")

        # Create Anki deck
        deck = create_anki_deck(deck_name, tags, questions)

        # Write the deck to a file-like object
        output_buffer = io.BytesIO()
        anki_pkg = genanki.Package(deck)
        anki_pkg.write_to_file(output_buffer)
        output_buffer.seek(0)

        return StreamingResponse(output_buffer, media_type='application/octet-stream', headers={'Content-Disposition': 'attachment; filename=generated_deck.apkg'})
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        return {"error": str(e)}
