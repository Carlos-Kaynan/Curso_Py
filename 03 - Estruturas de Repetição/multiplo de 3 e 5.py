'''
Problem Statement:
Faça um programa que, dado um valor n, exiba os valores de 0 a n que são múltiplos de 3, de 5 e de ambos.

Input:
n -> inteiro

Output:
Se o número for múltiplo de 3:
"{numero} é múltiplo de 3"

Se o número for múltiplo de 5:
"{numero} é múltiplo de 5"

Se for múltiplo de ambos:
"{numero} é múltiplo de 3 e de 5"

onde numero é um número dentro do intervalo de 0 a n
'''

n = int(input())

for i in range(n+1):
  if i % 3 == 0 and i % 5 == 0:
    print(f"{i} é múltiplo de 3 e de 5")
  elif i % 3 == 0:
    print(f"{i} é múltiplo de 3")
  elif i % 5 == 0  :
    print(f"{i} é múltiplo de 5")
    
