"""
Problem Statement:
Escreva um programa que recebe valores para serem adicionados numa lista. Após isso, o programa deverá exibir quantas vezes os valores aparecem dentro da lista.

Input:
confirmacao -> string
n -> float
Enquanto confirmacao for "s" ou "S", receber valores para a variável n. Quando confirmacao for diferente do esperado, exibir quantas vezes os elementos aparecem dentro dela.

Output:
A saída deverá ser, por ordem de entrada dos elementos na lista:
O elemento {elemento0} aparece {quantidade_repeticoes0} vezes na lista
O elemento {elemento1} aparece {quantidade_repeticoes1} vezes na lista
Até o último elemento diferente da lista.
Atenção: a saída só deverá ser exibida se o n for diferente e já não tiver sido exibido anteriormente.
Por exemplo, se as entradas foram [2,2,4,5], a saída deverá ser:
O elemento 2.0 aparece 2 vezes na lista
O elemento 4.0 aparece 1 vezes na lista
O elemento 5.0 aparece 1 vezes na lista
Ou seja, seu programa não deve exibir a mesma mensagem para o número 2 simplesmente porque ele aparece duas vezes na lista.
"""

lista_numeros = []
elementos_unicos_na_ordem = []

n = float(input())
lista_numeros.append(n)
if n not in elementos_unicos_na_ordem:
  elementos_unicos_na_ordem.append(n)

confirmacao = input()

while confirmacao == 's' or confirmacao == 'S':
  n = float(input())
  lista_numeros.append(n)

  if n not in elementos_unicos_na_ordem:
    elementos_unicos_na_ordem.append(n)

  confirmacao = input()

for elemento in elementos_unicos_na_ordem:
  contagem = lista_numeros.count(elemento)
  print(f"O elemento {elemento} aparece {contagem} vezes na lista")
