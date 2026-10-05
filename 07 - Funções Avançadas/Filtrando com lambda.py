"""
Problem Statement:
Leia uma lista de números inteiros e, usando filter() e map() com funções lambda,
crie uma nova lista apenas com os números PARES elevados ao quadrado.
Não use for nem list comprehension neste exercício.

Input:
numeros -> string (inteiros separados por espaço)

Output:
A nova lista, exibida com print(lista).

Examples:
Input:
1 2 3 4 5 6

Output:
[4, 16, 36]
"""

# Escreva sua solução abaixo

def processa_pares_ao_quadrado(numeros_str):
    # Converte a string de inteiros para uma lista de números
    numeros = list(map(int, numeros_str.split()))
    
    # Filtra os pares e eleva ao quadrado usando filter, map e lambda
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros)))

# Leitura do input
entrada = input()

# Chamada da função
resultado = processa_pares_ao_quadrado(entrada)

# Exibe a lista final
print(resultado)
