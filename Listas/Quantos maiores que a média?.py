'''
Problem Statement:
Dada uma lista de n números, calcule a média aritmética e conte quantos elementos são maiores do que ela.

Input:
elementos -> string
Os elementos da lista devem ser recebidos em uma única linha, separados por um espaço em branco, e devem ser convertidos para inteiro posteriormente.

Output:
A saída deverá ser a quantidade de números que são maiores que a média aritmética.
'''
entrada_str = input()
elementos_str = entrada_str.split()

soma = 0
n = 0
lista_numeros = []

for x in elementos_str:
  numero = int(x)
  lista_numeros.append(numero)
  soma = soma + numero
  n = n + 1

if n == 0:
  media = 0
else:
  media = soma / n

contador_maiores = 0

for numero in lista_numeros:
  if numero > media:
    contador_maiores = contador_maiores + 1

print(contador_maiores)
