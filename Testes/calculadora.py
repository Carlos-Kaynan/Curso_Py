"""
Módulo usado no exercício test_calculadora.py.
Não é preciso alterar este arquivo: o exercício é escrever os testes para ele.
"""


def somar(a, b):
  return a + b


def subtrair(a, b):
  return a - b


def multiplicar(a, b):
  return a * b


def dividir(a, b):
  if b == 0:
    raise ValueError("não é possível dividir por zero")
  return a / b
