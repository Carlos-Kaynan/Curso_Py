'''
Problem Statement:
Faça um programa para ler números inteiros e positivos até o usuário não desejar continuar informando um novo número. Ao final, o programa deve exibir o total de números lidos e a soma deles.

Input:
confirmacao -> string
numero -> float
Obs.: A mensagem de confirmação é um "S" ou "s". Caso a variável confirmacao seja qualquer outra coisa, encerrar o código.

Output:
"Você digitou {quantidade} números"
"A soma final é: {soma}"
Obs.: soma deve ter 2 casas decimais
'''

contador = 0
soma = 0.0

confirmacao = input() 

while confirmacao == 'S' or confirmacao == 's':
  numero = float(input())
  soma += numero
  contador += 1
  confirmacao = input() 

print(f"Você digitou {contador} números")
print(f"A soma final é: {soma:.2f}")
