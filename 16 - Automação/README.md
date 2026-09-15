# Automação

Hora de usar Python para economizar tempo no dia a dia: organizar arquivos, gerar planilhas e buscar dados na internet.

## O que estudar
- `pathlib` e `shutil`: listar, criar, mover e renomear arquivos e pastas
- `openpyxl` (ou `pandas`): ler e gerar planilhas do Excel
- `requests`: consumir APIs que respondem em JSON
- `BeautifulSoup`: extrair informações de páginas web (web scraping)
- Próximos passos: automatizar o navegador com Selenium ou Playwright e agendar scripts (Agendador de Tarefas do Windows ou `cron`)

## Antes de começar
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS
pip install openpyxl requests beautifulsoup4
```

⚠️ Os scripts que mexem em arquivos devem ser testados primeiro em uma pasta de teste, nunca na sua pasta de Downloads de verdade.

📖 Documentação: https://docs.python.org/pt-br/3/library/pathlib.html
