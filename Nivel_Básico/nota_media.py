"""
Problem Statement:
Escreva um programa que leia as 2 notas de um aluno em uma disciplina, depois exiba quantos pontos o aluno ficou distante da nota 10 para cada avaliação, sua média e quantos pontos a média do aluno ficou distante da nota 10.

Input:
O input será composto por dois números, que irão representar a nota 1 e 2 do aluno:

Nota 1 = Float
Nota 2 = Float

Output:
A saída será da seguinte ordem:

Distância da nota 1 para 10
Distância da nota 2 para 10
Média
Distância da média para 10

"""

nota1 = float(input())
nota2 = float(input())

distancia1 = 10 - nota1
distancia2 = 10 - nota2

media = (nota1 + nota2) / 2

dist_media = 10 - media

print(f"{distancia1}\n{distancia2}\n{media}\n{dist_media}")
