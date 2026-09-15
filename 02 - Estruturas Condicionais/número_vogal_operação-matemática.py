"""
Problem Statement:
Escreva um programa para ler um ÚNICO caractere e depois informar se este é uma vogal, um número ou uma operação matemática (+, -, * ou /).
Obs.: A entrada da vogal pode ser tanto maiúscula quanto minúscula.
Você pode utilizar os métodos isnumeric( ) do Python
O input será comporto por um caractere

Input:
caractere = string

Output:
Quando o caractere for um número, a saída deverá ser:
"O caractere é um número"

Quando o caracter for uma operação matemática, a saída deverá ser:
"O caractere é uma operação matemática"

Quando o caractere for uma vogal, a saída deverá ser:
"O caractere é uma vogal"

"""

caractere = input()

if caractere.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("O caractere é uma vogal")
  
elif caractere in ('+', '-', '*', '/'):
    print("O caractere é uma operação matemática")

elif caractere.isnumeric():
    print("O caractere é um número")
