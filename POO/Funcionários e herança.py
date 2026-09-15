"""
Problem Statement:
Crie uma classe Funcionario com os atributos nome e salario e o método bonificacao(), que retorna 10% do salário.
Depois crie a classe Gerente, que HERDA de Funcionario e sobrescreve bonificacao():
o gerente recebe 15% do salário + R$ 1000,00.
Guarde todos os objetos em uma única lista e percorra essa lista chamando bonificacao()
sem usar if para saber o cargo (isso é polimorfismo!).

Input:
n -> inteiro
n linhas no formato "{cargo} {nome} {salario}", onde cargo é "funcionario" ou "gerente"

Output:
"{nome}: bonificação de R$ {valor}" para cada pessoa, na ordem de entrada

Obs.: valor com 2 casas decimais.

Examples:
Input:
3
funcionario Ana 3000
gerente Bruno 8000
funcionario Carla 4500

Output:
Ana: bonificação de R$ 300.00
Bruno: bonificação de R$ 2200.00
Carla: bonificação de R$ 450.00
"""

# Escreva sua solução abaixo
