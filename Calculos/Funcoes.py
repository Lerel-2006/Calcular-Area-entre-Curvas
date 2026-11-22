import sympy as sp

x = sp.Symbol("x")

def interpretar_funcao(expressao):

    funcao = sp.sympify(expressao)

    return funcao