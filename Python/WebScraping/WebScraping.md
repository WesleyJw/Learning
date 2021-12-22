# Data Mining: Web Scraping

Web scraping pode ser definido como a atividade de extrair dados de páginas ou simplesmente a coleta automatizada de dados da internet.

## Spider x Crawler

Um Crawler navega por divesas páginas, por exemplo o google, que navega por diversas páginas até obter uma repostar ou as  respostas com mais destaque. A spyder segue regras, estas estão dentro de um crawler. As spiders são responsáveis pela captura da informação desejada, o crawler determinar as condições e caminhos de captura.

## API's

API's fornecem dados de negócio com base em requisições HTTP. Quando estamos a procura de dados fazemos requisiçõs GET e a API é responsável por se comunicar com o sistema gerenciador de banco de dados informando quais os dados/informações requisitadas, retornando tudo aquilo previamente programado na API.

## Scrapy x Beautiful Soup

Para o desenvolvimento de spiders ("aranhas/robôs") que raspam dados da internet existem algumas bibliotecas especializadas em python. A biblioteca *urllib* possui diversos métodos para realizar requisições em protocolos http, bem como módulos para acomphanhar os status das requisições. Por isso, esta biblioteca é bastante utilizada. Temos ainda, a biblioteca BeautifulSoup que permite acessar conteúdos de páginas web lidas. Esta biblioteca possui diversos métodos para encontrar elementos tageados. Selenium é outra biblioteca que permite de forma rápida interagir com a página e recuperar dados. No entanto, a ferramenta mais completa e robusta para este tipo de atividade é o framework **Scrapy**.

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

## Start em WebScraping

Vamos começar realizando uma primeira busca na web utilizando as bibliotecas urllib e beautifulsoup. O código abaixo entra no site, busca toda a página html e retorna o título principal.

```Python
from urlllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.didigalvao.com.br/")

bsObj = BeautifulSoup(html.read(), features="html.parser")

print(">>>>>> All content in h1.")
print(bsObj.body.h1)

print(">>>>>> Only the text into span tag.")
print(bsObj.body.h1.span.text)

``` 


## Conexão Confiável

Imagine uma spider que possui múltiplas funções: abrir uma página html, procurar por uma tag específica, interagir com a página, entre outras. Torna-se fundamental garantir que diante de qualquer problema nossa spider não vai simplesmente parar diante de qualquer erro. Imagine que a tag com a informação desejada mudou de uma página para outra, pronto isso já é suficiente para quebrar nossa spider. Temos que tratar este tipo de problema e garantir uma conexão confiável da nossa spdier. 

```Python
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://www.didigalvao.com.br/")
except URLError as e:
    print(e)
else:
    if html is None:
        print("HTML Page not found!")
    else:
        bsObj = BeautifulSoup(html.read(), features="html.parser")

        print(">>>>>> All content in h1.")
        print(bsObj.body.h1)

        print(">>>>>> Only the text into span tag.")
        print(bsObj.body.h1.span.text)
```

## Dominando buscas em HTML

Todo site em html é escrito utilizando recursos da própria linguagem de marcação. Em html algumas tags são do tipo: \<html\>, \<body\>, \<header\>, \<h1\>, \<h2\> até \<h5\>, \<span\>, \<strong\>, \<table\>, \<div\>, \<section\>, entre outras. Estas tags ainda podem ser classificadas para cada tipo de função ou informação que apresenta, geralmente essa classificação é realizada com atributos utilizados principalmente pela estilização via CSS. Alguns destes atributos são: class, id, name, entre outros. Desta forma, fica bem mais fácil para a spider navegar pela página e buscar a informação desejada com base nos letores identificados. Vejamos um exemplo utilizando alguns destes seletores:

```Python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# We scraping the web blog of a jornalist of the Cabrobó city.
# The Blog report of the onion price by week in the ceasa City.
# Get the title of the onion report in the fisrt page of cotation onion.
# We have 32 cotaion onion pages. Get the titles of the first page.
# This titles has the url to page with onion contation of the week

try:
    html = urlopen(
        "https://www.didigalvao.com.br/page/1/?s=cota%C3%A7%C3%A3o+cebola")
except HTTPError as e:
    print(e)
else:
    bs = BeautifulSoup(html.read(), "html.parser")
    name_list = bs.find_all('h3', {'class': 'entry-title td-module-title'})
    for name in name_list:
        print(name.get_text())
```

Com a função **find_all** é possível buscar atributos html ou css em documentos html. Esta função retorna todas as ocorreções conforme os atributos especificados. Por outro lado a função **find** encontra primeira ocorrência de um atributo. Existe diversas funções **find** na biblioteca BeautifulSoup. 

A função **get_text** busca o texto que está contido na tag html que foi encontrada.

### Alguns objetos BeautifulSoup

#### Árvores de navegação

Vamos descobrir como navegar para frente, para trás e diagonalmente em páginas html.

```Python
print(bs.find_all(div.h3.a))
```

Esta não é a melhor forma de trabalhar pois em qualquer modificação do site a spider deixa de funcionar.

#### Trabalhando com childrens

