"""
Problem Statement:
Faça um programa para ler quatro números inteiros (n1, n2, n3 e n4) e depois exibir todos que são 
pares e positivos, pares e negativos, ímpares e positivos, ímpares e negativo e zero, nesta ordem.

Input:
n1 -> inteiro
n2 -> inteiro
n3 -> inteiro
n4 -> inteiro

Output:
"Números pares e positivos:"
E os números que são pares e positivos

"Números pares e negativos:"
E os números que são pares e negativos

"Números ímpares e positivos:"
E os número que são ímpares e positivos

"Números ímpares e negativos:"
E os número que são ímpares e negativos

"Números zeros:"
E exibir os números que são 0
"""

n1 = int(input())

n2 = int(input())

n3 = int(input())

n4 = int(input())

print("Números pares e positivos:")
if n1 > 0 and n1 % 2 == 0:
  print(n1)
if n2 > 0 and n2 % 2 == 0:
  print(n2)
if n3 > 0 and n3 % 2 == 0:
  print(n3)
if n4 > 0 and n4 % 2 == 0:
  print(n4)

print("")
print("Números pares e negativos:")
if n1 < 0 and n1 % 2 == 0:
  print(n1)
if n2 < 0 and n2 % 2 == 0:
  print(n2)
if n3 < 0 and n3 % 2 == 0:
  print(n3)
if n4 < 0 and n4 % 2 == 0:
  print(n4)
  
print("")
print("Números ímpares e positivos:")
if n1 > 0 and n1 % 2 != 0:
  print(n1)
if n2 > 0 and n2 % 2 != 0:
  print(n2)
if n3 > 0 and n3 % 2 != 0:
  print(n3)
if n4 > 0 and n4 % 2 != 0:
  print(n4)

print("")
print("Números ímpares e negativos:")
if n1 < 0 and n1 % 2 != 0:
  print(n1)
if n2 < 0 and n2 % 2 != 0:
  print(n2)
if n3 < 0 and n3 % 2 != 0:
  print(n3)
if n4 < 0 and n4 % 2 != 0:
  print(n4)

print("")
print("Números zeros:")
if n1 == 0:
  print(n1)
if n2 == 0:
  print(n2)
if n3 == 0:
  print(n3)
if n4 == 0:
  print(n4)
  
