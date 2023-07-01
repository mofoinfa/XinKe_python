# 家庭作业
# 获取豆瓣网页 https://movie.douban.com/subject/4811774/?from=showing的数据

import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/subject/4811774/?from=showing'
header = {
    'Cookie': 'll="118166"; bid=7HIgR0SCcPw; __gads=ID=c0f4f8563f5221a6-2217513cfbd10033:T=1650120086:RT=1650120086:S=ALNI_MaOo1a45bu0yCRoq8f1bgX767JCqw; _vwo_uuid_v2=D9638DA2ED60552B05E5AE1AF41709BBB|ec9226ecd622a64ff53876f6f34b9e5f; douban-fav-remind=1; __yadk_uid=O780RiBh91M08yhaSqAQRIQfGizulckb; __utmz=223695111.1672835977.4.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=30149280.1673713519.8.6.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=["","",1674973799,"https://cn.bing.com/"]; _pk_id.100001.4cf6=50ac70b51d3c100e.1650120086.6.1674973799.1672841395.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1423037999.1650120086.1673713519.1674973799.9; __utmb=30149280.0.10.1674973799; __utmc=30149280; __utma=223695111.1274966811.1650120086.1672841395.1674973799.6; __utmb=223695111.0.10.1674973799; __utmc=223695111; __gpi=UID=000009d140877d02:T=1663681583:RT=1674973801:S=ALNI_MZDh_6Q4Wn4Sn9806ayqTGraX5mAQ',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'
}
html = requests.get(url, headers=header)
data = BeautifulSoup(html.content, 'lxml')
title = data.find_all('span', property="v:itemreviewed")
title = [i.text for i in title]
print(f'标题:{title}')
film_data = data.find_all('div', id="info")
for i in film_data:
    print(i.text)

# 所学内容
# 一、bs4模块的安装与调用
# 1.安装
# pip install BeautifulSoup4
# 2.调用
# from bs4 import BeautifulSoup
#
# 二、bs4模块的使用
# 1.转化为树形数据
# html=requests.get(url,headers=header)
# data=BeautifulSoup(html,'lxml')
# 2.获取第一个标签
# print(data.link)
# 3.获取文本数据
# print(data.link.text)
# 4.获取标签对象的所有属性
# print(data.link.attrs)
# 5.获取标签的第一个属性
# print(data.title.get('class'))
# 6.获取满足条件的第一个数据（data.find('标签名'，'属性')）
# print(data.find('div',class_='123'))#记：class因为为关键字所以需要在最后加下划线
# 7.获取多个数据(data.find_all('标签名'，'属性'))
# （1）获取数据
# data=data.find_all('div',_class='abc')#得到的为一个可迭代对象
# （2）循环输出文本数据
# for i in data:
#     print(i.text)#输出数据
# （3）循环得到文本数据列表
# data=[i.text for i in data]
#
# 三、美化输出
# print(data.prettify())