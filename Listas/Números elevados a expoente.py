'''
Problem Statement:
Faça um programa que receba 10 números digitados pelo usuário e, em seguida, leia um expoente. O programa deve criar e imprimir uma nova lista com cada número elevado ao expoente informado.

Input:
numero1 -> float
...
numero10 -> float
expoente -> inteiro

Output:
A saída deverá ser cada um dos 10 números elevados ao expoente, linha a linha.

Obs.: a saída deverá ter 2 casas decimais.
'''
numeros = []

for _ in range(10):
  numero = float(input())
  numeros.append(numero)

expoente = int(input())

for num in numeros:
  resultado = num ** expoente
  print(f"{resultado:.2f}")
