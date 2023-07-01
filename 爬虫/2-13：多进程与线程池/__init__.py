# 家庭作业
# 对站长素材网站进行多线程获取
# 要求获取前5页的图片保存到文件中（图片分类自选）
# 站长素材（https://sc.chinaz.com/tupian/） 使用线程池获取
# import requests
# import re
# from concurrent.futures import ThreadPoolExecutor
#
#
# def get_img(url):
#     """
#     获取图片
#     :param url:
#     :return:
#     """
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
#     }
#     img = requests.get(url, headers=headers)
#     img = re.findall('data-original="(.*?)"', img.text)
#     for i in img:
#         save_img(i[-22:], 'https:' + i)
#
#
# def save_img(name, img):
#     f = open(f'img/{name}', 'wb')
#     img = requests.get(img)
#     f.write(img.content)
#     f.close()
#
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(10)
#     url_list = ['https://sc.chinaz.com/tupian/']
#     for i in range(2, 6):
#         url_list.append(f'https://sc.chinaz.com/tupian/index_{i}.html')
#     for i in url_list:
#         pool.submit(get_img, i)


# 所学内容
# 一、多进程
# 1.多进程的概述
# 同时执行多个进程，加快执行速度
#
# 2.多进程的调用
# import multiprocessing#全部调用
# from multiprocessing import Process#一般调用
#
# 3.使用方法
# p1=multiprocessing.Process(target=函数名,args=(变量，变量))
# p1.start()
# Process(target=函数名,args=(变量，变量)).start()
# 注意：只能在（if __name__ == '__main__':）里面调用，因为其会重新创建一个进程

# 4.实战：同时执行两个输入语句
# from multiprocessing import Process
#
#
# def input_addition(num):
#     num = [int(i) for i in num]
#     print(sum(num))
#
#
# def input_subtraction(num):
#     num = [int(i) for i in num]
#     minuend = num[0]
#     for i in range(1, len(num)):
#         minuend -= num[i]
#     print(minuend)
#
#
# if __name__ == '__main__':
#     num = input('请输入运算的数字（空格隔开）:').split()
#     Process(target=input_subtraction, args=(num,)).start()
#     Process(target=input_addition, args=(num,)).start()

# 二、线程池
# 1.引入
# from concurrent.futures import ThreadPoolExecutor
# pool=ThreadPoolExecutor(10)#表示有执行几个线程
# 2.方法
# pool.submit(函数名，参数，参数)
# pool.shutdown()结束线程
# 3.实战（获取北京新发地前50页的菜品数据（http://www.xinfadi.com.cn/priceDetail.html））
# import requests
# import time
# from concurrent.futures import ThreadPoolExecutor
#
#
# def get_data(data):
#     data = requests.post(url, headers=headers, data=data)
#     for dish_information in data.json()['list']:
#         print(dish_information)
#
#
# start = time.time()
# pool = ThreadPoolExecutor(20)  # 开启20个线程
# url = 'http://www.xinfadi.com.cn/getPriceData.html'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
# }
# for i in range(1, 51):
#     data = {
#         'limit': '20',
#         'current': i
#     }
#     pool.submit(get_data, data)
# pool.shutdown()  # 线程暂停
# end = time.time()
# print(end - start)
# 可得没用线程池所用时间40s，用了则为6s
