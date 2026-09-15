"""
Problem Statement:
Implemente a busca binária de forma iterativa (com while).
A lista já vem ORDENADA. A cada passo, olhe o elemento do meio:
se for o alvo, achou; se for menor, procure na metade da direita; se for maior, na metade da esquerda.
Conte quantas comparações com o elemento do meio foram feitas.
Desafio extra: faça também uma versão recursiva (veja a pasta Recursão).

Input:
numeros -> string (inteiros em ordem crescente, separados por espaço)
alvo -> inteiro

Output:
Se encontrar:
"Encontrado na posição {indice} após {comparacoes} comparações"
Se não encontrar:
"Valor não encontrado após {comparacoes} comparações"

Examples:
Input:
1 3 5 7 9 11
7

Output:
Encontrado na posição 3 após 3 comparações

Input:
1 3 5 7 9 11
4

Output:
Valor não encontrado após 3 comparações
"""

# Escreva sua solução abaixo
