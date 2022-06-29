import scrapy


class PokemonSpider(scrapy.Spider):
    name = 'pokemon'
    allowed_domains = ['pokeapi.co']
    start_urls = ['http://pokeapi.co/']

    def parse(self, response):
        pass
