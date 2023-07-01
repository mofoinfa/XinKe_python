# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    actor_count = scrapy.Field()
    actors = scrapy.Field()
    cover_url = scrapy.Field()
    id = scrapy.Field()
    is_playable = scrapy.Field()
    is_watched = scrapy.Field()
    rank = scrapy.Field()
    rating = scrapy.Field()
    regions = scrapy.Field()
    release_date = scrapy.Field()
    score = scrapy.Field()
    title = scrapy.Field()
    types = scrapy.Field()
    url = scrapy.Field()
    vote_count = scrapy.Field()
