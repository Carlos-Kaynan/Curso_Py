"""
Problem Statement:
Faça um programa que receberá n pares de dados: uma categoria e um valor inteiro. O seu código deve somar os valores por categoria e imprimir o total de cada uma.
Obs.: pesquise um pouco mais sobre a função split() em Python, será necessária para essa questão.

Input:
n -> inteiro
n linhas, cada uma com uma categoria (string) e um valor (inteiro)

Output:
"{categoria}: {valor_total}"
"""

n = int(input())

categorias = {}

for _ in range(n):
  linha = input().split()
  categoria = linha[0]
  valor = int(linha[1])

  if categoria in categorias:
    categorias[categoria] += valor
  else:
    categorias[categoria] = valor

for cat, total in categorias.items():
  print(f"{cat}: {total}")
