"""
Problem Statement:
Crie uma função area_retangulo(base, altura) que calcule e retorne a área de um retângulo.

Input:
base -> float
altura -> float

Output:
"A área do retângulo é {area}".

Obs.: area deve ter duas casas decimais
"""

base = float(input())
altura = float(input())

def area_retangulo(base, altura):
  area = base * altura
  print(f"A área do retângulo é {area:.2f}")

area_retangulo(base, altura)
