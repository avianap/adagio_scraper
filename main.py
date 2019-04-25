import scrapy
from scrapy.crawler import CrawlerProcess
from adagio_scraper.spiders import tea
from adagio_scraper.spiders import review

process = CrawlerProcess()
process.crawl(tea.TeaSpider)
process.start()

#scraper = review.ReviewScraper(sku = '001019')
#x = scraper.get_reviews()
#import pdb; pdb.set_trace()






