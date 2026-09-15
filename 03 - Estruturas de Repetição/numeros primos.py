"""
Problem Statement:
Escreva um programa que recebe um número inteiro n e imprime Sim se ele for um número primo, ou Não caso contrário.

Input:
n -> inteiro

Output:
Se o número for primo:
"Sim, esse número é primo"
Caso contrário:
"O número não é primo"
"""

n = int(input())

if n <= 1:
    print("O número não é primo")

else:
    i = 2
    
    primo = True
    
    while i * i <= n:
        if n % i == 0:
            primo = False
            break
        i = i + 1
            
    if primo:
        print("Sim, esse número é primo")
    else:
        print("O número não é primo")
