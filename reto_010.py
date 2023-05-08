"""
Reto #10 - EXPRESIONES EQUILIBRADAS
Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

symbols_open = {"{","[","("}
symbols_close = {"}","]",")"}
open = 0
close = 0
expression = "{ [ a * ( c + d ) ] - 5 }"

for c in expression:
    if c in symbols_open:
        open += 1
    if c in symbols_close:
        close += 1

print()
if open != close:
    print("Tu expresion no esta balanceada.")
else:
    print("Tu expresion esta balanceada.")
