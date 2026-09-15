"""
Problem Statement:
Faça um programa que, dado uma string, crie uma função que conta quantas vezes cada vogal aparece na string.
Obs.: letras maiusculas e minusculas são consideradas, mas letras acentuadas não são.

Input:
word -> string

Output:
A saída deverá ser um dicionário, onde a chave corresponde a vogal e o valor é a quantidade de vezes que aquela vogal apareceu na variável word.
"""

word = input()

def contar_vogais(word):
  vogais = "aeiou"
  contagem = {v: 0 for v in vogais}
  for letra in word:
    letra_minuscula = letra.lower()
    if letra_minuscula in vogais:
      contagem[letra_minuscula] += 1
  return contagem

resultado = contar_vogais(word)
print(resultado)
