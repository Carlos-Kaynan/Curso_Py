"""
Problem Statement:
Faça um programa que, dado uma string, conte a quantidade de vogais que aparecem naquela palavra.
Obs.: letras maiusculas e minusculas devem ser consideradas, mas letras acentuadas não.

Input:
word -> string
Output

A saída deverá ser:
"A quantidade de vogais em {palavra} é {resultado_contagem}"

"""

word = input()

def contar_vogais(word):
  vogais = "aeiouAEIOU"
  contador = 0
  for letra in word:
    if letra in vogais:
      contador += 1
  print(f"A quantidade de vogais em {word} é {contador}")



contar_vogais(word)
