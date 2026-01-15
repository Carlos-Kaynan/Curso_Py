"""
Problem Statement:
Faça um programa para ler a média salarial dos funcionários e, na sequência, o nome e o salário de um dos funcionários dessa empresa. Ao terminar a leitura, exibir o nome do funcionário e se o seu salário é maior, menor ou igual a média salarial.

Input:
media_salarial -> float
nome_funcionario -> string
salario_funcionario -> float

Output:
As saídas deverão ser:
Se o salário do funcionário for maior que a média salarial:
"{nome_funcionario} recebe R$ {resultado} a mais do que a média salarial da empresa."

Se o salário do funcionário for menor que a média salarial:
"{nome_funcionario} recebe R$ {resultado} a menos do que a média salarial da empresa."

Se o salário do funcionário for igual a média salarial:
"{nome_funcionario} recebe igual a média salarial da empresa."

Obs.: a variável resultado é calculada a partir da diferença entre o salário do funcionário e a média salarial. Ela deve ter duas casas decimais.
"""

media_salarial = float(input())
nome_funcionario = input()
salario_funcionario = float(input())


if salario_funcionario > media_salarial:
  resultado = salario_funcionario - media_salarial
  print(f"{nome_funcionario} recebe R$ {resultado:.2f} a mais do que a média salarial da empresa.")

elif salario_funcionario < media_salarial:

  resultado = media_salarial - salario_funcionario
  print(f"{nome_funcionario} recebe R$ -{resultado:.2f} a menos do que a média salarial da empresa.")

else:
  print(f"{nome_funcionario} recebe igual a média salarial da empresa.")
