"""
Problem Statement:
Crie uma função potencia(n, x) que calcule e retorne n elevado a x SEM UTILIZAR o operador ** nem a função pow().
Obs.: considere que x é um inteiro maior ou igual a 0.

Input:
n -> float
x -> inteiro

Output:
"{n} elevado a {x} é {resultado}"

Obs.: resultado deve ter 2 casas decimais

Examples:
Input:
2
10

Output:
2.0 elevado a 10 é 1024.00
"""

def potencia(n, x):
  resultado = 1
  for _ in range(x):
    resultado = resultado * n
  return resultado

n = float(input())
x = int(input())

resultado = potencia(n, x)
print(f"{n} elevado a {x} é {resultado:.2f}")
