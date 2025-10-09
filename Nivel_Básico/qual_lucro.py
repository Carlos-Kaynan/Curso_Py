"""
Problem Statement

Escreva um programa que, a partir de um valor de custo e de um valor de venda, mostre o valor do lucro obtido com a venda do produto.

Input:
As entradas serão as seguintes:

custo -> float

venda -> float

Output:
A saída deverá ser:

"O lucro obtido foi R$ {lucro}."

Obs.: lucro deverá ter 2 casas decimais.

Examples:

Input:
2
15

Output:
O lucro obtido foi R$ 13.00.
"""

custo = float(input())
venda = float(input())

lucro = venda - custo

print(f"O lucro obtido foi R$ {lucro:.2f}.")
