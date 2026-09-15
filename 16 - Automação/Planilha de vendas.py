"""
Problem Statement:
Usando a biblioteca openpyxl (pip install openpyxl), leia o arquivo "../12 - Arquivos/vendas.csv"
e gere a planilha vendas.xlsx com:
- uma linha de cabeçalho: Produto | Quantidade | Preço unitário | Total (em negrito)
- uma linha para cada venda, com Total = Quantidade x Preço unitário
- uma última linha com o texto "TOTAL GERAL" e a soma da coluna Total
Dica: para achar o CSV independentemente de onde o script é executado, use
Path(__file__).parent.parent / "12 - Arquivos" / "vendas.csv"
Desafio extra: em vez de escrever o valor da soma, escreva a fórmula do Excel (ex.: "=SUM(D2:D7)").

Input:
Não há entrada pelo teclado.

Output:
"Planilha vendas.xlsx criada com {quantidade} vendas. Total geral: R$ {total}"

Obs.: total com 2 casas decimais.

Examples:
Output (com o vendas.csv da pasta "12 - Arquivos"):
Planilha vendas.xlsx criada com 6 vendas. Total geral: R$ 212.40
"""

# Escreva sua solução abaixo
