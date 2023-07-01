import re

import scrapy
from ..items import ZzscItem


class ZzImgSpider(scrapy.Spider):
    name = "zz_img"
    allowed_domains = ["sc.chinaz.com"]
    start_urls = [f"https://sc.chinaz.com/tupian/index_{i}.html" for i in range(2, 21)]
    start_urls.append('https://sc.chinaz.com/tupian/index.html')

    def parse(self, response):
        item = ZzscItem()
        img_url = re.findall('data-original="(.*?)"', response.text)
        img_urls = []
        for i in img_url:
            i = str(i).replace('_s', '')
            img_urls.append('https:' + i)
        item['image_urls'] = img_urls
        print(item)
        yield item
