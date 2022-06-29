# scrapy-pokemon-web-crawler

Pokemon pokeapi scrapy demo project using spiders and simple yelds to save data in .csv files

## Motivation

Demonstrate how to fetch and crawl data from APIs REST using python. This Repository contains spiders that fetch and crawl data from REST APIs JSON responses and saves it to .csv files with headers.
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

| id | name      | order | base_exp | sprite       | hp | attack | defense | speed | height | weight |
|----|-----------|-------|----------|--------------|----|--------|---------|-------|--------|--------|
| 1  | bulbasaur | 1     | 64       | <sprite_url> | 45 | 49     | 49      | 45    | 7      | 69     |

