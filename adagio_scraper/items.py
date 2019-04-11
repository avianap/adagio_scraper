# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AdagioScraperItem(scrapy.Item):
    # define the fields for your item here like:
    names = scrapy.Field()
    price_per_cup = scrapy.Field()
    ratings = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    tea_type = scrapy.Field()
