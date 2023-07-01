# # 家庭作业
# # 获取豆瓣top250的所有页数数据[https://movie.douban.com/top250]
# # 解析方式不限，存储到mysql数据库，要求数据截图
# import requests
# import pymysql
# import re
#
# db = pymysql.connect(user='root', password='xzy472260102', database='creepar_data')
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
#     # print(title, other_message[0][3:], other_message[1][3:],
#     #       other_message[2], other_message[3], other_message[4],
#     #       score, evaluate_num, Film_review, is_player)
#
#     # print(db)
#     cursor = db.cursor()
#     sql = '''insert into movie_data(
#         title,
#         director,
#         lead_acter,
#         release_time,
#         release_place,
#         type,
#         score,
#         evaluate_num,
#         Film_review,
#         is_player)
#         values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
#     try:
#         cursor.execute(sql, (title, other_message[0][3:], other_message[1][3:],
#                              other_message[2], other_message[3], other_message[4],
#                              score, evaluate_num, Film_review, is_player))
#         db.commit()
#     except Exception as e:
#         db.rollback()
#         print(f'失败：{e}')
#     # db.close()
#
# get_data()
# db.close()
# 所学内容
# 一、数据库在python中的引用和安装
# 1.安装
# pip install pymysql
# 2.引用
# import pymysql
#
# 二、使用方法
# 1.连接
# db=pymysql.connect(user='root', password='xzy472260102',database='数据库名字')
# 2. 使用cursor()方法获取操作游标
# cursor=db.cursor()
# 3.插入语句
# sql = """INSERT INTO url_data(
#          url_id,
#          url_title,
#          url_author)
#          VALUES (%s,%s,%s)"""
# 4.执行
# try:
#     cursor.execute(sql,('数据','数据','数据'))#执行sql语句
#     db.commit()#提交到数据库执行
# except Exception as e:
#     db.rollback() # 如果发生错误则回滚
#     print(f'失败{e}')#输出失败原因
# 4.关闭数据库
# db.close()
