# scrapy-pokemon-web-crawler

Pokemon [pokeapi](https://pokeapi.co/) scrapy demo project using spiders and simple yelds to save data in **.csv** files

<br>

---
## Motivation

Demonstrate how to fetch and crawl data from APIs REST using python. This Repository contains spiders that fetch and crawl data from REST APIs JSON responses and saves it to .csv files with headers.

<br>

---
## How to

clone this repository
```bash
git clone https://github.com/esperancaleonardo/scrapy-pokemon-web-crawler.git
```

create a python virtual env inside the repo, aside `/crawler` folder
```bash
cd scrapy-pokemon-web-crawler
python3 -m venv .venv 
```

activate the virtual env and install project requirements.txt
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

on root folder of the project `/scrapy-web-crawler`, first run the **list pokemons** spider, using **-o** flag to create a **.csv** file to output and save data

```bash
scrapy crawl list_pokemons -L INFO -o pokemons_list.csv
```

it will create a **.csv** with the structure (columns) below:

| pokemon_id | pokemon_name | pokemon_api_url                      |
| -----------| ------------ | ------------------------------------ |
| 1          | bulbasaur    | https://pokeapi.co/api/v2/pokemon/1/ |
| ...        | ...          | ...                                  |


then, on the same folder, run the **pokemon** spider to crawl pokemon info of all pokemons in the crawled **.csv** file

```bash
scrapy crawl pokemon -L INFO -o pokemons_info.csv
```

it will create a **.csv** with the structure (columns) below:

| id | name      | order | base_exp | sprite   | hp | attack | defense | speed | height | weight |
|----|-----------|-------|----------|----------|----|--------|---------|-------|--------|--------|
| 1  | bulbasaur | 1     | 64       | <sprite> | 45 | 49     | 49      | 45    | 7      | 69     |


<br>

---
## Create new spiders to fetch other routes

generate the spider inside this repo folder
```bash
scrapy genspider <spidername> <domaintocrawl>
```

it will create a **.py** file with the spider given name and a spider template inside `/spiders` folder

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

## Stack in project

**Python version:** 3.10.5

**Libraries:** pandas@1.4.3, scrapy@2.6.1



## Author

- [@esperancaleonardo](https://www.github.com/esperancaleonardo)

## References

 - [Scrapy](https://scrapy.org/) - [Docs](https://docs.scrapy.org/en/latest/)
 - [Pandas](https://pandas.pydata.org/) - [Docs](https://pandas.pydata.org/docs/)
