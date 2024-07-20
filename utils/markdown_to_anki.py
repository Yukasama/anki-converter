from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
import genanki
import io

app = FastAPI()

logging.basicConfig(level=logging.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define model for Cloze cards
cloze_model = genanki.Model(
    1607392319,
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
    css='.card { font-family: arial; font-size: 20px; text-align: left; color: black; background-color: white; }'
)

# Define model for Basic cards
basic_model = genanki.Model(
    1607392320,
    'Basic Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Basic Card',
            'qfmt': '{{Question}}',
            'afmt': '{{Answer}}',
        },
    ],
    css='.card { font-family: arial; font-size: 20px; text-align: left; color: black; background-color: white; }'
)

def add_basic_card(deck, question, answer, tags=None):
    note = genanki.Note(
        model=basic_model,
        fields=[question, answer],
        tags=tags if tags else []
    )
    deck.add_note(note)
    logging.debug(f"Added basic card: {question} -> {answer}")

def add_cloze_card(deck, text, tags=None):
    note = genanki.Note(
        model=cloze_model,
        fields=[text],
        tags=tags if tags else []
    )
    deck.add_note(note)
    logging.debug(f"Added cloze card: {text}")

def parse_markdown(content):
    lines = content.split('\n')
    cards = []
    current_tags = []
    question = None
    answer_lines = []
    cloze = False

    for line in lines:
        line = line.strip()
        if line.startswith("###"):
            current_tags = [line.replace("###", "").strip()]
            logging.debug(f"Current tags: {current_tags}")
        elif line.startswith("####"):
            if question and answer_lines:
                answer = "\n".join(answer_lines).strip()
                cards.append((question, answer, cloze, current_tags))
                logging.debug(f"Collected card - Question: {question}, Answer: {answer}, Cloze: {cloze}, Tags: {current_tags}")
            question = line.replace("####", "").strip()
            cloze = "[Cloze]" in question
            question = question.replace("[Cloze]", "").strip()
            answer_lines = []
        else:
            if line:
                answer_lines.append(line)
    
    # Add the last collected card
    if question and answer_lines:
        answer = "\n".join(answer_lines).strip()
        cards.append((question, answer, cloze, current_tags))
        logging.debug(f"Collected card - Question: {question}, Answer: {answer}, Cloze: {cloze}, Tags: {current_tags}")

    return cards

@app.post("/api/uploadfile")
async def create_anki_deck_from_markdown(file: UploadFile = File(...)):
    try:
        # Read the content of the uploaded file
        content = await file.read()
        content = content.decode('utf-8')

        # Create a new deck
        deck = genanki.Deck(
            2059400110,
            'ERP - Enterprise Resource Planning'
        )

        # Parse the markdown content and create cards
        cards = parse_markdown(content)
        for question, answer, cloze, tags in cards:
            if cloze:
                add_cloze_card(deck, f"{question} {{c1::{answer}}}", tags=tags)
            else:
                add_basic_card(deck, question, answer, tags=tags)

        # Check if any cards were added
        if len(deck.notes) == 0:
            logging.debug("No cards were added to the deck.")
        else:
            logging.debug(f"{len(deck.notes)} cards were added to the deck.")

        # Write the deck to a file-like object
        output_buffer = io.BytesIO()
        anki_pkg = genanki.Package(deck)
        anki_pkg.write_to_file(output_buffer)
        output_buffer.seek(0)

        return StreamingResponse(output_buffer, media_type='application/octet-stream', headers={'Content-Disposition': 'attachment; filename=generated_deck.apkg'})
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        return {"error": str(e)}

# Run the FastAPI app (optional: for testing locally)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
