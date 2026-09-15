"""
Problem Statement:
Melhore a "Lista telefonica" (pasta Dicionarios) para que os contatos fiquem salvos no arquivo agenda.json.
- Ao iniciar, se agenda.json existir, carregue o dicionário com json.load(); se não existir, comece com {}.
- Comandos aceitos (um por linha):
  "adicionar {nome} {telefone}" → salva o contato
  "buscar {nome}"              → mostra o telefone
  "sair"                       → grava o dicionário com json.dump() e encerra
- Os nomes não diferenciam maiúsculas de minúsculas.

Input:
comando -> string (várias linhas, até "sair")

Output:
Ao adicionar: "Contato {nome} salvo."
Ao buscar um contato existente: "{nome}: {telefone}"
Ao buscar um contato inexistente: "{nome} não está na agenda."
Ao sair: "Agenda salva com {quantidade} contato(s)."

Examples (rodando pela primeira vez, sem agenda.json):
Input:
adicionar Ana 99999-1111
adicionar Bruno 98888-2222
buscar ana
buscar Carla
sair

Output:
Contato ana salvo.
Contato bruno salvo.
ana: 99999-1111
carla não está na agenda.
Agenda salva com 2 contato(s).

Rodando de novo, "buscar bruno" já deve encontrar o contato salvo na execução anterior.
"""

# Escreva sua solução abaixo
