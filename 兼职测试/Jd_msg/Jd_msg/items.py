# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdMsgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    big_title = scrapy.Field()
    mid_title = scrapy.Field()
    min_title = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    price=scrapy.Field()
    pass
