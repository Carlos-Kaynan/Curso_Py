"""
Problem Statement:
Simule a fila de atendimento de um banco usando collections.deque.
Comandos (um por linha):
- "chegou {nome}" → a pessoa entra no fim da fila
- "atender"       → a primeira pessoa da fila é atendida
- "fim"           → encerra o programa

Input:
comando -> string (várias linhas, até "fim")

Output:
Ao atender: "Atendendo: {nome}" ou, se não houver ninguém, "Fila vazia."
Ao encerrar: "Ainda na fila: {nomes}" (separados por vírgula e espaço) ou "Ninguém na fila."

Examples:
Input:
chegou Ana
chegou Bruno
atender
chegou Carla
atender
atender
atender
chegou Davi
fim

Output:
Atendendo: Ana
Atendendo: Bruno
Atendendo: Carla
Fila vazia.
Ainda na fila: Davi
"""

# Escreva sua solução abaixo
