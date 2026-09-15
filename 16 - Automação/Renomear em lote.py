"""
Problem Statement:
Faça um script que renomeie todos os arquivos com uma extensão escolhida dentro de uma pasta,
usando um prefixo e uma numeração com 3 dígitos: foto_001.jpg, foto_002.jpg, ...
Os arquivos devem ser renomeados em ordem alfabética do nome original.
Use Path.glob() para encontrar os arquivos e Path.rename() para renomear.
Dica: f"{numero:03d}" escreve 1 como 001.

Para testar, crie uma pasta com alguns arquivos vazios, como no exercício "Organizador de arquivos".

Input:
pasta -> string
extensao -> string (ex.: .jpg)
prefixo -> string

Output:
"{nome_antigo} -> {nome_novo}" para cada arquivo renomeado
"{quantidade} arquivo(s) renomeado(s)."

Examples (pasta "fotos" com IMG_2931.jpg, IMG_0042.jpg e notas.txt):
Input:
fotos
.jpg
viagem

Output:
IMG_0042.jpg -> viagem_001.jpg
IMG_2931.jpg -> viagem_002.jpg
2 arquivo(s) renomeado(s).
"""

# Escreva sua solução abaixo
