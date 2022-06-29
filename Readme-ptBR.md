# scrapy-pokemon-web-crawler

[English Version](./Readme.md)

Projeto demonstrativo com scrapy, utilizando spiders para raspar dados da api Pokemon [pokeapi](https://pokeapi.co/) e salvar em arquivos **.csv**

<br>

---
## Motivação

Demonstrar e exemplificar como raspar dados de APIs RESTful com python.

<br>

---
## Como fazer você mesmo

clone o repositório do projeto
```bash
git clone https://github.com/esperancaleonardo/scrapy-pokemon-web-crawler.git
```

crie um virtualenv do python dentro do repositório, ao lado da pasta `/crawler`
```bash
cd scrapy-pokemon-web-crawler
python3 -m venv .venv 
```

ative o ambiente virtual e instale as dependências do projeto
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

ainda na pasta raiz, execute a primeira spider do projeto com o comando abaixo, passando a flag **-o** para salvar os dados em um **.csv**
```bash
scrapy crawl list_pokemons -L INFO -o pokemons_list.csv
```

será criado um arquivo **.csv** com a estrutura abaixo:

| pokemon_id | pokemon_name | pokemon_api_url                      |
| -----------| ------------ | ------------------------------------ |
| 1          | bulbasaur    | https://pokeapi.co/api/v2/pokemon/1/ |
| ...        | ...          | ...                                  |


então, ainda na mesma pasta, execute a segunda spider para raspar dados dos pokemons raspados na primeira etapa
```bash
scrapy crawl pokemon -L INFO -o pokemons_info.csv
```

será criado um arquivo **.csv** com a estrutura abaixo:

| id | name      | order | base_exp | sprite   | hp | attack | defense | speed | height | weight |
|----|-----------|-------|----------|----------|----|--------|---------|-------|--------|--------|
| 1  | bulbasaur | 1     | 64       | <sprite> | 45 | 49     | 49      | 45    | 7      | 69     |


<br>

---
## Raspando outras rotas da API

inicialize uma nova spider com o comando abaixo, dentro da raiz do projeto:
```bash
scrapy genspider <spidername> <domaintocrawl>
```

será criado um arquivo **.py** com o nome dado à spider e com o template dentro da pasta `/spiders`:
```python
import scrapy

# generated with  'scrapy genspider myspider exemple.com'
class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['exemple.com']
    start_urls = ['http://exemple.com/']

    def parse(self, response):
        pass

```

## Stack utilizada

**Python:** 3.10.5

**Bibliottecas:** pandas@1.4.3, scrapy@2.6.1



## Autor

- [@esperancaleonardo](https://www.github.com/esperancaleonardo)

## Referências

 - [Scrapy](https://scrapy.org/) - [Documentação](https://docs.scrapy.org/en/latest/)
 - [Pandas](https://pandas.pydata.org/) - [Documentação](https://pandas.pydata.org/docs/)
