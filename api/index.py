from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import logging
from utils.markdown_to_anki import parse_markdown, create_anki_deck, save_deck_to_file 

app = FastAPI()

@app.post("/api/uploadfile")
async def create_anki_deck_from_markdown(file: UploadFile = File(...)):
    content = await file.read()
    markdown_content = content.decode('utf-8')
    logging.info(f"Received file with content: {markdown_content}")

    cards = parse_markdown(markdown_content)
    deck = create_anki_deck('Generated Deck', cards)

    output_file = 'generated_deck.apkg'
    save_deck_to_file(deck, output_file)
    
    return FileResponse(output_file, media_type='application/octet-stream', filename=output_file)
