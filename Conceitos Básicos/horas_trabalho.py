"""
Problem Statement:
Escreva um programa que leia o salário de uma pessoa, quantas horas ela trabalha por dia e quantos dias ela trabalhou no mês. Em seguida, calcule e exiba quanto essa pessoa recebe por hora.

Input:
As entradas serão;

salário -> float
horas_por_dia -> inteiro
dias_trabalhados -> inteiro

Output:
A saída deve ser da seguinte maneira;
"Eu recebo uma mixuruca de R$ {valor_hora} por hora trabalhada."

Obs.: valor_hora deve ter uma casa decimal apenas.
"""

salario = float(input())
horas_p_dia = float(input())
dias_trab = int(input())


salario_p_hora = salario / (dias_trab * horas_p_dia)

print(f"Eu recebo uma mixuruca de R$ {salario_p_hora:.1f} por hora trabalhada.")
