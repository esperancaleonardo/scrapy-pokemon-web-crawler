import scrapy


class ListPokemonsSpider(scrapy.Spider):
    name = 'list_pokemons'
    allowed_domains = ['pokeapi.co']
    start_urls = ['https://pokeapi.co/api/v2/pokemon/']

    def parse(self, response):
        response = response.json()

        for pokemon in response['results']:
            yield {
                'pokemon_id': pokemon['url'].split('/')[-2],
                'pokemon_name': pokemon['name'],
                'pokemon_api_url': pokemon['url']
            }

        if response['next']:
            yield scrapy.Request(response['next'], callback=self.parse)
