# 家庭作业
# http://quotes.toscrape.com/ 获取网站的 名言和人名称
# 网站使用不了可以使用上课的网站练习
# 存储数据不限


# 所学内容
# 一、scrapy的安装
# 1.pip install --upgrade pip
# 2.pip install Scrapy
#
# 二、创建scrapy的框架
# cd 到该项目的文件
# 终端：scrapy startproject 框架名字
#
# 三、终端常用的定位方式
# cd 路径     如何进入到指定的路径
# D:          进入D盘
# cd 路径     cd 文件夹/文件夹/文件夹
# cd ../     返回上一级
#
# 四、创建爬虫文件
# cd 到spiders文件下创建创建爬虫文件
# scrapy genspider 爬虫的名称 爬虫网站
#
# 五、在setting中需要更改的数据
# 1.添加头文件
# 在DEFAULT_REQUEST_HEADERS内添加头文件
# 2.开启保存通道
# ITEM_PIPELINES
# 提示：里面的数值越小，优先值越高
# 3.开启爬虫
# ROBOTSTXT_OBEY改为False
#
# 六、item文件的作用
# 将数据类型更改为item的类型
#
# 七、pipelines的作用
# 保存至各个位置
#
# 八、运行项目
# import os
# os.system('scrapy crawl movie_douban')
