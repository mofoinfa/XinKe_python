# # 使用selenium模拟登录 17小说网 https://passport.17k.com/
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By  # 导入定位的方法
# import time
#
# driver = webdriver.Chrome(service=Service('D:\\Chrome\\chromedriver.exe'))
# driver.get('https://passport.17k.com/')
# # 跳转弹窗
# ariam = driver.find_element(By.XPATH, '/html/body/iframe')
# driver.switch_to.frame(ariam)
# # 输入账号
# username = driver.find_element(By.XPATH, '/html/body/form/dl/dd[2]/input')  # 输入账号
# username.send_keys('13398854476')
# # 输入账号
# password = driver.find_element(By.XPATH, '/html/body/form/dl/dd[3]/input')  # 输入密码
# password.send_keys('Xzy13398854476@')
# # 输入复选框
# xbox_btn = driver.find_element(By.XPATH, '//*[@id="protocol"]')
# xbox_btn.click()
# # 点击登陆
# login_btn = driver.find_element(By.XPATH, '/html/body/form/dl/dd[5]/input')  # 输入登陆按钮
# login_btn.click()
# input()


# 所学内容
# 一、自动化处理
# 1.安装模块
# pip install selenium
# 下载谷歌驱动
# http://chromedriver.storage.googleapis.com/index.html
# 确认版本，点击右上的三个点，点击浏览器的设置-》点击关于谷歌 查看版本
# 我的版本109.0.5414.75  如果没有对应版本 找它最近的版本 版本向下兼容
# 下载chromedriver_win32.zip  解压chromedriver.exe  存放到一个位置

# 2.自动化模块
# <1>设置驱动
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# driver = webdriver.Chrome(service=Service('D:\\Chrome\\chromedriver.exe'))

# <2>利用驱动跳转页面
# driver.get('https://www.baidu.com/s?wd=%E7%8C%AA%E5%85%AB%E6%88%92%E6%8E%A5%E5%8D%95%E5%B9%B3%E5%8F%B0%E5%AE%98%E7%BD%91&ie=utf-8&tn=15007414_8_pg')

# <3>使其保持不关闭
# input()

# <4>关闭页面
# driver.close()

# <5>获取元素
# from selenium.webdriver.common.by import By
# element=driver.find_element(By.ID,'ID名字')#根据ID获取
# element=driver.find_element(By.XPATH,'元素的XPATH')#根据XPATH获取
# element=driver.find_element(By.CLASS_NAME,'元素的Class_name')#根据类名获取

# <6>获取下拉列表的元素
# from selenium.webdriver.support.select import Select
# select=Select(element)
# select.select_by_index(0)#根据索引获取
# select.select_by_value('value值')#根据value值获取
# select.select_by_visible_text('根据文字获取')#根据文字获取


# <7>等待页面缓存结束在执行
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# wait=WebDriverWait(driver,10)#如果10s还没有反应就报错
# #加载后立刻点击
# wait.until(EC.presence_of_element_located((By.XPATH,'获取元素得Xpath'))).click()


# <8>实际案例
# 实例1：下拉自动选择12306铁路的证件类型(https://kyfw.12306.cn/otn/regist/init)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.service import Service
#
# driver = webdriver.Chrome(service=Service('D:\\Chrome\\chromedriver.exe'))
# driver.get('https://kyfw.12306.cn/otn/regist/init')
# id_card = driver.find_element(By.ID, 'cardType')
# Select(id_card).select_by_index(1)
# Select(id_card).select_by_value('H')
# Select(id_card).select_by_visible_text('护照')
# input()
# 实例2：进入百度贴吧的广告页面并且下拉页面(https://tieba.baidu.com/)
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome(service=Service('D:\\Chrome\\chromedriver.exe'))
# driver.get('https://tieba.baidu.com/')
#
# # 拉取和跳转只能存在一个页面
# # 拉取的是driver页面
# s = 200
# n = 1000
# for i in range(s, n, 5):  # 实现网页下拉
#     js = 'window.scrollTo(0,%s)' % (i * 100)
#     driver.execute_script(js)
#     time.sleep(0.3)
#
# # 因为页面源代码中没有广告标签，因此需要先跳转在进行操作
# iframe = driver.find_element(By.NAME, 'iframeu6739266_0')
# driver.switch_to.frame(iframe)
# time.sleep(2)  # 页面加载缓慢，暂缓2秒
# first_advertising = driver.find_element(By.ID, 'title0')
# first_advertising.click()
#
# input()

# 三、行为链
# <1>调用
# from selenium.webdriver.common.action_chains import ActionChains
# action = ActionChains(driver)

# <2>鼠标移动
# action.move_to_element('获取的元素')

# <3>鼠标点击
# action.click()

# <4>模拟输入
# action.send_keys_to_element(获取的元素，'输入的文本')

# <4>执行命令
# action.perform()


# # <5>实战（在百度里搜索西瓜）
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# # 创建自动化引擎
# driver = webdriver.Chrome(service=Service('D:\\Chrome\\chromedriver.exe'))
# driver.get('https://www.baidu.com/')
# # 创建行为链
# action = ActionChains(driver)
# # 进行搜索
# search = driver.find_element(By.ID, 'kw')
# action.move_to_element(search)
# action.click()
# action.send_keys_to_element(search, '西瓜')
# # 点击搜索
# search_btn = driver.find_element(By.ID, 'su')
# action.move_to_element(search_btn)
# action.click()
# # 执行命令
# action.perform()
# time.sleep(4)
# # 关闭页面
# driver.close()
# input()
