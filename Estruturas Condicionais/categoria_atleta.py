"""
Problem Statement:
Faça um programa que leia o nome, o sobrenome e a idade de um atleta e exiba seu nome completo e se ele está na categoria infantil (menor de 12 anos), juvenil (entre 12 e 17 anos), adulto (entre 18 e 35 anos) ou master (acima de 35 anos).

Input:
nome -> string
sobrenome -> string
idade -> inteiro

Output:
Se for da categoria infantil:
"A categoria do atleta {nome_completo} é a infantil."

Se for da categoria juvenil:
"A categoria do atleta {nome_completo} é a juvenil."

Se for da categoria adulto:
"A categoria do atleta {nome_completo} é a adulta."

Se for da categoria master:
"A categoria do atleta {nome_completo} é a master."

Obs.: nome completo é dado pela concatenação entre nome e sobrenome
"""

nome = input()
sobrenome = input()
idade = int(input())



nome_completo = nome + f" {sobrenome}"


categoria = ""


if idade < 12:
    categoria = "infantil"
    
elif idade <= 17:
    categoria = "juvenil"
    
elif idade <= 35:
    categoria = "adulta"
    
else:
    categoria = "master"
    

print(f"A categoria do atleta {nome_completo} é a {categoria}.")
