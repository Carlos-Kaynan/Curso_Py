"""
Problem Statement:
Crie uma função somar(*numeros) que aceite QUALQUER quantidade de números e retorne a soma deles.
Leia os números em uma única linha, converta para float e chame a função desempacotando a lista: somar(*lista).

Input:
numeros -> string (números separados por espaço)

Output:
"A soma é {total}"

Obs.: total deve ter 2 casas decimais.

Examples:
Input:
1 2 3.5

Output:
A soma é 6.50
"""

# Escreva sua solução abaixo

def somar(*numeros):
    return sum(numeros)

# Leitura da entrada e conversão dos valores para float
entrada = input()
lista = [float(x) for x in entrada.split()]

# Chamada da função desempacotando a lista
total = somar(*lista)

# Exibição do resultado com 2 casas decimais
print(f"A soma é {total:.2f}")
