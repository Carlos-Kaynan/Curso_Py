"""
Problem Statement:
Faça um programa que, dado um saldo inicial, simule operações de depositar ou sacar.

Input:
** saldo -> float **
** operacao -> string **
Enquanto o usuário não colocar como entrada "sair" na * operacao *, o programa deverá ser capaz de executar as operação de depositar ou sacar.
Obs.: a operação de depositar só será feita se a variável operacao for "depositar" e a operação de sacar só será feita se a variável operacao for sacar.
Após verificar se a operação é válida ou não, seu programa deve receber o valor (float) que será depositado/sacado.

Output:
Ao final, seu programa deverá mostrar:
"Seu saldo era: R$ {saldo_anterior}"
"Seu novo saldo é: R$ {saldo_atual}"
As variáveis devem ter 2 casas decimais.

"""
saldo = float(input())
operacao = input()
saldo_inicial = saldo 

while operacao != "sair":
  if operacao == "depositar":
    valor = float(input())
    saldo = saldo + valor

  elif operacao == "sacar":
    valor = float(input())
    saldo = saldo - valor

  operacao = input()

print(f"Seu saldo era: R$ {saldo_inicial:.2f}")
print(f"Seu novo saldo é: R$ {saldo:.2f}")
