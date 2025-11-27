# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calclex import tokens

#para usar la raíz cuadrada
import math

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]
    
def p_factor_sqrt(p):
    'factor : SQRT LPAREN expression RPAREN'
    # Calcula la raíz cuadrada del valor de la expresión (p[3])
    p[0] = math.sqrt(p[3])

def p_factor_abs(p):
    'factor : ABS LPAREN expression RPAREN'
    # Calcula el valor absoluto del valor de la expresión (p[3])
    p[0] = abs(p[3])
    
def p_factor_exp(p):
    'factor : EXP LPAREN expression RPAREN'
    # Calcula la exponencia del valor de la expresión (p[3])
    p[0] = math.exp(p[3])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

#s es la cadena que se va a obtener de excel
s="6-3+4*sqrt(9)*exp(1)-abs(2)" #cadena de ejemplo
result = parser.parse(s)
print(result)

#while True:
#   try:
#       s = input('calc > ')
#   except EOFError:
#       break
#   if not s: continue
#   result = parser.parse(s)
#   print(result)
