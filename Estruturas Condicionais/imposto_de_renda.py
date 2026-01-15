"""
Problem Statement:
Faça um programa que leia o valor da diária de um funcionário, a quantidade de dias que este trabalhou no mês e exiba o salário bruto, o Imposto de Renda (IR) a ser pago e o salário líquido. O cálculo do IR deve considerar os seguintes percentuais:
Salário até R$2.000,00 é isento de IR;
Salário entre R$2.000,00 e R$5.000,00 deve pagar 15% de IR
Salário superior a R$5.000,00 deve pagar 27,5% de IR.

Input:
valor_diaria -> float
dias_trabalhados -> inteiro

Output:
Se o salário bruto não pagar IR:
"Você está isento do Imposto de Renda."
"Seu salário é: R$ {salario_bruto}"

Se o salário bruto precisar pagar IR:
"Você não está isento do Imposto de Renda."
"Seu salário bruto é de: R$ {salario_bruto}"
"Seu valor do IR é: R$ {ir}"
"Seu salário líquido é de: R$ {salario_liquido}"

Obs.: todas as variáveis devem exibir 2 casas decimais.
"""

diaria = float(input())
dias_trabalhados = int(input())

salario = dias_trabalhados * diaria
ir = 0.0

if salario <= 2000:
  print(f"Você está isento do Imposto de Renda.")
  print(f"Seu salário é: R$ {salario:.2f}")
  
elif salario > 2000 and salario <= 5000:
  print("Você não está isento do Imposto de Renda.")
  print(f"Seu salário bruto é de: R$ {salario:.2f}")
  ir = 0.15 * salario
  salario_liquido = salario - ir
  print(f"Seu valor do IR é: R$ {ir:.2f}")
  print(f"Seu salário líquido é de: R$ {salario_liquido:.2f}")
elif salario > 5000:
  print("Você não está isento do Imposto de Renda.")
  print(f"Seu salário bruto é de: R$ {salario:.2f}")
  ir = 0.275 * salario
  salario_liquido = salario - ir
  print(f"Seu valor do IR é: R$ {ir:.2f}")
  print(f"Seu salário líquido é de: R$ {salario_liquido:.2f}")
