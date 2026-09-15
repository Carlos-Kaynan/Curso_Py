'''
Problem Statement:
Faça um programa que leia o nome e a nota de vários alunos (a entrada termina quando for digitado um nome vazio OU quando a entrada for "fim"). Armazene os nomes em uma lista e as notas em outra. Em seguida, exiba os nomes dos alunos ordenados da maior para a menor nota.

Input:
nome_aluno -> string
Caso nome_aluno seja diferente de "fim", o programa deve receber outra variável:
nota_aluno -> float

Output:
O programa deverá exibir nome e nota, da maior para a menor nota, separado linha a linha.

Obs.: caso as notas sejam as mesmas, exibir por ordem de entrada no programa.
Obs.: a saída de notas deve ter 2 casas decimais

'''

nomes = []
notas = []

while True:
  nome = input()
  if not nome or nome.lower() == "fim":
    break
  nota = float(input())

  nomes.append(nome)
  notas.append(nota)

dados_alunos = list(zip(nomes, notas))

dados_ordenados = sorted(dados_alunos, key=lambda x: x[1], reverse=True)

for nome, nota in dados_ordenados:
    print(f"{nome}: {nota:.2f}")
