# 家庭作业
# 把上节课的存储方式从mysql改成mongo存储
# import requests
# import re
# import pymongo
#
# cli = pymongo.MongoClient()  # 连接数据库
# db = cli.movie_data
# col = db.movie_data
# def collate_message(old_message):
#     """
#     修整其他信息内容
#     :param old_message:旧的信息
#     :return: 新的信息
#     """
#     for i in old_message:
#         i = list(i)
#         if '<br>' in i:
#             i[1] = '主演:无'
#         if i[0].find('&') != -1:
#             i[0] = i[0][0:i[0].find('&')] + i[0][i[0].find('.'):]
#     return i
#
#
# def collate_title(old_title):
#     """
#
#     :param old_title: 旧标题
#     :return:整理后的新标题
#     """
#     new_title = ''
#     for i in old_title:
#         new_title += i + '/'
#     new_title = new_title.replace(' ', '')
#     return new_title[:-1]
#
#
# def get_data():
#     """
#     获取网页数据
#     :return: 获取的网页数据
#     """
#     url = 'https://movie.douban.com/top250'
#     for i in range(0, 250, 25):
#         headers = {
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
#             'Cookie': 'll="118166"; bid=7HIgR0SCcPw; __gads=ID=c0f4f8563f5221a6-2217513cfbd10033:T=1650120086:RT=1650120086:S=ALNI_MaOo1a45bu0yCRoq8f1bgX767JCqw; _vwo_uuid_v2=D9638DA2ED60552B05E5AE1AF41709BBB|ec9226ecd622a64ff53876f6f34b9e5f; douban-fav-remind=1; __yadk_uid=O780RiBh91M08yhaSqAQRIQfGizulckb; __utmz=30149280.1673713519.8.6.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; __utmc=30149280; __utmc=223695111; __gpi=UID=000009d140877d02:T=1663681583:RT=1675437579:S=ALNI_MZDh_6Q4Wn4Sn9806ayqTGraX5mAQ; __utma=30149280.1423037999.1650120086.1675437578.1675443260.12; __utmt=1; __utmb=30149280.1.10.1675443260; dbcl2="267349846:pP7mVhjUD/w"; ck=5ham; _pk_ref.100001.4cf6=["","",1675443319,"https://accounts.douban.com/"]; _pk_ses.100001.4cf6=*; __utma=223695111.1274966811.1650120086.1675437578.1675443319.9; __utmb=223695111.0.10.1675443319; __utmz=223695111.1675443319.9.4.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=50ac70b51d3c100e.1650120086.9.1675443542.1675438600.'
#         }
#         params = {
#             'start': i
#         }
#         movie_data = requests.get(url, headers=headers, params=params)
#         dataAnalysis(movie_data)
#
#
# def dataAnalysis(movie_data):
#     """
#     将得到的数据进行分类
#     :param movie_data:电影的初始数据
#     :return:
#     """
#     eve_movie = re.findall('<div class="info">(.*?)</li>', movie_data.text, re.S)  # 获取每一个电影的块级
#     x = 0
#     for i in eve_movie:
#         # 获取标题
#         if re.findall('class="title">(.*?)</span>.*?>&nbsp;/&nbsp;(.*?)</span>.*?>&nbsp;/&nbsp;([^a-z]+)</span>', i,
#                       re.S):
#             title = re.findall(
#                 'class="title">(.*?)</span>.*?>&nbsp;/&nbsp;(.*?)</span>.*?>&nbsp;/&nbsp;([^a-z]+)</span>', i,
#                 re.S)
#         else:
#             title = re.findall('class="title">(.*?)</span>.*?>&nbsp;/&nbsp;(.*?)</span>', i,
#                                re.S)
#         title = collate_title(title[0])
#         is_player = '可播放' if re.findall('class="playable">(.*?)</span>', i) else '不可播放'
#         # 可能出现没有导演的情况
#         other_message = re.findall(
#             '<p class="">\s+(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>\s+(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\s+</p>', i,
#             re.S) if re.findall(
#             '<p class="">\s+(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>\s+(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\s+</p>', i,
#             re.S) else re.findall(
#             '<p class="">\s+(.*?)(<br>)\s+(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\s+</p>', i,
#             re.S)
#         other_message = collate_message(other_message)
#         score = re.findall('property="v:average">(.*?)</span>', i)
#         evaluate_num = re.findall('<span>(.*?)评价</span>', i)
#         Film_review = re.findall('<span class="inq">(.*?)</span>', i) if re.findall('<span class="inq">(.*?)</span>', i,
#                                                                                     re.S) else ['无评论']
#         database(title, is_player, other_message, score[0], evaluate_num[0], Film_review[0])
#
#
# def database(title, is_player, other_message, score, evaluate_num, Film_review):
#     """
#     数据库存储
#     :param title:标题
#     :param is_player:是否播放
#     :param other_message: 其他数据
#     :param score: 评分
#     :param evaluate_num:评价人数
#     :param Film_review: 电影评价
#     :return:
#     """
#     print(title, other_message[0][3:], other_message[1][3:],
#           other_message[2], other_message[3], other_message[4],
#           score, evaluate_num, Film_review, is_player)
#     # print(evaluate_num)
#     movie_data = {'标题': title, '导演': other_message[0][3:], '主演': other_message[1][3:],
#                   '出版时间': other_message[2], '类型': other_message[4], '评分': score,
#                   '评论人数': evaluate_num, '电影点评': Film_review, '是否播放': is_player}
#     col.insert_one(movie_data)
#     # col.delete_many({'age': '21'})
#
#
#
# # get_data()
# data = col.find()
# for i in data:
#     print(i)


