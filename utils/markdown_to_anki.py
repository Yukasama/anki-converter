import genanki
import re

def parse_markdown(md_content):
    headers = re.findall(r'(#+) (.*)', md_content)
    content = re.split(r'#+ .*', md_content)[1:]
    cards = []

    for header, text in zip(headers, content):
        header_text = header[1].strip()
        card_text = text.strip()
        cards.append((header_text, card_text))

    return cards

def create_anki_deck(deck_name, cards):
    my_deck = genanki.Deck(
        deck_id=2059400110,
        name=deck_name
    )

    my_model = genanki.Model(
        model_id=1607392319,
        name='Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ]
    )

    for front, back in cards:
        note = genanki.Note(
            model=my_model,
            fields=[front, back]
        )
        my_deck.add_note(note)

    return my_deck

def save_deck_to_file(deck, filename):
    genanki.Package(deck).write_to_file(filename)