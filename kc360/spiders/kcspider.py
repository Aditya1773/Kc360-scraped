import scrapy
from ..items import Kc360Item


class Kc360Spider(scrapy.Spider):
    name = 'kcspider'

    start_urls = ['https://kc360.in/menu']

    def parse(self, response):
        items = Kc360Item()
        
        food_name = response.css('div.menu-item-name::text ').extract()
        food_price = response.css('.menu-item-price::text').extract()
        items['food_name'] = food_name
        items['food_price'] = food_price
        yield items
        pass




