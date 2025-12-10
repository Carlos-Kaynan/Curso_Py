"""
Problem Statement:
Dada uma lista de números inteiros distintos, escreva um programa que encontre o n-ésimo maior valor da lista.
O programa deve primeiro ler um inteiro t (tamanho da lista), depois t inteiros distintos n, e por fim um inteiro k, representando a posição do valor desejado na ordem crescente.
OBS.: Suponha t = 10
t1 = n1
t2 = n2
t3 = n3
. . .
t10 = n10

Input:
As entradas serão:
t -> inteiro
Depois de saber o tamanho da lista, você deve receber t inteiros, que são os n abaixo:
n -> inteiro
Por último, receber qual é a posição desejada
k -> inteiro

Output:
A saída deverá ser o k-ésimo maior valor que está na lista.
Obs.: k sempre estará no intervalo do tamanho da lista.
"""

t = int(input())

numeros = []
for _ in range(t):
  numeros.append(int(input()))

k = int(input())

numeros.sort()

print(numeros[k])
