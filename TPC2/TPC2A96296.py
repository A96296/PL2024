import sys
import re

def markdown_to_html(markdown_text):
    # Cabeçalhos
    markdown_text = markdown_text.replace('# ', '<h1>').replace('\n', '</h1>\n', 1)
    markdown_text = markdown_text.replace('## ', '<h2>').replace('\n', '</h2>\n', 1)
    markdown_text = markdown_text.replace('### ', '<h3>').replace('\n', '</h3>\n', 1)

    # Bold
    markdown_text = markdown_text.replace('**', '<b>', 1).replace('**', '</b>', 1)

    # Itálico
    markdown_text = markdown_text.replace('*', '<i>', 1).replace('*', '</i>', 1)

    # Lista numerada
    lines = markdown_text.split(',')
    if re.match(r'\d+\. .*', lines[0].lstrip()):
        markdown_text = '<ol>\n'
        for line in lines:
            match = re.match(r'(\d+)\. (.*)', line.lstrip())
            if match:
                markdown_text += f'<li>{match.group(2)}</li>\n'
        markdown_text += '</ol>'

    # Imagem
    markdown_text = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', markdown_text)

    # Link
    markdown_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', markdown_text)

    return markdown_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python nome_do_script.py 'markdown_text'")
        sys.exit(1)

    markdown_text = sys.argv[1]
    html_output = markdown_to_html(markdown_text)
    print(html_output)
