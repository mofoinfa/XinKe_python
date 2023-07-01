import re

import scrapy
from ..items import ToscrapeItem


class GoodwordSpider(scrapy.Spider):
    name = "goodWord"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        # 数据解析
        contant = re.findall('itemprop="text">“(.*?)”</span>', response.text)
        author = re.findall('itemprop="author">(.*?)</small>', response.text)
        item = ToscrapeItem()
        for contant, author in zip(contant, author):
            item['contant'] = contant
            item['author'] = author
            yield item
