'''
Problem Statement
Faça um programa que receba dois valores inteiros (a e b), e faça a divisão de a por b SEM UTILIZAR o operador / ou //.
Obs.: considere sempre que a >= b

Input:
a -> inteiro
b -> inteiro

Output:
A saída deverá ser o quociente da divisão de a por b.
'''

a = int(input())
b = int(input())

cociente = 0

while a >= b:
  a = a - b
  cociente = cociente + 1

print(cociente)
