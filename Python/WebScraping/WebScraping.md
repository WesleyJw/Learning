# Data Mining: Web Scraping

Web scraping pode ser definido como a atividade de extrair dados de páginas ou simplesmente a coleta automatizada de dados da internet.

## Spider x Crawler

Um Crawler navega por divesas páginas, por exemplo o google, que navega por diversas páginas até obter uma repostar ou as  respostas com mais destaque. A spyder segue regras, estas estão dentro de um crawler. As spiders são responsáveis pela captura da informação desejada, o crawler determinar as condições e caminhos de captura.

## API's

API's fornecem dados de negócio com base em requisições HTTP. Quando estamos a procura de dados fazemos requisiçõs GET e a API é responsável por se comunicar com o sistema gerenciador de banco de dados informando quais os dados/informações requisitadas, retornando tudo aquilo previamente programado na API.

## Scrapy x Beautiful Soup

### Biblioteca Beautiful Soup

- É um conjunto de funções reutilizáveis;
- O código chama a biblioteca;
- Mais amigavel para quem está começando.

### Framework Scrapy

- É o framework (código) que dita a arquitetura do projeto;
- Maneira padrão e adequada de criar e implementar programas;
- Possui diversas bibliotecas embutidas;
- Maior vantagem para grandes projetos.

## Seletores

Seletores são métodos que identificam atributos e repassam endereços ao crawler ou Spider. Estes possuem o objetivo de selecionar elementos de forma padronizada do código HTML. Os dois seletores mais conhecidos são do tipo **CSS** e **XPath**.

### Seletores CSS

São utilizados para identificar elementos de estilização CSS, podem ser classes, id, name, title, entre outros. Desta forma, podemos identificar onde a informação está com base no estilo utilizado pelo autor do site.

### Seletores XPath

XPath é uma **linguagem de consulta**, que serve para identificar **tags** ou **elementos** específicos em documentos XML e HTML. XPath usa expressões de caminho para navegar por elementos e atributos em um documento XML (inclusive HTML). Estes são utilizados principalmente por grandes sites. Todo elemento html possui um endereço XPATH, desta forma é possível recuperar informações até mesmo não visíveis na tela. Exemplo de um endereço XPath **/html/body/section/p**. 