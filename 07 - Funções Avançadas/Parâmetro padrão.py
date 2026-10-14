"""
Problem Statement:
Crie uma função saudacao(nome, cumprimento="Olá") que RETORNA a frase de saudação.
Se o usuário não digitar nenhum cumprimento (linha vazia), a função deve ser chamada sem esse argumento,
usando o valor padrão "Olá".

Input:
nome -> string
cumprimento -> string (pode ser vazia)

Output:
"{cumprimento}, {nome}!"

Examples:
Input:
Kaynan
(linha vazia)

Output:
Olá, Kaynan!

Input:
Ana
Bom dia

Output:
Bom dia, Ana!
"""

# Escreva sua solução abaixo

def saudacao(nome, cumprimento="Olá"):
    return f"{cumprimento}, {nome}!"

# Leitura das entradas
nome = input().strip()
cumprimento_input = input().strip()

# Se a segunda linha for vazia, chama a função usando apenas o primeiro argumento (usando o valor padrão)
if complemento_input := cumprimento_input:
    mensagem = saudacao(nome, complemento_input)
else:
    mensagem = saudacao(nome)

print(mensagem)
