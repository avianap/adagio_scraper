# -*- coding: utf-8 -*-
from lxml.etree import fromstring
  
# The requests library
import requests
  
class ReviewScraper:
  
    API_url = 'https://www.adagio.com/ajax/load_reviews_2017.html'

    def get_reviews(self):
     
        # This is the only data required by the api 
        # To send back the stores info
        data = {
        'reviewCounter': '0',
        'teaId': '001019',
        'reviewLoad': '6',
        }
        # Making the post request
        import pdb; pdb.set_trace()
        response = requests.post(self.API_url, data=data)

        # The data that we are looking is in the second
        # Element of the response and has the key 'data', 
        # so that is what's returned
        return response.json()[1]['data']

if __name__ == '__main__':
  scraper = ReviewScraper()
  scraper.get_reviews()



#from scrapy import Request
#from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LinkExtractor
#from adagio_scraper.items import Review
#
#class ReviewSpider(CrawlSpider):
#    name = 'review'
#    allowed_domains = ['https://www.adagio.com/']
#    start_urls = [
#        'https://www.adagio.com/black/irish_breakfast.html',
#        'https://www.adagio.com/black/golden_monkey.html',
#        ]
#
#    def start_requests(self):
#        for url in self.start_urls:
#            yield Request(url, self.parse, meta={
#                'splash': {
#                    'endpoint': 'render.html',
#                    'args': {'wait': 0.5}
#                }
#            })
#
#    def parse(self, response):
#        import pdb; pdb.set_trace()
#        response.xpath('//*[@id="reviewsDiv"]').getall() 
#
#        #item = Review()
#        #item['sku'] = response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div[@itemscope]/meta[@itemprop="productID"]/@content').get()
#        #price_info = response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div[1]/div[@class="cart"]/div[@id="pricesDiv"]/div[@class="itemBlock autoDeliverable1 "]').getall()
#        #review_block = response.xpath('//div[@id="mainContainer"]/div[@id="stage"]/div/div/div[@class="review_block"]').get()
#       
