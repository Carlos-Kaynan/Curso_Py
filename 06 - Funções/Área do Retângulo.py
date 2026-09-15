"""
Problem Statement:
Faça um programa que, dado os parâmetros base e altura, crie uma função que calcule a área de um retângulo.

Input:

base -> float
altura -> float

Output:
"A área do retângulo é {resultado}".

Obs.: resultado deve ter 2 casas decimais

"""

base = float(input())
altura = float(input())

def area_retangulo(base, altura):
  resultado = base * altura
  print(f"A área do retângulo é {resultado:.2f}")

area_retangulo(base, altura)
