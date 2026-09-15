"""
Problem Statement:
Escreva um programa que recebe uma única frase como entrada e conta quantas vezes cada letra do alfabeto aparece, ignorando espaços, acentos e letras maiúsculas/minúsculas.
Exiba as letras e suas contagens em ordem alfabética.

Input:
frase -> string

Output:
"{letra}: {contagem" para cada letra que apareceu na frase.
"""

frase = input()

frase = frase.upper()

contagem = {}

for c in frase:
  if ('A' <= c <= 'Z') or ('À' <= c <= 'Ý'):  
    contagem[c] = contagem.get(c, 0) + 1

for letra in sorted(contagem.keys()):
  print(f"{letra}: {contagem[letra]}")
