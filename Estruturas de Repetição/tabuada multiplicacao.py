'''
Problem Statement:
Escreva um programa que, dado um valor n, escreva a tabuada desse número (n x 1 até n x 10)

Input:
A entrada será a seguinte:
numero -> inteiro

Output:
** {numero} x {1} = {resultado} **
** {numero} x {2} = {resultado} ** ... ** {numero} x {10} = {resultado} **
'''

numero = int(input())

for i in range(1, 11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
