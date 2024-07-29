from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
import genanki
import io
import re
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def sanitize_tag(tag):
    return re.sub(r'\W+', '_', tag)

def parse_markdown(content):
    lines = content.split('\n')
    tags = []
    questions = []
    current_question = None
    current_answer = []
    cloze = False

    for line in lines:
        if line.startswith('# ') or line.startswith('## '):
            continue
        elif line.startswith('### '):
            tags = [sanitize_tag(line[4:].strip())]
        elif line.startswith('#### '):
            if current_question:
                questions.append((current_question, '\n'.join(current_answer).strip(), cloze))
            current_question = line[5:].strip()
            current_answer = []
            cloze = '[Cloze]' in current_question
            if cloze:
                current_question = current_question.replace('[Cloze]', '').strip()
        else:
            if line.strip():
                current_answer.append(line)

    if current_question:
        questions.append((current_question, '\n'.join(current_answer).strip(), cloze))

    return tags, questions

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
        ],
        css="""
        .card {
         font-family: arial;
         font-size: 20px;
         text-align: left;
         color: black;
         background-color: white;
        }
        """
    )

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
         color: cyan;
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
        if not question or not answer:
            continue

        if cloze:
            lines = [line.strip().lstrip("-").strip() for line in answer.split('\n')]
            for i in enumerate(lines):
                cloze_text = question + "<br><ul>"
                for j, part in enumerate(lines):
                    if i == j:
                        cloze_text += f'<li>{{{{c1::{part}}}}}</li>'
                    else:
                        cloze_text += f'<li>{part}</li>'
                cloze_text += "</ul>"
                note = genanki.Note(
                    model=model_cloze,
                    fields=[cloze_text])
                if tags:
                    note.tags = tags
                deck.add_note(note)
        else:
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
        content = await file.read()
        content = content.decode('utf-8')
        
        filename = os.path.splitext(file.filename)[0]
        tags, questions = parse_markdown(content)

        deck = create_anki_deck(filename, tags, questions)

        output_buffer = io.BytesIO()
        anki_pkg = genanki.Package(deck)
        anki_pkg.write_to_file(output_buffer)
        output_buffer.seek(0)

        return StreamingResponse(output_buffer, media_type='application/octet-stream', headers={'Content-Disposition': f'attachment; filename={filename}.apkg'})
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        return {"error": "Internal server error"}
