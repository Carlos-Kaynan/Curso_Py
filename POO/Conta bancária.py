"""
Problem Statement:
Transforme o "caixa eletronico" (pasta Estruturas de Repetição) em uma classe ContaBancaria.
- __init__(self, titular, saldo=0): guarda o titular e o saldo
- depositar(self, valor): soma o valor ao saldo
- sacar(self, valor): só saca se houver saldo; caso contrário, imprime "Saldo insuficiente."
- __str__(self): retorna "Conta de {titular} | Saldo: R$ {saldo}" (saldo com 2 casas decimais)

No programa principal, leia o titular e o saldo inicial, crie a conta e processe os comandos
"depositar {valor}" e "sacar {valor}" até aparecer "sair". No fim, faça print(conta).

Input:
titular -> string
saldo -> float
comando -> string (várias linhas, até "sair")

Output:
"Saldo insuficiente." sempre que um saque não puder ser feito
"Conta de {titular} | Saldo: R$ {saldo}" ao final

Examples:
Input:
Kaynan
100
depositar 250
sacar 80
sacar 500
sair

Output:
Saldo insuficiente.
Conta de Kaynan | Saldo: R$ 270.00
"""

# Escreva sua solução abaixo
