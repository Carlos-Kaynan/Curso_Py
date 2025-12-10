'''
Problem Statement:
Escreva um programa que, dado um inteiro N, imprimir a sequência de Collatz começando com N até que o número chegue a 1. Cada número da sequência deve ser impresso em uma nova linha.
A Sequência de Collatz é da seguinte forma:
Se o número for par, divida-o por 2.
Se o número for ímpar, multiplique-o por 3 e adicione 1.

Input:
n -> inteiro

Output:
A saída deverá ser a sequência de Collatz começando com N até que o número chegue a 1, linha a linha.
'''

n = int(input())

while n > 1:
  if n % 2 == 0:
    n = n // 2
  else:
    n = 3 * n + 1
  print(n)

