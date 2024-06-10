# Markdown to Anki Converter

## How to generate an Anki PKG from a Markdown file

1. **Create python environment**

    ```bash
    // Windows
    python -m venv env

    //MacOS/Linux
    python3 -m venv env
    ```

2. **Activate environment**

    ```bash
    // Windows
    .\env\Scripts\activate

    //MacOS/Linux
    source env/bin/activate
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Start server**

    ```bash
    uvicorn main:app --reload
    ```

5. **Create a Postman Request**

   - URL: `http://localhost:8000/uploadfile`
   - Method: `POST`
   - Body:
     - form-data:
       - Key: file
       - Value: `<file_name>.md`

6. **Import .apkg into Anki**

    Select file `converted_deck.apkg` from project directory to import

7. **Happy Learning**

## How to format a Markdown file (.md)

- Note: There are two types of cards used here: Basic, Cloze
- Note: There are four variants of card formats as shown below
- Note: In cards marked with [Cloze], only use bullet points

```markdown
# File Name

## Heading

### Sub Heading (will be used as Tag for sub-Cards)

#### Card Question    // Basic
Card Answer

#### Card Question    // Basic with bullet points
- Card Bullet Point
- Card Bullet Point

#### Card Question [Cloze]    // [Cloze] will turn bullet points into x Cloze cards
- Card Bullet Point
- Card Bullet Point

#### Card Question [Cloze]    // 'Description:' will not be included in Cloze tags
- Description: Card Bullet Point
- Description: Card Bullet Point
```
