import re

import requests
import scrapy
from ..items import ZzscItem
from scrapy_redis.spiders import RedisSpider


class ImageSpider(RedisSpider):
    name = "image"
    # allowed_domains = ["sc.chinaz.com"]
    # start_urls = ["https://sc.chinaz.com/tupian/index.html"]

    redis_key = 'Zzsc:start_urls'

    def parse(self, response, *_):
        # 循环网页
        # print(response.text)
        url = re.findall('2883</b></a><a href="(.*?)"', response.text)[0]
        # print(url)
        if str(url) == 'index_21.html':
            pass
        else:
            url = 'https://sc.chinaz.com/tupian/' + str(url)
            print(url)
            yield scrapy.Request(url, callback=self.parse)
        # 返回图片地址
        item = ZzscItem()
        image_urls = ['https:' + str(i).replace('_s', '') for i in
                      response.xpath('//div[@class="item"]/img/@data-original').extract()]
        item['image_urls'] = image_urls
        yield item