Se uma tag não está bem especificada, uma possibilidade é identificar a tag que ela está contida (pai) e assim buscar as informações da tag filho (children).

```Python
# In this spider we are studing about metods of library beautifulsoup

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# We still work with the bs4_methods.py problem.

# Work with the same search, now with the children method

try:
    html = urlopen(
        "https://www.didigalvao.com.br/page/1/?s=cota%C3%A7%C3%A3o+cebola")
except HTTPError as e:
    print(e)
else:
    bs = BeautifulSoup(html.read(), "html.parser")
    for child in bs.find('div', {'class': 'td-ss-main-content'}).children:
        print(child)
```

Algumas outras funções semelhantes são: **next_siblings()** deixa muito fácil a coleta de dados de tabelas. 

Também é possível trabalhar com tags pais a partir da tag filho. Para isto conheça a família de funções **parents**.

## Expressões regulares (Regex)

Expressões regulares são assim chamadas por que servem para encontrar strings regulares em textos. String regulares são nada mais que textos escritos por meio de regras lineares, como este que você lê. 

### Expressões Regulares e BeautifulSoup

```Python
# In this spider we are studing about metods of library beautifulsoup

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

# We still work with the bs4_methods.py problem.

# Work with the same search, now with the children method

try:
    html = urlopen(
        "https://www.didigalvao.com.br/page/2/?s=cota%C3%A7%C3%A3o+cebola")
except HTTPError as e:
    print(e)
else:
    bs = BeautifulSoup(html.read(), "html.parser")
    images = bs.find_all('img',
                         {'alt title':
                             re.compile('Cota+')})
    for image in images:
        print(image['alt title'])
```

## Web Crawlers

Web crawlers são rastreadores da internert, por diversas vezes precisamos navegar na internet em busca de informações que estão contidas em páginas dentro de outras páginas.

Vejamos em ação nosso primeiro Onion Crawler:

```Python
# This get the link pages that store cotation onion links

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

# Get the pages links

def get_page_url(url):

    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
    else:
        if html is None:
            print("Page empty!")
        else:
            bs = BeautifulSoup(html, "html.parser")
            current = bs.find('span', {'class': 'current'}).get_text()
            title = str(int(current) + 1)
            try:
                next_page = bs.find('a', {'title': title}).attrs['href']
            except AttributeError:
                next_page = ""
    return next_page

# Get url of the next page

if __name__ == '__main__':
    url = "https://www.didigalvao.com.br/page/1/?s=cota%C3%A7%C3%A3o+cebola"
    while url:
        print(url)
        url = get_page_url(url)
```

## Modelos de Web Crawling

Um erro comun quando se começar a desenvolver web crawlings é não modelar seu problema. E começar a definir escopos quando se está visitando as páginas de interesse. Se web crawlings possuem a natureza de buscar dados em diversas páginas, imagine o perigo de não modelar bem o seu problema. A cada visita em novos sites você vê uma gama de possíveis variáveis de interesse. Este número de variáveis só aumenta e cada vez mais seu crawler tem a chance de quebrar por apresentar cada vez mais complexidade.

Desta forma, é extremamente importante modelar o crawler antes mesmo de começar a desenvolvê-lo. Pense em quais dados são importantes para coletar, em quais páginas eles se encontram, como eles aparecem na página, qual o tipo de dado e como armazená-lo. Em alguns casos pode ser fácil armazenar os dados em um banco SQL, em outros pode ser mais viável amazenar no formato de texto, json ou armazenar em bancos NOSql. 

Em alguns casos podemos coletar informações cruciais sobre o produto:

- Nome;
- Preço;
- Id do produto
- Data

Em seguida podemos coletar outras informações que podemos classificar como do tipo atributo, estas não são obrigatórias:

- Nome do atributo
- Valor do atributo

Estes podem até mesmo serem armazenados em diferentes banco de dados. Desta forma fica muito mais fácil trabalhar com diferentes sites em busca de informações semelhantes.

## Scrapy

Scrapy é um framework python que permite o desenvolvimento de Web Crawlers de forma mais organizada e limpa, permitindo também uma manutenção e reaproveitamento de código mais intuitivo. Para instalar podemos utilizar o gerenciador de pacotes anaconda com o seguinte comando `conda install -c conda-forge scrapy`.

### Inicializando uma spider 

A partir de agora uma Spider é um projeto Scrapy que permite rastrear a web. Por outro lado Crawler significa qualquer programa genérico que rastreia a web, usando Scrapy ou não.

Para criarmos nossa primeira spider vamos executar a seguinte linha de comando (lembre de navegar até o dirétorio do projeto):

`$ scrapy startproject wikiSpider`

Este comando criará um novo diretório com o nome do projeto criado o qual possui por padrão 

Vá até a pasta spiders e crie um arquivo chamado `article.py`, em seguida vamos criar nossa primeira spider:

```Python
import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_requests(self):
        urls = [
            'http://en.wikipedia.org/wiki/Python_'
            '%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python']

        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_firs()
        print("URL is: {}".format(url))
        print("Title is: {}".format(title))
```

Para executar este código você pode utilizar o comando `scrapy crawl articles` dentro do dirétorio do projeto.