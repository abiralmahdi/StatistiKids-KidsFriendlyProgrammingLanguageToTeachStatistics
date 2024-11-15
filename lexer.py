import ply.lex as lex

# List of token names
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'IDENTIFIER',
    'EQUALS',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'STRING',
    'SEMICOLON'
)

# Regular expressions for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_STRING = r'\"([^\\\"]|\\.)*\"'
t_SEMICOLON = r';'


# Identifier (variable name) rule
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Number token rule
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignoring spaces and tabs
t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = 'x = 3 + 4 * 10'
lexer.input(data)
