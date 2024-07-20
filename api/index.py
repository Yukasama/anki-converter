from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
import genanki
from utils.markdown_to_anki import parse_markdown, create_anki_deck

app = FastAPI()

logging.basicConfig(level=logging.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/uploadfile")
async def create_anki_deck_from_markdown(file: UploadFile = File(...)):
    logging.debug("Received POST request to /api/uploadfile")

    content = await file.read()
    markdown_content = content.decode('utf-8')
    logging.info(f"Received file with content: {markdown_content}")

    cards = parse_markdown(markdown_content)
    deck = create_anki_deck('Generated Deck', cards)

    filename = 'generated_deck.apkg'
    anki_pkg = genanki.Package(deck)

    logging.debug("Generated Anki package successfully")
    return FileResponse(anki_pkg, media_type='application/octet-stream', filename=filename)

@app.get("/api/test")
async def test_get():
    return {"message": "GET request works"}

@app.post("/api/test")
async def test_post():
    return {"message": "POST request works"}
