"""
Problem Statement:
Escreva uma função chamada media(a, b, c) que recebe três números como argumentos e retorna a média aritmética entre eles.

Input:
n1 -> float
n2 -> float
n3 -> float

Output:
A saída deverá ser a média aritmética entre os três números, com duas casas decimais.
"""

def media(a, b, c):
  resultado = (a + b + c) / 3
  return round(resultado, 2)

n1 = float(input())
n2 = float(input())
n3 = float(input())

resultado = media(n1, n2, n3)
print(f"{resultado:.2f}")
