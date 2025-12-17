"""
Problem Statement:
Dado um número inteiro positivo n, crie um dicionário onde as chaves vão de 1 até n, e os valores são os quadrados das chaves.

Input:
n -> inteiro

Output:
"{chave}: {valor}"
Para cada um dos elementos do dicionário.
"""

n = int(input())

d = {}

for i in range(1, n + 1):
    d[i] = i * i

for chave, valor in d.items():
    print(f"{chave}: {valor}")
