#lexer.py
import ply.lex as lex

# --- TOKENS ---
tokens = (
    # Operators and Punctuation
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'COLON', 'COMMA',
    'LPAREN', 'RPAREN',
    # Relational Operators
    'GT', 'LT', 'EQEQ', 'GE', 'LE', 'NE',
    'NAME', 'NUMBER',
    'NEWLINE',
)

# --- RESERVED WORDS ---
reserved = {
    'if': 'IF', 'else': 'ELSE', 'def': 'DEF', 'return': 'RETURN',
}

tokens = tokens + tuple(reserved.values())

# --- REGEX ---
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUALS    = r'='
t_COLON     = r':'
t_COMMA     = r','
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_GE        = r'>='
t_LE        = r'<='
t_NE        = r'!='
t_GT        = r'>'
t_LT        = r'<'
t_EQEQ      = r'=='
t_ignore = ' \t'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define NEWLINE 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = 'NEWLINE'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()