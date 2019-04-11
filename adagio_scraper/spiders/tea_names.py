# -*- coding: utf-8 -*-
#import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from adagio_scraper.items import AdagioScraperItem 

class TeaNamesSpider(CrawlSpider):
    name = 'tea_names'
    allowed_domains = ['https://www.adagio.com/']
    start_urls = [
        'https://www.adagio.com/black/',
        'https://www.adagio.com/oolong/',
        'https://www.adagio.com/green/',
        ]

    def parse(self, response):
        item = AdagioScraperItem()
        item['names'] = response.xpath('//div[@class="productIndex"]/div[5]/h6[@class="regular"]/text()').getall()
        item['ratings'] = response.xpath('//div[@class="productIndex"]/div[5]/div[@class="stars"]/text()').getall()
        item['price_per_cup'] = response.xpath('//div[@class="productIndex"]/div[5]/div[@class="pricePer"]/text()').getall()
        item['project'] = self.settings.get('BOT_NAME')
        item['spider'] = self.name
        item['tea_type'] = response.xpath('//*[@id="accountNav"]/div/a[@class="selected"]/text()').getall()

        return item
        
