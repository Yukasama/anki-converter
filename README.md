# Markdown to Anki Converter

## How to generate an Anki PKG from a Markdown file

1. **Start server**

    ```bash
    uvicorn main:app --reload
    ```

2. **Create a Postman Request**

   - URL: `http://localhost:8000/uploadfile`
   - Method: `POST`
   - Body:
     - form-data:
       - Key: `file`
       - Value: `<file>`

3. **Import .apkg into Anki**

    Select file `converted_deck.apkg` from project directory to import

4. **Happy Learning**

## How to format a Markdown file (.md)

- Note: There are two types of cards used here: Basic, Cloze
- Note: Use only Bullet points in [Cloze]

### Sub Heading (will be used as Tag for sub-Cards)

#### Card Question 1 // Basic

Card Answer

#### Card Question 2 // Basic with bullet points

- Card Bullet Point
- Card Bullet Point

#### Card Question 3 [Cloze] // [Cloze] will turn it into x Cloze cards

- {{c1::Card Bullet Point}}
- {{c2::Card Bullet Point}}

#### Card Question 4 [Cloze] // `Description:` will not be included

- Description: {{c1::Card Bullet Point}}
- Description: {{c2::Card Bullet Point}}
