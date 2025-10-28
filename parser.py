#parser.py
import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# --- GRAMMAR RULES ---
def p_program(p):
    '''program : statement_list'''
    print(f"Program validated successfully.")


def p_statement_list(p):
    '''statement_list : statement NEWLINE statement_list
                      | statement
                      | empty'''
    pass

def p_block(p):
    '''block : statement_list'''
    pass

def p_statement(p):
    '''statement : assignment
                 | function_def
                 | if_statement
                 | return_statement'''
    pass

# 1. Assignment Operator
def p_assignment(p):
    'assignment : NAME EQUALS expression'
    print(f"Syntax OK: Assignment ({p[1]})")

# 2. Arithmetic Expression
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    pass

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    pass

def p_expression_term(p):
    '''expression : NUMBER
                  | NAME'''
    pass

# 3. if/else
def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN COLON NEWLINE block
                    | IF LPAREN condition RPAREN COLON NEWLINE block ELSE COLON NEWLINE block'''
    print("Syntax OK: If/Else Block")

def p_condition(p):
    '''condition : expression GT expression
                 | expression LT expression
                 | expression EQEQ expression
                 | expression GE expression
                 | expression LE expression
                 | expression NE expression'''
    pass

# 4. function definition
def p_function_def(p):
    'function_def : DEF NAME LPAREN parameters RPAREN COLON NEWLINE block'
    print(f"Syntax OK: Function Definition ({p[2]})")

def p_parameters(p):
    '''parameters : NAME COMMA parameters
                  | NAME
                  | empty'''
    pass

# 5. return statement
def p_return_statement(p):
    'return_statement : RETURN expression'
    print("Syntax OK: Return Statement")

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"*SYNTAX ERROR* at token '{p.value}' on line {p.lineno}.")
    else:
        print("*SYNTAX ERROR* at EOF.")

parser = yacc.yacc(debug=False)