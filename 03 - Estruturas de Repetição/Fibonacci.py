"""
Problem Statement:
A sequência de Fibonacci é uma famosa sequência numérica onde cada número é a soma dos dois anteriores. Ela começa com os termos 0 e 1, e segue assim:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Ou seja:
O 0º termo é 0
O 1º termo é 1
A partir do 2º termo: F(n) = F(n-1) + F(n-2)
Faça um programa que, dado um número inteiro n, imprima todos os termos da sequência de Fibonacci menores ou iguais a n, linha a linha.

Input:
termo -> inteiro

Output:
Uma linha com os termos da sequência de Fibonacci menores ou iguais a n, linha a linha.
"""
n = int(input())

if n < 0:
    pass
    
elif n == 0:
    print(0)
    
else:
    a = 0
    b = 1
    
    print(a)
    
    while b <= n:
        print(b)
        
        proximo_termo = a + b
        
        a = b
        b = proximo_termo 
