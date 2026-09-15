# Arquivos

Até agora, tudo o que o programa guardava sumia quando ele terminava. Com arquivos, os dados ficam salvos.

## O que estudar
- `open()` e os modos `"r"`, `"w"` e `"a"`
- Sempre usar `with open(...) as arquivo:` (fecha o arquivo sozinho)
- Ler linha a linha, `read()`, `readlines()` e `write()`
- Sempre informar `encoding="utf-8"` (por causa dos acentos)
- Arquivos CSV com o módulo `csv` (`csv.reader` e `csv.DictReader`)
- Arquivos JSON com o módulo `json` (`json.load` e `json.dump`)
- Caminhos de arquivos com `pathlib.Path`

O arquivo `vendas.csv` desta pasta é usado no exercício "Relatório CSV".

📖 Documentação: https://docs.python.org/pt-br/3/tutorial/inputoutput.html
