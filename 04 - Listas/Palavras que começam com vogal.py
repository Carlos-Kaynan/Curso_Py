"""
Problem Statement:
Dado uma lista de palavras, crie uma nova lista contendo apenas as que começam com vogal.

Input:
confirmacao -> string
palavra -> string
Obs.: enquanto a variável confirmacao for diferente de 'fim', isso indica que o usuário quer digitar uma nova palavra para o programa.

Output:
A saída deverá ser todas as palavras digitadas pelo usuário que COMEÇAM com vogais, sendo exibidas linha a linha, de acordo com a ordem de entrada.
Se caso todas as palavras digitadas não começarem com vogal, o programa deverá exibir:
"Nenhuma palavra digitada começa com vogal."
"""

todas_as_palavras = []
vogais = 'aeiou'

while True:
  palavra = input()
  if palavra.lower() == "fim":
    break
  todas_as_palavras.append(palavra)

nenhuma_vogal = True

for palavra in todas_as_palavras:
  if palavra[0].lower() in vogais:
    print(palavra)
    nenhuma_vogal = False

if nenhuma_vogal:
  print("Nenhuma palavra digitada começa com vogal.")
