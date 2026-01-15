"""
Problem Statement:
Em um evento, foram vendidos dois tipos de ingressos:
Meia-entrada: custa metade do valor do ingresso inteiro.
Inteira: valor cheio do ingresso.

Sabendo que:
Uma quantidade total de ingressos foi vendida.
Um certo percentual dos ingressos vendidos foi de meia-entrada, e o restante de inteira.
O valor do ingresso inteiro é informado pelo usuário.
Escreva um programa que leia:

A quantidade total de ingressos vendidos;
O percentual de ingressos vendidos como meia-entrada (o restante será inteira);
O valor do ingresso inteiro.
O programa deve calcular e exibir:
A quantidade de ingressos meia-entrada e inteiros vendidos;
O valor faturado com cada tipo de ingresso;
O valor total arrecadado com as vendas.

Input:
O input será composto por três valores:

Quantidade de ingressos = inteiro;
O percentual de ingressos vendidos como meia-entrada (o restante será inteira) = inteiro;
O valor do ingresso inteiro = float.

Output:
O output será da seguinte forma:

"Quantidade de ingressos meia-entrada: {total_meia}"
"Quantidade de ingressos inteiros: {total_inteira}"
"Faturamento com meia-entrada: R${faturamento_meia}"
"Faturamento com inteira: R${faturamento_inteira}"
"Faturamento total: R${faturamento_total}"

Atenção: As saídas de faturamento deverão ter apenas duas casas decimais após a vírgula!
"""

total_ingressos = int(input())
percentual = int(input())
valor_ingresso = float(input())



qtd_meia = (total_ingressos * percentual) / 100
valor_total_meia = qtd_meia * (valor_ingresso / 2)
qtd_inteira = total_ingressos - qtd_meia
valor_total_inteira = qtd_inteira * valor_ingresso
valor_total = valor_total_meia + valor_total_inteira

print(f"Quantidade de ingressos meia-entrada: {qtd_meia:.0f}")
print(f"Quantidade de ingressos inteiros: {qtd_inteira:.0f}")
print(f"Faturamento com meia-entrada: R${valor_total_meia:.2f}")
print(f"Faturamento com inteira: R${valor_total_inteira:.2f}")
print(f"Faturamento total: R${valor_total:.2f}")
