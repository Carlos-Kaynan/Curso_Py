"""
Problem Statement
Faça um programa que receberá nomes de pessoas, um por linha, até que o usuário digite "fim". Ao final, agrupe e imprima os nomes de acordo com a primeira letra do nome, ignorando se está em maiúsculo ou minúsculo. Os nomes devem ser agrupados em ordem alfabética da letra inicial e exibidos na ordem de inserção.

Input:
nome -> string (poderá ser o nome ou "fim")

Output:
"{letra}: {nomes}"
"""

grupos = {}

while True:
  nome = input().strip()
  if nome.lower() == "fim":
    break

  letra = nome[0].upper()


  if letra not in grupos:
    grupos[letra] = []

  grupos[letra].append(nome)

for letra in sorted(grupos.keys()):
    print(f"{letra}: {' '.join(grupos[letra])}")
