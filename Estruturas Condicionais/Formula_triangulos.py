qqqqqqqqqqqqqqqqqqqqqqqqqq"""
Problem Statement:
Escreva um programa para ler o tamanho de três segmentos de retas e informar se estas 
podem formar um triângulo (a soma de quaisquer dois lados sempre deve ser maior que o terceiro lado).
Caso sim, também deve-se informar se este é equilátero (tem os três lados iguais), escaleno (tem os três lados diferentes) 
ou isósceles (tem apenas dois lados iguais).

Input:
lado_1 -> inteiro
lado_2 -> inteiro
lado_3 -> inteiro

Output:

Caso não seja um triângulo:
"Esses segmentos de reta não formam um triângulo. Tchau!!!!"

Caso forme um triângulo E seja equilátero:
"Triangulinho com todos os lados iguais: é equilátero!!"

Caso forme um triângulo E seja isósceles:
"Triangulinho com dois lados iguais: é isósceles!!"

Caso forme um triângulo E seja escaleno:
"Tem os três lados diferentes mas ainda continua sendo um triangulinho: é escaleno!!"
"""



lado_1 = int(input())
lado_2 = int(input())
lado_3 = int(input())

soma_1 = lado_1 + lado_2
soma_2 = lado_1 + lado_3
soma_3 = lado_2 + lado_3

if soma_1 > lado_3 and soma_2 > lado_2 and soma_3 > lado_1:
  
  if lado_3 == lado_2 and lado_3 == lado_1 and lado_2 == lado_1:
    print("Triangulinho com todos os lados iguais: é equilátero!!")
  
  elif lado_3 != lado_2 and lado_3 != lado_1 and lado_2 != lado_1:
    print("Tem os três lados diferentes mas ainda continua sendo um triangulinho: é escaleno!!")
  
  else:
    print("Triangulinho com dois lados iguais: é isósceles!!")
    
else:
  print("Esses segmentos de reta não formam um triângulo. Tchau!!!!")
