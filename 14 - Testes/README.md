# Testes

Testes automatizados verificam se o seu código faz o que deveria, sem você precisar digitar as entradas toda vez.
Os exercícios do curso já têm entradas e saídas definidas, então são ótimos para praticar.

## O que estudar
- `assert` para checagens simples
- Separar a lógica em funções que **retornam** valores (é muito mais fácil testar um `return` do que um `print`)
- O bloco `if __name__ == "__main__":`, que permite importar um arquivo sem executar o `input()`
- A biblioteca `pytest`: arquivos `test_*.py`, funções `test_*` e `pytest.raises`

## Como rodar os testes desta pasta
```bash
pip install pytest
cd "14 - Testes"
pytest
```

📖 Documentação: https://docs.pytest.org/
