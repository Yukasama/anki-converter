import re

def clean_cloze(text):
    text = re.sub(r'\{\{c\d+::', '- ', text)
    text = text.replace('}}', '')
    return text

def read_and_clean_file(input_file_path):
    processed_lines = []
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not line or "Toggle Masks" in line or "#separator" in line or re.match(r'^[a-f0-9]{32}-ao-\d+$', line):
                continue
            line = clean_cloze(line)
            processed_lines.append(line)
    return processed_lines

def combine_lines(lines):
    combined_lines = []
    current_q = ""
    current_a = ""
    for line in lines:
        parts = line.split("\t")
        if len(parts) == 2:
            if current_q and current_a:
                combined_lines.append(f"{current_q}\n{current_a}")
            current_q, current_a = parts
            current_q = clean_cloze(current_q)
            current_a = clean_cloze(current_a)
        else:
            if current_q:
                current_a += " " + line
            else:
                current_q += " " + line
    if current_q and current_a:
        combined_lines.append(f"{current_q}\n{current_a}")
    return combined_lines

def format_combined_lines(combined_lines):
    formatted_lines = []
    for entry in combined_lines:
        q, a = entry.split("\n", 1)
        a_lines = a.split("- ")
        a_formatted = "\n".join([f"- {line.strip()}" for line in a_lines if line.strip()])
        formatted_lines.append(f"{q.strip()}\n{a_formatted}")
    return formatted_lines

def save_to_file(lines, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write("\n\n".join(lines))

# File paths
input_file_path = 'test.txt'
output_file_path = 'processed_anki_formatted.txt'

# Process the file
cleaned_lines = read_and_clean_file(input_file_path)
combined_lines = combine_lines(cleaned_lines)
formatted_lines = format_combined_lines(combined_lines)
save_to_file(formatted_lines, output_file_path)
