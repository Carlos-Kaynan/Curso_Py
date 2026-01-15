"""
Problem Statement:
Escreva um programa que, leia um valor de custo e o percentual de lucro desejado, e na sequencia mostre o valor final do produto;

Input:
As entradas serão da seguinte forma;

custo -> float
percentual -> float

Output:
A saída deverá ser;
"Valor final do produto: R$ {valor_final}."

Obs.: a variável valor_final deverá ter 4 casas decimais.
"""

custo = float(input())
percentual = float(input())

calculo = (custo * percentual) / 100
valor_final = custo + calculo

print(f"Valor final do produto: R$ {valor_final:.4f}.")
