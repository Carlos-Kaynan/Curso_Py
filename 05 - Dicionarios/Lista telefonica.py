"""
Problem Statement
Faça um programa que armazena números de telefone de algumas pessoas em um dicionário. O programa deve receber entradas no formato nome telefone, uma por linha, até que o usuário digite "fim" para encerrar o cadastro. Depois disso, o programa deve ler um nome e imprimir o número correspondente, caso exista no dicionário.

Input:
linha -> string (pode ser nome telefone ou "fim")
Após o usuário digitar "fim", o programa deverá receber:
nome -> string (nome a ser consultado)

Output:
Caso o número exista na lista telefônica: {numero}
Caso contrário: "Essa pessoa não está na lista telefônica"
Atenção: a variável nome pode ser tanto maiuscula quanto minuscula e mesmo assim deve exibir o número correspondente, caso exista.
"""


agenda = {}

while True:
  linha = input().strip()

  if linha.lower() == "fim":
    break

  nome, telefone = linha.split()
  agenda[nome.lower()] = telefone

consulta = input().strip().lower()

if consulta in agenda:
  print(agenda[consulta])
else:
  print("Essa pessoa não está na lista telefônica")
