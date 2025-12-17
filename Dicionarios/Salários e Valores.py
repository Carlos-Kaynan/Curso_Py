"""
Problem Statement
Faça um programa para ler cpf, nome, salário de 10 funcionários. Ao final da leitura, exibir os nomes e salários de quem tem salário abaixo e acima da média, nessa ordem.

Input:
A entrada deverá ser, para cada um dos 10 funcionários:
cpf -> string
nome -> string
salario -> float

Output:
"Abaixo da média:"
{CPF} {Nome}
"Acima da média:"
{CPF} {Nome}
"""

for _ in range(10):
  cpf = input()
  nome = input()
  salario = float(input())

  funcionarios[cpf] = {"nome": nome, "salario": salario}

soma = 0
for cpf in funcionarios:
  soma += funcionarios[cpf]["salario"]

media = soma / 10

print("Abaixo da média:")
for cpf in funcionarios:
  if funcionarios[cpf]["salario"] < media:
    print(cpf, funcionarios[cpf]["nome"])

print("")

print("Acima da média:")
for cpf in funcionarios:
  if funcionarios[cpf]["salario"] > media:
    print(cpf, funcionarios[cpf]["nome"])
