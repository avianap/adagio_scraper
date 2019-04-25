# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AdagioScraperItem(scrapy.Item):
    names = scrapy.Field()
    price_per_cup = scrapy.Field()
    ratings = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    tea_type = scrapy.Field()

class Tea(scrapy.Item):
    name = scrapy.Field()
    sku = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
    review_count = scrapy.Field()
    price_16oz = scrapy.Field()
    price_2oz = scrapy.Field()
    description = scrapy.Field()
    steeping_info = scrapy.Field()
    price_per_cup = scrapy.Field()
    tea_type = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()

class Review(scrapy.Item):
    name = scrapy.Field()
    sku = scrapy.Field()
    rating = scrapy.Field()
    review = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
