import re
import requests

import scrapy
from ..items import JdMsgItem


class JdCrawlSpider(scrapy.Spider):
    name = "Jd_crawl"
    allowed_domains = ["www.jd.com"]
    start_urls = ["http://www.jd.com/allSort.aspx"]

    def parse(self, response):
        big_title = response.xpath('//html/body/div[5]/div[2]/div[1]/div[1]/div/a/text()').extract()
        mid_title = response.xpath('//div/dl/dt/a/text()').extract()
        min_title = response.xpath('//div/dl[@class="clearfix"]/dd/a/text()').extract()
        name = response.xpath('//div[@class="item-hot clearfix"]/a/@title').extract()
        url = response.xpath('//div[@class="item-hot clearfix"]/a/@href').extract()
        item = JdMsgItem()
        item['big_title'] = big_title
        item['mid_title'] = mid_title
        item['min_title'] = min_title
        item['name'] = name
        item['url'] = url
        yield scrapy.Request("http://www.jd.com/allSort.aspx",meta={'item': item}, callback=self.sun_parse)  # 调用子页面

    def sun_parse(self, response):
        """因为数据个数不统一，所以将数据进行统一查询"""
        item = response.meta['item']
        price = []
        # print(item['url'])
        for i in item['url']:
            id = re.findall('//item.jd.com/(.*?).html', i)
            url = 'https://api.m.jd.com/api?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&t=1680061888220&client=pc&clientVersion=1.0.0&loginType=3&body={"skuId": "%s","cat": "1713,3265,3428","area": "25_2235_27497_28901","shopId": "1000004363","venderId": 1000004363,"paramJson": {"platform2":"100000000001","specialAttrStr":"p0ppppppppppp1ppp1ppppppppp","skuMarkStr":"00"},"num": 1}&uuid=122270672.564351460.1659410514.1680011309.1680061666.8&jsonp=jQuery1226430&_=1680061888221' % int(
                id[0])
            headers = {
                'authority': 'api.m.jd.com',
                'accept': '*/*',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'referer': 'https://item.jd.com/',
                'sec-ch-ua': '\\',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '\\',
                'sec-fetch-dest': 'script',
                'sec-fetch-mode': 'no-cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54',
            }
            response = requests.get(url, headers=headers)
            try:
                price.append(re.findall('"op":"(.*?)"', response.text)[0])
            except:
                price.append('')
        item['price'] = price
        yield item