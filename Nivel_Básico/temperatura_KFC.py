"""
Problem Statement:
Crie um programa que receba uma temperatura em Celsius e exiba a temperatura lida usando as escalas Kelvin (K) e Fahrenheit (F).

Considere as seguintes fórmulas:
K = C + 273
F = 1,8*C + 32

Input:
A entrada será da seguinte maneira:
temperatura_celsius -> float

Output:

"Temperatura em Kelvin: {temperatura_kelvin}K"
"Temperatura em Fahrenheit: {temperatura_fahrenheit}ºF"

Obs,: As variáveis temperatura_kelvin e temperatura_fahrenheit devem ter 2 casas decimais

"""

temperatura_celsius = float(input())

k = temperatura_celsius + 273
f = (1.8*temperatura_celsius) + 32

print(f"Temperatura em Kelvin: {k:.2f}K")
print(f"Temperatura em Fahrenheit: {f:.2f}ºF")
