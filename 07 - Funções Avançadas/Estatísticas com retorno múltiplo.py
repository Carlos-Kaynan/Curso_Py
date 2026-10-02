"""
Problem Statement:
Crie uma função estatisticas(numeros) que recebe uma lista e RETORNA três valores de uma vez:
o menor número, o maior número e a média. Quem chama a função é que deve imprimir os resultados.
Dica: return menor, maior, media  →  menor, maior, media = estatisticas(lista)

Input:
numeros -> string (inteiros separados por espaço)

Output:
"Menor: {menor}"
"Maior: {maior}"
"Média: {media}"

Obs.: media deve ter 2 casas decimais.

Examples:
Input:
4 8 15 16 23 42

Output:
Menor: 4
Maior: 42
Média: 18.00
"""


def estatisticas(numeros):
    # Converte a string de números separados por espaço em uma lista de inteiros
    lista = [int(x) for x in numeros.split()]
    
    menor = min(lista)
    maior = max(lista)
    media = sum(lista) / len(lista)
    
    # Retorna os três valores de uma vez (tupla)
    return menor, maior, media

# Leitura do input
entrada = input()

# A função é chamada e os três valores são atribuídos às variáveis
menor, maior, media = estatisticas(entrada)

# Quem chamou a função é responsável por imprimir os resultados
print(f"Menor: {menor}")
print(f"Maior: {maior}")
print(f"Média: {media:.2f}")
