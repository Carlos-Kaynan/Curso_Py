"""
Problem Statement:
Faça um programa que leia os nomes (sem repetição), os preços de compra e os percentuais de lucro de 5 produtos. Após a leitura, exiba para cada produto seu nome, o preço de compra e o preço de venda calculado.

Input:
nome_produto -> string
preco_compra -> float
percentual_lucro -> float

Output:
A saída deverá ser, para cada um dos produtos!
"{nomes_produto}: Compra = R${preco_compra}, Venda = R${preco_venda}
Obs.: as variáveis preco_compra e preco_venda devem ter 2 casas decimais.
"""

nomes_produtos = []
precos_compra = []
precos_venda = []

for _ in range(5):
  nome = input()
  preco_compra = float(input())
  percentual_lucro = float(input())
  
  fator_lucro = percentual_lucro / 100
  preco_venda = preco_compra * (1 + fator_lucro)

  nomes_produtos.append(nome)
  precos_compra.append(preco_compra)
  precos_venda.append(preco_venda)

for i in range(5):
  nome = nomes_produtos[i]
  compra = precos_compra[i]
  venda = precos_venda[i]
  
  print(f"{nome}: Compra = R${compra:.2f}, Venda = R${venda:.2f}")
