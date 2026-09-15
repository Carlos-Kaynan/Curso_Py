"""
Problem Statement
Crie uma função alunos_acima_da_media(nomes, notas) que recebe duas listas com os nomes e as notas dos alunos. 
Após isso, o programa deverá ser capaz de exibir o nome dos alunos que foram aprovados (nota >= 7)

Input:
n -> inteiro
E depois, de 0 a n-1, receber:

nome_do_aluno -> string
nota_do_aluno -> float

Output:
"Os alunos que foram aprovados foram: "

Seguido do nome dos alunos que foram aprovados, linha após linha.
"""

n = int(input())

def alunos_acima_da_media(nomes, notas):
  print("Os alunos que foram aprovados foram: ")
  for i in range(len(nomes)):
    if notas[i] >= 7:
      print(nomes[i])

nomes = []
notas = []

for _ in range(n):
  nome = input()
  nota = float(input())
  nomes.append(nome)
  notas.append(nota)

alunos_acima_da_media(nomes, notas)
