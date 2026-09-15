"""
Problem Statement:
Use @dataclass (from dataclasses import dataclass) para criar a classe Aluno, com os campos nome e notas (lista de floats)
e o método media().
Depois crie a classe Turma, que guarda uma lista de alunos e tem os métodos:
- adicionar(aluno)
- melhor_aluno(): retorna o Aluno com a maior média
- media_geral(): retorna a média das médias dos alunos

Input:
n -> inteiro
n linhas no formato "{nome} {nota1} {nota2} {nota3}"

Output:
"Melhor aluno: {nome} (média {media})"
"Média da turma: {media_geral}"

Obs.: médias com 2 casas decimais.

Examples:
Input:
3
Ana 8 9 10
Bruno 6 7 5.5
Carla 9 9.5 8

Output:
Melhor aluno: Ana (média 9.00)
Média da turma: 8.00
"""

# Escreva sua solução abaixo
