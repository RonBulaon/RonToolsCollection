# Filename: toc.py
# Author  : Ron Bulaon - https://github.com/RonBulaon/toolbox

import re
import sys

def create_toc(markdown_file):
    try:
        with open(markdown_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{markdown_file}' not found.")
        return

    toc = []
    header_pattern = re.compile(r'^(#+) (.*)')

    for line in lines:
        match = header_pattern.match(line)
        if match:
            level = len(match.group(1)) - 1  # Subtract 1 to make '##' a level 1
            header_title = match.group(2).strip()
            anchor = header_title.lower().replace(' ', '-').replace('.', '').replace(',', '').replace('(', '').replace(')', '')
            toc.append(f"{'  ' * level}- [{header_title}](#{anchor})")

    toc_str = '\n'.join(toc)
    return toc_str

def update_markdown_file(file_name, toc):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    updated_content = re.sub(r'<!-- toc -->.*?<!-- /toc -->', f'<!-- toc -->\n{toc}\n<!-- /toc -->', content, flags=re.DOTALL)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# Main function to take file name from command line argument
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_toc.py <markdown_file.md>")
    else:
        markdown_file = sys.argv[1]
        toc = create_toc(markdown_file)
        if toc:
            update_markdown_file(markdown_file, toc)
            print(f"Updated Table of Contents in '{markdown_file}'")
