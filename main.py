import scrapy
from scrapy.crawler import CrawlerProcess
from adagio_scraper.spiders import review

process = CrawlerProcess()
process.crawl(review)
process.start()


