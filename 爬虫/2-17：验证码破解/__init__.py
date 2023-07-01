# # 家庭作业
# # https://passport.bilibili.com/login b站模拟登录的点触验证码破解
# # 截图破解成功的图片即可
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from PIL import Image
# import time
# from chaojiying import Chaojiying_Client
# import operator
#
#
# def basic_information():
#     """
#     基本信息填入
#     :return:
#     """
#     username = driver.find_element(By.XPATH, '//*[@id="login-username"]')  # 账号
#     username.send_keys('12345678')
#     password = driver.find_element(By.XPATH, '//*[@id="login-passwd"]')  # 密码
#     password.send_keys('123456')
#     login_btn = driver.find_element(By.XPATH, '//*[@id="geetest-wrap"]/div/div[5]/a[1]')
#     login_btn.click()  # 登陆按钮
#
#
# def get_picture():
#     """
#     图片获取
#     :return:
#     """
#     time.sleep(2)
#     driver.save_screenshot('yzm.png')
#     img = Image.open('yzm.png')
#     # 验证码坐标
#     cropped = img.crop((791, 353, 1114, 677))
#     cropped.save('yzm_s.png')
#     # 验证码顺序
#     cropped = img.crop((950, 300, 1107, 350))
#     cropped.save('yzm_wz.png')
#
#
# def mask_data(png):
#     """
#     数据解析
#     :param png: 图片名称
#     :return:合理的数据
#     """
#     chaojiying = Chaojiying_Client('13398854476', 'Xzy13398854476@', '945125')
#     data = chaojiying.PostPic(open(png, 'rb').read(), 9501)  # 数据获取
#     data = str(data['pic_str']).split('|')  # 根据|进行分割
#     tep_data = []
#     # 按照横坐标排序
#     for i in range(len(data)):
#         tep_data.append(data[i].split(','))
#         tep_data[i][1] = int(tep_data[i][1])
#     data = sorted(tep_data, key=operator.itemgetter(1))
#     return data
#
#
# def verificationCode():
#     """
#     验证码破解
#     :return:
#     """
#     literal_order = mask_data('yzm_wz.png')  # 文字顺序
#     literal_data = mask_data('yzm_s.png')  # 文字坐标
#     literal_pos = []
#     # 根据文字顺序获取对应的正确坐标
#     for i in literal_order:
#         for j in literal_data:
#             if j[0] in i:
#                 literal_pos.append([j[1], j[2]])
#     clike_btn(literal_pos)  # 点击
#     print(f'坐标：{literal_pos}')
#     print(f'顺序：{literal_order}')
#     print(f'数据：{literal_data}')
#
#
# def clike_btn(pos):
#     """
#     点击坐标
#     :return:
#     """
#     action = ActionChains(driver)
#     element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div/div[2]/div[1]/div/div[2]')
#     for x, y in pos:
#         print(x, y)
#         action.move_to_element(element).move_by_offset(
#             int(x) / 1.3 - 152 / 1.3,
#             int(y) / 1.3 - 145 / 1.3
#         ).click().perform()
#         time.sleep(1)
#         print(f'成功点击')
#     affirm = driver.find_element(By.CLASS_NAME, 'geetest_commit_tip')
#     affirm.click()
#
#
# driver = webdriver.Chrome(service=Service('D:\\Chrome\\chromedriver.exe'))
# driver.get('https://passport.bilibili.com/login')
# basic_information()
# time.sleep(2)
# get_picture()
# verificationCode()
# input()

# 所学内容
# 一、破解验证码的网站
# 1、图灵（http://tulingtech.xyz/#/）
# import base64
# import json
# import requests
# def b64_api(username, password, img_path, ID):
#     with open(img_path, 'rb') as f:
#         b64_data = base64.b64encode(f.read())
#     b64 = b64_data.decode()
#     data = {"username": username, "password": password, "ID": ID, "b64": b64, "version": "3.1.1"}
#     data_json = json.dumps(data)
#     result = json.loads(requests.post("http://www.tulingtech.xyz/tuling/predict", data=data_json).text)
#     return result
# 最终返回需要的结果值

# 2、超级鹰（https://www.chaojiying.com/）
# 下载python文件，将py文件导入
# from chaojiying import Chaojiying_Client
# cjy=Chaojiying_Client('13398854476', 'Xzy13398854476@', '945125')
# cjy.PostPic('图片','所用类型的编号')
# 实例：chaojiying.PostPic(open(png, 'rb').read(), 9501)  # 数据获取


# 3.屏幕截图
# <1>截取整个屏幕的图片
# # driver.save_screenshot('yzm.png')
# <2>打开图片
# from PIL import Image
# img = Image.open('yzm.png')
# <3>截图
# ropped = img.crop((791, 353, 1114, 677))#所要图片左上角的坐标，以及右下角坐标
# <4>保存图片
# cropped.save('ss.png')


# 4.实战--网易易顿滑动验证码破解
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from PIL import Image
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.action_chains import ActionChains
import base64
import json
import requests


def page_slide():
    """
    设置页面滑动
    :return:
    """
    js = 'window.scrollTo(0,%s)' % 200
    driver.execute_script(js)


def access_yzm():
    # 点击滑动
    sliding_btn = driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[2]/div[2]/ul/li[2]')
    sliding_btn.click()
    # 进行页面滑动
    page_slide()
    time.sleep(4)
    access_yzm = driver.find_element(By.CLASS_NAME, 'yidun_intelli-tips')
    access_yzm.click()


def get_img():
    """
    获取图片
    :return:
    """
    time.sleep(3)
    driver.save_screenshot('智能/qt.png')
    img = Image.open('智能/qt.png')
    ropped = img.crop((470, 442, 843, 628))
    ropped.save('智能/yzm.png')


def get_pos(username, password, img_path, ID):
    with open(img_path, 'rb') as f:
        b64_data = base64.b64encode(f.read())
    b64 = b64_data.decode()
    data = {"username": username, "password": password, "ID": ID, "b64": b64, "version": "3.1.1"}
    data_json = json.dumps(data)
    result = json.loads(requests.post("http://www.tulingtech.xyz/tuling/predict", data=data_json).text)
    pos = result['data']['缺口']['X坐标值']
    print(pos)
    return get_move_track(pos * 0.6666)


# 行为路径
def get_move_track(gap):
    print(gap)
    track = []  # 移动轨迹
    current = 0  # 当前位移
    # 减速阈值
    mid = gap * 4 / 5  # 前4/5段加速 后1/5段减速
    t = 0.2  # 计算间隔
    v = 0  # 初速度
    while current < gap:
        if current < mid:
            a = 5  # 加速度为+5
        else:
            a = -5  # 加速度为-5
        v0 = v  # 初速度v0
        v = v0 + a * t  # 当前速度
        move = v0 * t + 1 / 2 * a * t * t  # 移动距离
        current += move  # 当前位移
        track.append(round(move))  # 加入轨迹
    return track


def active(track):
    diamond = driver.find_element(By.CLASS_NAME, 'yidun_jigsaw')
    ActionChains(driver).click_and_hold(diamond).perform()  # 按住标签不放
    for i in track:
        ActionChains(driver).move_by_offset(i, 0).perform()  # 每次移动一点点
    ActionChains(driver).release().perform()


driver = webdriver.Chrome(service=Service('D:\\Chrome\\chromedriver.exe'))
driver.get('https://dun.163.com/trial/sense')
access_yzm()
get_img()
active(get_pos('13398854476', 'Xzy13398854476@', '智能/yzm.png', '78915616'))
input()
