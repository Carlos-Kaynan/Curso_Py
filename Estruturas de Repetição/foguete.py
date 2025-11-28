'''
Problem Statement:
Faça um programa que, dado um número, faça a contagem regressiva até 0 para saber a hora do lançamento de um foguete

Input:
n -> inteiro

Output:
n

n-1

...

0

"O foguete decolou!"
'''


n = int(input())


for i in range(n, - 1, -1):
    print(i)

print("O foguete decolou!")
