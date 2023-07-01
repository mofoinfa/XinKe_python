# 获取链接网前5页的数据 爬取标题 爬*-* 位置 总价格和单价
# 保存到text文件里面 一条数据存一行
# 作业提交保存数据的截图

import requests
from lxml import etree

# 抓取数据
f = open('房子数据.txt', 'a+', encoding='utf-8')
for i in range(1, 6):
    url = f'https://cs.lianjia.com/ershoufang/pg{i}/'
    head_data = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    }

    html = requests.get(url, headers=head_data)
    html = etree.HTML(html.text)
    title = html.xpath('//div[@class="title"]/a/text()')  # 标题
    pos = html.xpath('//div[@class="positionInfo"]/a/text()')  # 位置
    total_Prices = html.xpath('//div[@class="totalPrice totalPrice2"]/span/text()')  # 总价
    unit_Price = html.xpath('//div[@class="unitPrice"]/span/text()')  # 单价
    for i in range(len(unit_Price)):
        f.write(f'标题：{title[i]}\t')
        f.write(f'位置：{pos[2 * i]}-{pos[2 * i + 1]}\t')
        f.write(f'总价格：{total_Prices[i]}万\t')
        f.write(f'单价:{unit_Price[i]}\n')
f.close()

# 所学内容
# 一、xpath的安装与应用
# 1.安装
# pip install lxml#安装
# from lxml import etree#调用
#
# 2.调用
# html=etree.HTML(html)#把文本数据转化为可解析的树形文档
#
# 二、xpath的使用
# 1.从根节点触发，绝对路径(/)
# html.xpath('/html/head')#从最初的根目录找，层层递进
# 2.从相对节点出发(//)
# html.xpath('//head/div')#直接转到head下的div
# 3.选取属性(@)
# html.xpath('//head/div/@class')#在head下的div内选取属性class内的内容
# 4.同时满足多个属性(|)
# html.xpath('//head/div/@class|//head/div/@id')#同时获取两个属性
# 5.将得到的内容只截取出文本数据(text())
# html.xpath('//head/div/text()')
# 6.同时获取多个数据后，选取需要调用的是哪个（谓语）([])
# html.xpath('//head/link[2]')
# 7.按照需求获取某一部分数据([postion>x])
# html.xpath('//head/link[position>5]')#获取10条数据中的后4条数据
# 8.获取出现过此属性的值([@x])
# html.xpath('//head/link[@class])')#获取link中有class属性的值
# 9.获取属性等于某个确切值对应的内容([@x=y])
# html.xpath('//head/link[@class=abc])')
# 10.表示代表所有数据
# html.xpath('//*[@rel]')# 获取元素里面有rel属性的元素 不会受到标签的限制
# html.xpath('//*')#获取所有数据
# 11.简易获取方法
# 在网页内对所需要的数据复制其Xpath
#
# 三、解决数据乱码
# html.encoding = 'utf-8'#将乱码转化为中文格式
