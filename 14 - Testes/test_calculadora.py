"""
Problem Statement:
Escreva testes com pytest para as funções do arquivo calculadora.py.
Já existe um teste de exemplo. Complete com pelo menos:
- um teste para subtrair, multiplicar e dividir;
- um teste com números negativos;
- um teste com números decimais (dica: use pytest.approx(0.3) para comparar 0.1 + 0.2);
- um teste que confirme que dividir(10, 0) lança ValueError (dica: with pytest.raises(ValueError):).

Como rodar:
Dentro da pasta "14 - Testes", execute: pytest

Output esperado:
Todos os testes passando (pontinhos verdes ou "passed" no terminal).
"""

import pytest

from calculadora import somar, subtrair, multiplicar, dividir


def test_somar():
  assert somar(2, 3) == 5


# Escreva seus testes abaixo