# 所学内容
# 一.在终端调用mongodb数据库
# （1）数据库处理
# 1.创建数据库
# use DouBan_data
# 2.查询数据库（插入数据之后才会显示）
# show DouBan_data
# 3.查看当前数据库
# db
# 4.删除数据库（使用use到对应的数据库，使用语法后删除对应的数据库）
# db.dropDatabase
# 5.查看所有数据库
# show dbs
#
# （2）集合处理
# 1.创建集合
# db.createCollection('name')
# 2.插入集合
# db.集合名称.insert({'name':'小明'})
# 3.查看集合
# show collections
# 4.删除集合
# db.表名.drop()
#
# （3）集合数据处理
# 1.查看集合
# db.集合名.find()
# 2.集合更新
# <1>一条数据：db.集合名称.updata({'age':18},{$set:{'age':20}})
# <2>多条数据：db.集合名称.update({'age':18},{$set:{'age':20}},{multi:true})
# 3.删除集合的数据
# db.集合名称.remove({'age':20})

# 二.mongodb在Pycharm中的运用
# 1.下载模块
# pip install pymongo
# 2.调用
# import pymongo
# 3.连接数据库
# cli = pymongo.MongoClient()
# 4.选择需要调用的数据库
# db = cli.DouBan_data
# 5.获取需要操作的集合
# col = db.text
# 6.查看集合数据
# for i in col.find():
#     print(i)
# 7.插入集合数据
# <1>插入一条
# col.insert_one({'name': '小王', 'age': '20'})
# <2>插入多条
# data=[{'name': '小金', 'age': '20'},{'name': '小聪明', 'age': '19'}]
# col.insert_many(data)
# 8.删除集合数据
# <1>删除一条
# col.delete_one({'name': '小王', 'age': '20'})
# <2>删除多条
# col.delete_many({'age': '20'})
# 9.更新集合数据
# <1>更新一条
# col.update_one({'name': '小王'}, {'$set': {'name': '小聪明'}})
# <2>更新多条
# col.update_many({'name': '小聪明'}, {'$set': {'name': '小王'}})

