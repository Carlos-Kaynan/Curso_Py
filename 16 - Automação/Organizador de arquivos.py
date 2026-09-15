"""
Problem Statement:
Faça um script que organize os arquivos de uma pasta em subpastas, de acordo com a extensão:
- Imagens: .jpg, .jpeg, .png, .gif
- Documentos: .pdf, .docx, .txt
- Planilhas: .xlsx, .csv
- Outros: qualquer outra extensão
Use pathlib.Path para listar os arquivos (ignore as subpastas) e shutil.move para movê-los.
As subpastas só devem ser criadas se forem necessárias (Path.mkdir(exist_ok=True)).

Para testar, crie antes uma pasta "bagunca" com arquivos vazios, por exemplo:
    from pathlib import Path
    pasta = Path("bagunca")
    pasta.mkdir(exist_ok=True)
    for nome in ["foto.jpg", "print.png", "contrato.pdf", "notas.txt", "gastos.xlsx", "musica.mp3"]:
        (pasta / nome).touch()

Input:
pasta -> string (caminho da pasta a organizar)

Output:
"{quantidade} arquivo(s) movido(s) para {subpasta}" para cada subpasta usada, em ordem alfabética

Examples:
Input:
bagunca

Output:
2 arquivo(s) movido(s) para Documentos
2 arquivo(s) movido(s) para Imagens
1 arquivo(s) movido(s) para Outros
1 arquivo(s) movido(s) para Planilhas
"""

# Escreva sua solução abaixo
