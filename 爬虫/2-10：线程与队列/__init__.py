# 家庭作业
# https://www.duitang.com/category/?cat=wallpaper
# 获取堆糖的前5页图片 使用生产者和消费者模式
# import queue
# from queue import Queue
#
# import requests
# import re
# from threading import Thread
#
# q = Queue()  # 创建队列
#
#
# def get_data():
#     """
#     获取数据
#     :return:
#     """
#     url = 'https://www.duitang.com/napi/blog/list/by_search/'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
#     }
#     for i in range(0, 24 * 5, 24):
#         params = {
#             'include_fields': 'like_count,sender,album,msg,reply_count,top_comments',
#             'kw': '壁纸',
#             'start': i,
#         }
#         html_data = requests.get(url, headers=headers, params=params)
#         get_img(html_data.text)
#
#
# def get_img(img):
#     """
#     通过数据解析图片
#     :param img:
#     :return:
#     """
#     img_url = re.findall('"photo":.*?"path":"(.*?)",', img)
#     for img in img_url:
#         img_name = img[-25:]
#         q.put([img_name, img])
#
#
# def sava_img():
#     """
#     保存图片
#     :return:
#     """
#     while True:
#         print(f'目前队列：{q.qsize()}')
#         try:
#             img_name, img = q.get(timeout=5)
#         except queue.Empty:
#             break
#         img_data = requests.get(img)
#         f = open(f'img\{img_name}', 'wb')
#         f.write(img_data.content)
#         f.close()
#
#
# if __name__ == '__main__':
#     Thread(target=get_data()).start()  # 生产者
#     for i in range(10):
#         Thread(target=sava_img()).start()  # 消费者

# 所学内容

# 一、队列的作用
# 规律：先进先出
# 作用：加快运行速度
# 二、队列的基本知识
# 1.队列的引用
# <1>import queue #全部导入
# <2>from queue import Queue #一般情况
# 2.定义
# q=Queue()
# 3.将一个数据放入队列中
# q.put()
# 4.将队列中的数据取出
# <1>取之方法
#     q.get()
# <2>验证是否已经取完
#     try:
#         q.get(timeout=5)#5s没有取到值，则结束取值
#     except queue.Empty:
#         print('里面已经没有数据了')
#
# 5.判断队列是否为空
# q.empty() #返回bool值
# 6.判断队列是否为满
# q.full()#返回bool值
# 7.返回队列的长度
# q.qsize()

# 三、实战，王者荣耀高清壁纸获取前五页
import requests
import re
from urllib import parse
import queue
from threading import Thread


def data_analysis(params):
    """
    解析数据
    :param params:
    :return:
    """
    data = requests.get(url, headers=headers, params=params)
    name = re.findall('"sProdName":"(.*?)"', data.text)
    img_url = re.findall('"sProdImgNo_6":"(.*?)"', data.text)
    for name, img_url in zip(name, img_url):
        img_name = parse.unquote(name)
        img_url = parse.unquote(img_url)  # 解析数据乱码
        img_url = img_url[:-3] + '0'  # 将最后的三个数字删除
        q.put([img_name, img_url])
    # print(data)


def save_img():
    """
    保存队列
    :return:
    """
    try:
        img_name, img_url = q.get(timeout=5)
        img = requests.get(img_url)
        f = open(f'王者_img/{img_name}.jpg', 'wb')
        f.write(img.content)
        f.close()
    except queue.Empty:
        print('数据已经取出')
    print(f'目前队列{q.qsize()}')


q = queue.Queue()
url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
}
for i in range(1, 6):
    params = {
        'activityId': '2735',
        'sVerifyCode': 'ABCD',
        'sDataType': 'JSON',
        'iListNum': '20',
        'totalpage': '0',
        'page': i,
        'iOrder': '0',
        'iSortNumClose': '1',
        'jsoncallback': 'jQuery11130891451590526193_1677062564967',
        'iAMSActivityId': '51991',
        '_everyRead': 'true',
        'iTypeId': '2',
        'iFlowId': '267733',
        'iActId': '2735',
        'iModuleId': '2735',
    }
    Thread(target=data_analysis, args=(params,)).start()  # 生产者

    # 消费者
    for i in range(10):
        Thread(target=save_img).start()
