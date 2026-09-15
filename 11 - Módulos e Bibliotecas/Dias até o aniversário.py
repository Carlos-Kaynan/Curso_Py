"""
Problem Statement:
Usando o módulo datetime, leia a data de hoje e o dia/mês do aniversário de uma pessoa
e calcule quantos dias faltam para o PRÓXIMO aniversário.
Se o aniversário deste ano já passou, conte até o aniversário do ano que vem.
Dica: datetime.strptime(texto, "%d/%m/%Y").date() transforma o texto em data.
Obs.: considere que ninguém faz aniversário em 29/02.

Input:
hoje -> string no formato DD/MM/AAAA
aniversario -> string no formato DD/MM

Output:
Se o aniversário for hoje:
"Feliz aniversário!"
Caso contrário:
"Faltam {dias} dias para o seu aniversário."

Examples:
Input:
15/09/2026
20/09

Output:
Faltam 5 dias para o seu aniversário.

Input:
15/09/2026
10/01

Output:
Faltam 117 dias para o seu aniversário.
"""

# Escreva sua solução abaixo
