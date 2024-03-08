import re

# Definindo os padrões de expressões regulares para os tokens
tokens = [
    ('SELECT', r'SELECT'),
    ('FROM', r'FROM'),
    ('WHERE', r'WHERE'),
    ('ID', r'id'),
    ('NOME', r'nome'),
    ('SALARIO', r'salario'),
    ('NUMBER', r'\d+'),
    ('OPERATOR', r'[><=!]+'),
    ('COMMA', r','),
    ('SPACE', r'\s+')
]

# Função para analisar a string de entrada
def lexer(input_string):
    # Unir os padrões de expressões regulares
    regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)
    # Fazer o match da entrada com os padrões
    for match in re.finditer(regex, input_string):
        # Ignorar espaços em branco
        if match.lastgroup != 'SPACE':
            yield match.lastgroup, match.group()

# Testar o analisador léxico com uma consulta de exemplo
query = "SELECT id, nome, salario FROM empregados WHERE salario >= 820"
for token in lexer(query):
    print(token)
