# 家庭作业
# 用scrpay爬取豆瓣电影的前10页
# https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action
# 所学内容
# 一、负载json数据请求
# 1.使用情况，当载荷数据是json数据时，使用该调用方法
# 2.实战：爬取次元岛的主页图片（http://ciyuandao.com/coser/28624）

# import requests
#
# url = 'http://ciyuandao.com/api/works/works/getuserphotoworks'
#
# cookies = {
#     'Hm_lvt_a725808a2c5b68407266e3dc120ad8ea': '1677420850,1677923808',
#     '.ciyuandao.pass.antiforgery': 'CfDJ8NXGAZ7ga0ZHs10PANj6fDx7eev0QHkz2YXtk3UHlFmU5YkUMzVFkwG_-xOXZHVtk-F_dOokM3W3a2xw7PO9GzH86wXvdXYU3P9T2bdW4aRFfEFZy8wTrBJDsf2kJL-pXinhDbGTZSBfO5SW3RQZHTQ',
#     'Hm_lpvt_a725808a2c5b68407266e3dc120ad8ea': '1677926721',
# }
#
# headers = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/json',
#     'Origin': 'http://ciyuandao.com',
#     'Pragma': 'no-cache',
#     'Referer': 'http://ciyuandao.com/coser/28624',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
#     'X-Requested-With': 'XMLHttpRequest',
#     'x-csrf-token': 'CfDJ8NXGAZ7ga0ZHs10PANj6fDzMiSS_niEmtiXplg0xnHYkuTlW2JQXGy_6QalOD-GpUsYt4jdX1fIRh1JzvDSQM_7OCvC3xRJkZSE8TIVmWZhQ4Bjj1q_-cpAeoS3sUIwxZidS5wnKJJUaJOzg4c2iDFE',
# }
#
# data = {
#     'isReadCount': 'true',
#     'limit': '6',
#     'page': '1',
#     'userId': "28624"
# }
# data = requests.post(url, headers=headers, json=data, cookies=cookies)  # 利用json类型获取
# image = ['http://img.ciyuandao.com/' + i['faceSrc'] for i in data.json()['data']]
# for i in image:
#     name = i[-10:]
#     img = requests.get(i)
#     open(f'千岛图_img/{name}', 'wb').write(img.content)
# print(image)

# 二、scrapy shell的作用
# 终端操作：
# 1.启动
# scrapy shell
# 2.启动爬取的页面
# fetch('https://movie.douban.com/top250?start=0&filter=')
# 3.启动本地页面
# view(response)
# 4.利用xpath输出数据
# response.xpath('xpath代码').extract()

# 三、scrapy调用post数据
# 1.post请求代码
# def start_requests(self):
#     data={}
#     HEADERS={}
#     for url in self.start_urls:
#         yield scrapy.FormRequest(url=url, formdata=data, headers=HEADERS, callback=self.parse)
#
# 2.参考网站
# #https://blog.csdn.net/weixin_38819889/article/details/109106942

# 四、调用子页面
# 1.实战：获取豆瓣电影的简介（https://movie.douban.com/chart）
# 详见：文章sunpage
# 说明：
# <1>调用子页面
# 位置：sunpage/sunpage/spiders/crawl_intro.py
# 写法：yield scrapy.Request('地址',callback='返回的函数',meta='传递的参数（字典格式传递）')
# <2>子页面接收返回的数据
# item=response.meta['字典里的命名']

