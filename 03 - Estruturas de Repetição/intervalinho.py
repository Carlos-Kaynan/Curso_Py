'''
Problem Statement:
Faça um programa para ler o primeiro e último número de uma sequência e depois exibir: a somatória desses dois números, os números pares e os números ímpares dentro desse intervalo da sequência.

Input:
primeiro -> inteiro
segundo -> inteiro
Obs.: considere que SEMPRE primeiro >= segundo.

Output:
"A soma dos números é: {soma}"
"Os números pares dentro da sequência são:"
(exibir números pares)

"Os números ímpares dentro da sequência são:"
(exibir números ímpares)
'''

num1 = int(input())
num2 = int(input())

print(f"A soma dos números é: {num1 + num2}")
print("")


print("Os números pares dentro da sequência são:")
for i in range (num1, num2+1):
  if i % 2 == 0:
    print(i)

print("")

print("Os números ímpares dentro da sequência são:")
for i in range (num1, num2+1):
  if i % 2 != 0:
    print(i)
    
