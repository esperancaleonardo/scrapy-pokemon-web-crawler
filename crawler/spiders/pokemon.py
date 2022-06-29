import scrapy


class PokemonSpider(scrapy.Spider):
    name = 'pokemon'
    allowed_domains = ['pokeapi.co']
    start_urls = ['http://pokeapi.co/api/v2/pokemon/ditto', 'http://pokeapi.co/api/v2/pokemon/pikachu']

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
