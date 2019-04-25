# -*- coding: utf-8 -*-
#import scrapy
from scrapy import FormRequest
from scrapy.spiders import CrawlSpider, Rule
from adagio_scraper.items import Tea
from adagio_scraper.spiders import review
from bs4 import BeautifulSoup

class TeaSpider(CrawlSpider):
    name = 'tea'
    allowed_domains = ['https://www.adagio.com/']
    start_urls = [
        'https://www.adagio.com/black/irish_breakfast.html',
        'https://www.adagio.com/black/golden_monkey.html',
        ]

    def parse(self, response):
        item = Tea()
        item['name'] = response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div[1]/div[@class="cart"]/div[@class="summary"]/h1/text()').get().strip()
        item['sku'] = response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div[@itemscope]/meta[@itemprop="productID"]/@content').get()
        item['rating'] = int(response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div[1]/div[@class="cart"]/div[@class="summary"]/div[@itemprop="aggregateRating"]/div[@class="scoreSummary"]/text()').get().strip()) 
        item['rating_count'] = int(response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div[1]/div[@class="cart"]/div[@class="summary"]/div[@itemprop="aggregateRating"]/meta[@itemprop="ratingCount"]/@content').get())
        item['review_count'] = int(response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div[1]/div[@class="cart"]/div[@class="summary"]/div[@itemprop="aggregateRating"]/meta[@itemprop="reviewCount"]/@content').get())
        price_info = response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div[1]/div[@class="cart"]/div[@id="pricesDiv"]/div[@class="itemBlock autoDeliverable1 "]').getall()
        for price_block in price_info:
            parsed_block = BeautifulSoup(price_block)
            oz = parsed_block.find('div', {'class':'size'}).text.strip()
            try:
                item['price_'+oz] = int(parsed_block.find('div', {'class':'price'}).text.strip().replace('$',''))
            except:
                pass
        item['description'] = response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div[1]/div/div[@class="description"]/div[@itemprop="description"]/text()').get()
        item['steeping_info'] = response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div[1]/div/div[@class="description"]/div[@class="steepingInfo"]/text()').get()

        item['project'] = self.settings.get('BOT_NAME')
        item['spider'] = self.name
        item['tea_type'] = 'black'

        rs = review.ReviewScraper(sku = item['sku'], review_count = item['rating_count'])
        rs.get_reviews()

        return item



