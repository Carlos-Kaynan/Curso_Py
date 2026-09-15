""" 
Problem Statement:
Faça um programa que, solicite a altura e o raio de um cilindro, calcule o volume total do cilindro (use π=3.14) e exiba esse valor.

Input:
As entradas serão as seguintes:
altura -> float
raio -> float

Para cálculo do volume, considere que π=3.14
Obs.: o resultado do volume deve ter duas casas decimais

Output:
A saída deverá ser:
"O volume do cilindro que tem {ALTURA} de altura e {RAIO} de raio é igual a {VOLUME}"

"""

altura = float(input())
raio = float(input())

raio_quadrado = raio**2
volume = 3.14 * altura * raio_quadrado

print(f"O volume do cilindro que tem {altura} de altura e {raio} de raio é igual a {volume:.2f}")
