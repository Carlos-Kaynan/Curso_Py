"""
Problem Statement:
Dada uma lista de n números inteiros e um valor inteiro k, crie uma nova lista com os elementos multiplicados por k e imprima o resultado.

Input:
elementos -> string
k -> inteiro
Os elementos da lista devem ser recebidos em uma única linha, separados por um espaço em branco, e devem ser convertidos para inteiro posteriormente.
Obs.: existe um espaço final em branco após a exibição do último elemento.

Output:
A saída deverá ser os elementos da nova lista, multiplicados por k, na mesma linha, separados por um espaço em branco entre eles.
"""

elementos_str = input()
k = int(input())

lista_original = [int(x) for x in elementos_str.split()]
lista_multiplicada = [elemento * k for elemento in lista_original]
saida_str = " ".join(map(str, lista_multiplicada))

print(saida_str + " ")
