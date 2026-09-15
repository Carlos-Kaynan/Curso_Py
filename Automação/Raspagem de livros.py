"""
Problem Statement:
Faça web scraping do site https://books.toscrape.com/, uma livraria de mentira criada justamente para praticar.
Use requests para baixar a página e BeautifulSoup (pip install beautifulsoup4) para extrair,
da primeira página, o título e o preço de cada livro.
Dicas:
- Cada livro fica em um <article class="product_pod">
- O título completo está no atributo "title" do link dentro do <h3>
- O preço está no <p class="price_color">
- Use BeautifulSoup(resposta.content, "html.parser") para o símbolo £ aparecer corretamente

Depois, mostre os livros e o mais caro da página.

Input:
Não há entrada pelo teclado.

Output:
"{titulo} - {preco}" para cada livro da primeira página
"Livros encontrados: {quantidade}"
"Mais caro: {titulo} ({preco})"

Examples:
A primeira linha da saída deve ser:
A Light in the Attic - £51.77
E a página tem 20 livros.
"""

# Escreva sua solução abaixo
