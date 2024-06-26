import genanki
import re

list_tag = '<li>'

def parse_markdown(md_content):
    headers = re.findall(r'(#+) (.*)', md_content)
    content = re.split(r'#+ .*', md_content)[1:]
    cards = []

    for (level, header_text), text in zip(headers, content):
        level = len(level)
        card_text = text.strip()
        if level == 4:
            question = header_text.strip()
            tags = find_tags(headers, header_text)
            if '[Cloze]' in question:
                question = question.replace('[Cloze]', '').strip()
                cloze_cards = create_cloze_text(question, card_text)
                cards.extend(cloze_cards)
            else:
                answer = format_answer(card_text)
                cards.append(('Basic', question, answer, tags))

    return cards

def find_tags(headers, card_header):
    tags = []
    for (level, header_text) in headers:
        if header_text == card_header:
            break
        if len(level) == 3:  # ### means it's a tag
            tags = [header_text.strip().replace(' ', '_')]
    return tags

def format_answer(text):
    lines = text.split('\n')
    if any(line.startswith('-') for line in lines):
        formatted_lines = [list_tag + line.strip()[1:].strip() + list_tag if line.startswith('-') else line.strip() for line in lines if line.strip()]
        return '<ul>' + ''.join(formatted_lines) + '</ul>'
    else:
        return '<br>'.join(line.strip() for line in lines if line.strip())

def create_cloze_text(question, text):
    lines = text.split('\n')
    cloze_cards = []

    for i, line in enumerate(lines):
        if ':' in line:
            prefix, content = line.split(':', 1)
            cloze = '{{c1::' + content.strip() + '}}'
            cloze_line = prefix.strip() + ': ' + cloze
        else:
            cloze = '{{c1::' + line.strip() + '}}'
            cloze_line = cloze

        if any(l.startswith('-') for l in lines):
            cloze_text = '<ul>' + ''.join([list_tag + line.strip()[1:].strip() + list_tag if idx != i else list_tag + cloze_line[1:].strip() + list_tag for idx, line in enumerate(lines) if line.strip()]) + '</ul>'
        else:
            cloze_text = '<br>'.join(lines[:i] + [cloze_line] + lines[i+1:])

        cloze_cards.append(('Cloze', question, cloze_text, []))

    return cloze_cards

def create_anki_deck(deck_name, cards):
    my_deck = genanki.Deck(
        deck_id=2059400110,
        name=deck_name
    )

    basic_model = genanki.Model(
        model_id=1607392319,
        name='Basic Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
            {'name': 'Tags'}
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
            font-family: Arial;
            font-size: 20px;
            color: black;
            background-color: white;
        }
        ul {
            margin-top: 0;
            padding-left: 20px;
        }
        """
    )

    cloze_model = genanki.Model(
        model_id=1607392320,
        name='Cloze Model',
        fields=[
            {'name': 'Text'},
        ],
        templates=[
            {
                'name': 'Cloze Card',
                'qfmt': '{{cloze:Text}}',
                'afmt': '{{cloze:Text}}'
            },
        ],
        css="""
        .card {
            font-family: Arial;
            font-size: 20px;
            color: black;
            background-color: white;
        }
        ul {
            margin-top: 0;
            padding-left: 20px;
        }
        """,
        model_type=genanki.Model.CLOZE
    )

    for card_type, front, back, tags in cards:
        if card_type == 'Basic':
            note = genanki.Note(
                model=basic_model,
                fields=[front, back, ', '.join(tags)],
                tags=tags
            )
        elif card_type == 'Cloze':
            cloze_content = f"<b>{front}</b><br><br>{back}"
            note = genanki.Note(
                model=cloze_model,
                fields=[cloze_content],
                tags=tags
            )
        my_deck.add_note(note)

    return my_deck

def save_deck_to_file(deck, filename):
    genanki.Package(deck).write_to_file(filename)
