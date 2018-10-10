import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        yield {
            'title':'helloo',
            'votes': 'worldd',
            
        }
