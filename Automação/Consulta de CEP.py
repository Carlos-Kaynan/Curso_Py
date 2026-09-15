"""
Problem Statement:
Usando a biblioteca requests (pip install requests), consulte a API gratuita ViaCEP:
    https://viacep.com.br/ws/{cep}/json/
A resposta vem em JSON (use resposta.json()) com campos como logradouro, bairro, localidade e uf.
Trate os casos de erro:
- CEP que não tem 8 dígitos (remova o traço antes de conferir): não faça a requisição
- CEP com 8 dígitos que não existe: a API responde com a chave "erro"
- Falha de conexão: capture requests.exceptions.RequestException

Input:
cep -> string (com ou sem traço)

Output:
Se encontrar:
"{logradouro}, {bairro} - {localidade}/{uf}"
Se o CEP for inválido:
"CEP inválido."
Se o CEP não existir:
"CEP não encontrado."
Se não conseguir conectar:
"Não foi possível consultar o CEP agora."

Examples:
Input:
01001-000

Output:
Praça da Sé, Sé - São Paulo/SP

Input:
123

Output:
CEP inválido.
"""

# Escreva sua solução abaixo
