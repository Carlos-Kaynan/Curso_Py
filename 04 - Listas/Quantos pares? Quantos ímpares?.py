'''
Problem Statement:
Escreva um programa em Python que permita ao usuário digitar uma quantidade indeterminada de números inteiros, um por vez. Depois, o programa deverá exibir a quantidade de números digitados, a quantidade de números pares e a quantidade de números ímpares.

Inputs:
confirmacao -> string
numero -> inteiro
A variável de confirmacao só coletará um novo número SE o usuário digitar 's' ou 'S', indicando que ele quer digitar um novo valor.

Output:
"Quantidade de números digitados: {qtd_total}"
"Soma dos números pares: {soma_pares}"
"Soma dos números ímpares: {soma_impares}"

'''
numeros_digitados = []

primeiro_numero = int(input())
numeros_digitados.append(primeiro_numero)
confirmacao = input()

while confirmacao == 's' or confirmacao == 'S':
    
    numero = int(input())
    numeros_digitados.append(numero)
        
    confirmacao = input()

qtd_total = len(numeros_digitados)
soma_pares = 0
soma_impares = 0

for num in numeros_digitados:
    if num % 2 == 0:
        soma_pares = soma_pares + num
    else:
        soma_impares = soma_impares + num

print(f"Quantidade de números digitados: {qtd_total}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
