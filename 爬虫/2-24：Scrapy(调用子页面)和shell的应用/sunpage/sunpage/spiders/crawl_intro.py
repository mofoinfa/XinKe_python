import re

import scrapy
from ..items import SunpageItem


class CrawlIntroSpider(scrapy.Spider):
    name = "crawl_intro"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/chart"]
    def parse(self, response):
        # print(response.text)
        sunpage_url = response.xpath('//a[@class="nbg"]/@href').extract()
        title = re.findall('<a href=".*?"  class="">(.*?)\/', response.text, re.S)
        author = response.xpath('//div[@class="pl2"]/a/span/text()').extract()
        for sunpage_url, title, author in zip(sunpage_url, title, author):
            item = SunpageItem()
            title = str(title).strip()
            item['title'] = title
            item['author'] = author
            yield scrapy.Request(sunpage_url, meta={'item': item}, callback=self.sun_parse)  # 调用子页面

    def sun_parse(self, response):
        item = response.meta['item']
        contant = response.xpath('//span[@property="v:summary"]/text()').extract()[0]
        contant = str(contant).strip().replace('\\n', '').replace('\\u3000', '')
        item['contant'] = contant
        yield item
