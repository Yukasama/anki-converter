# Markdown to Anki Converter

## How to generate an Anki PKG from a Markdown file

1. **Setup environment**

   ```bash
   // Windows
   python -m venv .
   .\Scripts\activate

   // MacOS/Linux
   python3 -m venv .
   source bin/activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start server**

   ```bash
   uvicorn main:app --reload
   ```

4. **Create a Postman Request**

   - URL: `http://localhost:8000/uploadfile`
   - Method: `POST`
   - Body:
     - form-data:
       - Key: file
       - Value: `<file_name>.md`

5. **Import .apkg into Anki**

   Select file `generated_deck.apkg` from project directory to import

6. **Happy Learning**

## How to format a Markdown file (.md)

Note:

- There are two types of cards used here: Basic, Cloze
- There are four variants of cards, as shown below
- In cards marked with [Cloze], only use bullet points

```markdown
# File Name

## Heading

### Sub Heading (will be used as Tag for sub-Cards)

#### Card Question // Basic

Card Answer

#### Card Question // Basic with bullet points

- Card Bullet Point
- Card Bullet Point

#### Card Question [Cloze] // [Cloze] will turn bullet points into x Cloze cards

- Card Bullet Point
- Card Bullet Point

#### Card Question [Cloze] // '\<Option\>:' will not be included in Cloze tags

- Option: Card Bullet Point
- Other Option: Card Bullet Point
```
