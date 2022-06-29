import scrapy
import pandas as pd

class PokemonSpider(scrapy.Spider):
    name = 'pokemon'
    allowed_domains = ['pokeapi.co']

    df = pd.read_csv('pokemons_list.csv')
    start_urls = df['pokemon_api_url'].tolist()

    def parse(self, response):
        response = response.json()

        yield {
            'id': response['id'],
            'name': response['name'],
            'order': response['order'],
            'base_experience': response['base_experience'],
            'sprite': response['sprites']['front_default'],
            'hp': response['stats'][0]['base_stat'],
            'attack': response['stats'][1]['base_stat'],
            'defense': response['stats'][2]['base_stat'],
            'speed': response['stats'][5]['base_stat'],
            'height': response['height'],
            'weight': response['weight']
        }
