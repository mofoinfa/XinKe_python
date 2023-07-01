# 家庭群
# 对站长素材网站进行多线程获取
# 要求获取前5页的图片保存到文件中（图片分类自选）
# 网址：https://sc.chinaz.com/tupian/
# import requests
# from lxml import etree
# import threading
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
# }
#
#
# def get_img(url):
#     # print('http:'+url)
#     img = requests.get('http:' + url, headers=headers)
#     return img
#
#
# def get_data(url):
#     """
#     获取数据
#     :param url: 网页地址
#     :return:
#     """
#     html = requests.get(url, headers=headers)
#     html.encoding = 'utf-8'
#     # print(html.text)
#     html = etree.HTML(html.text)
#
#     img = html.xpath('//img/@data-original')
#     name = html.xpath('//img/@alt')
#     t1 = threading.Thread(target=deposit_img, args=(img, name,))
#     t1.start()
#
#
# def deposit_img(img, name):
#     """
#     存取图片
#     :param img:图片
#     :param name: 图片名称
#     :return:
#     """
#     for img, name in zip(img, name):
#         f = open(f'img\{name}.jpg', 'wb')
#         f.write(get_img(img).content)
#         f.close()
#         # print(img, name)
#
#
# if __name__ == '__main__':
#     get_data('https://sc.chinaz.com/tupian/')
#     for i in range(2, 6):
#         url = f'https://sc.chinaz.com/tupian/index_{i}.html'
#         get_data(url)

# 所学内容
# 一、多线程的作用
# 1.加快运行的速度
# 2.两个人不间断完成线程操作

# 二、多线程的引用
# 1.调用
# import threading
# 2.方法
# threading.Thread(target=函数名, args=(函数引用变量)).start
# 3.获取美食食节前五页的商品原材料(实战)
# https://www.meishij.net/zuofa/guangdongchangfen_6.html

# import re
# import requests
# import threading
# import time

# def get_data(url):
#     """获取页面获取数据"""
#     for i in url:
#         Ingredients = requests.get(i, headers=headers)
#         Ingredients = re.findall(
#             '<strong><a target="_blank" href="https://www.meishij.net/shicaizuofa/.*?/">(.*?)</a>(.*?)</strong>',
#             Ingredients.text)
#         print(Ingredients)
#
#
# def first_get():
#     for i in range(5):
#         url = f'https://www.meishij.net/xiaochi/guangdongxiaochi/p{i}'
#         jump_data = requests.get(url, headers)
#         url = re.findall('<a href="(.*?)" class="list_s2_item_img"', jump_data.text)
#         # 调用多线程
#         t1 = threading.Thread(target=get_data, args=(url,))
#         t1.start()
#         t1_list.append(t1)
#
#
#
# t2_list = []
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50'
# }
# t1_list = []
# t2 = threading.Thread(target=first_get)
# t2.start()
