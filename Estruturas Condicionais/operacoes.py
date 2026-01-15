#Operação com dois números

"""
Problem Statement:
Faça um programa para ler dois número (n1 e n2) e uma operação da matemática (+, -, * ou /) e exiba o resultado dessa operação entre esses dois números.

Input:
n1 -> float
n2 -> float
operacao -> string

Output:
Se for uma operação de soma:
"Você escolheu a operação de adição. O resultado dessa adição é {n1 + n2}"

Se for uma operação de subtração:
"Você escolheu a operação de subtração. O resultado dessa subtração é {n1 - n2}"

Se for uma operação de multiplicação:
"Você escolheu a operação de multiplicação. O resultado dessa multiplicação é {n1 * n2}"

Se for uma operação de divisão:
"Você escolheu a operação de divisão. O resultado dessa divisão é {n1 / n2}"

Obs.: todos os resultados devem ter pelo menos duas casas decimais.
"""

num1 = float(input())
num2 = float(input())
operacao = input()

resultado = 0
nome_operacao = ""


if operacao == "+":
  resultado = num1 + num2
  nome_operacao = "adição"
  
elif operacao == "-":
  resultado = num1 - num2
  nome_operacao = "subtração"

elif operacao == "*":
  resultado = num1 * num2
  nome_operacao = "multiplicação"

elif operacao == "/":
  resultado = num1 / num2
  nome_operacao = "divisão"

  
print(f"Você escolheu a operação de {nome_operacao}. O resultado dessa {nome_operacao} é {resultado:.2f}")
