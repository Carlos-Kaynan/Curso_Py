"""
Problem Statement:
A função eh_primo(n) abaixo é a lógica do exercício "numeros primos" (pasta Estruturas de Repetição),
agora dentro de uma função que RETORNA True ou False.
Escreva pelo menos 6 asserts que verifiquem casos importantes:
números negativos, 0, 1, 2, um primo maior (ex.: 97) e um número que não é primo (ex.: 91 = 7 x 13).
Se todos os asserts passarem, o programa deve imprimir a mensagem abaixo.
Depois, quebre a função de propósito (troque <= por <, por exemplo) e veja qual assert falha.

Input:
Não há entrada.

Output:
"Todos os testes passaram!"
"""


def eh_primo(n):
  if n <= 1:
    return False
  i = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i = i + 1
  return True


# Escreva seus asserts abaixo
