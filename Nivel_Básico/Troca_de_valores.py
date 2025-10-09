""" 

Problem Statement

Escreva um programa que permute (troque) o valor de duas variáveis inteiras.

Input

O input será composto por dois números inteiros:

a = inteiro

b = inteiro

Output

A saída será os valores de A e B após a troca de valores:

"Valor de a após permutação: {a}"

"Valor de b após permutação: {b}"

Examples

Case: 1

Input

45
50

Output

Valor de a após permutação: 50
Valor de b após permutação: 45
"""



a = int(input())
b = int(input())


a, b = b, a


print(f"Valor de a após permutação: {a}")
print(f"Valor de b após permutação: {b}")
