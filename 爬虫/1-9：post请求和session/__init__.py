# 家庭作业
# https://passport.17k.com/
# 使用session模拟登录17k小说网站
# import requests
#
# # 验证登陆，获取正确的信息
# session = requests.session()
# url = 'https://passport.17k.com/ck/user/login'
# head_data = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
# }
# data = {
#     'loginName': '13398854476',
#     'password': 'Xzy472260102'
# }
# html = session.post(url, headers=head_data, data=data)
# print(html.json())
# f = open('验证登陆.txt', 'w+', encoding='utf-8')
# f.write(html.text)
#
# print('-' * 10, '登陆页面', '-' * 10)
# # 进行登陆
# url = 'https://user.17k.com/www/userinfo/index.html'
# head_data = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
# }
# html = session.get(url, headers=head_data)
# print(html.text)
# f = open('登陆页面.txt', 'w+', encoding='utf-8')
# html.encoding = 'utf-8'
# f.write(html.text)


# 所学内容
# 一、常见问题和步骤
# 步骤：
#     1.找数据（确认数据是否在在网页上）
#     2.若没在，很有可能是post请求，使用抓包进行验证
#     3.补全头文件
# 常见问题：
#     1.获取不到需要的数据:1增加cookie等其他比较重要的请求头信息
#     2.获取的数据是乱码状态:
#         1)写Accept-Encoding 容易乱码 请求头里面不要写
#         2)html = requests.get(url,headers=head_data),html.encoding = 'utf-8' # 解决数据乱码

# 二、post请求
# 实例1，获取百度logo图片
# 案例内容总结：
#             1、判断get请求
#             2、爬取数据有字节流（text），二进制编码（.content,open存取（wb）），json数据（.json）
#             3、根据头文件补全链接

import requests
url = ' http://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'  # 有三个图片，抓包提前唯一的图片
head_data = {
    # 字典，需要有一个键值对
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 在源代码中能发现
logo = requests.get(url, headers=head_data)
print(logo)
# f = open('百度logo.png', 'wb')
# f.write(logo.content)
# f.close()

# 实例2，获取百度翻译的数据
# 案例内容总结：
#             1、抓包找到对应的数据，在网络文件内进行搜索，找到负载最多数据的网址

# import requests
#
# url = 'https://fanyi.baidu.com/v2transapi'  # 有三个图片，抓包提前唯一的图片
# head_data = {
#     # 字典，需要有一个键值对
#
#     'Referer': 'https://fanyi.baidu.com/',
#     'Acs-Token': '1673510707025_1673540620857_WOOKLog92MYmDIqvisLzgdSfArW+6zAO7WNnOW/KxO0AD9gn8K5JtoA+lTeU1lIu9T39FrR92GcCg8RFhwcg90WGgfVoR+yMfq3tCxElnkD8uzqs1MkHrgNg93II5yw89Lg7plL7YG5h1hBKakPPd3Cd9B6VqcRY/k4Hziq25gRbY5IGtIIZTKXP+DkEM+qG2TcEDGJpp0uNkxWKIpMKQ9y0LQs3XGfUWxvufJAnIGiksGWdvlIxiNH+7EHl0EzRU5dIyhNfQpFyQOSRQCrtGaiU6CPu/rHrRfvDybsgD/aF/7YB15yzKIId9ttoTBEXyXFRvVxzEiZUmBTQjMAFC9+/OTnyDeJ8vimex+j1FkI=',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
#     'Cookie': 'BIDUPSID=C7D9963B67BA811E923F2D407E629C10; PSTM=1617448568; __yjs_duid=1_d31de959fb659416cd56b3df01ca74c71620300019707; BAIDUID=8099F3C8D6ED2F15F4829FE2620342B5:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=B6bDc2T1RkVFh-cEVVLUVTckptc05sQS0yMGE5TGJ-alE4M2V0RndYVDRwNHhqRVFBQUFBJCQAAAAAAAAAAAEAAADPCGOF0%7Eu2ydL4utMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgaZWP4GmVjaV; BDUSS_BFESS=B6bDc2T1RkVFh-cEVVLUVTckptc05sQS0yMGE5TGJ-alE4M2V0RndYVDRwNHhqRVFBQUFBJCQAAAAAAAAAAAEAAADPCGOF0%7Eu2ydL4utMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgaZWP4GmVjaV; H_PS_PSSID=36560_37972_37646_37551_37518_37907_38022_36920_38035_37990_36803_37919_38041_26350_37957_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=8099F3C8D6ED2F15F4829FE2620342B5:FG=1; BA_HECTOR=240ka1002h040g0h8l0k21gv1hs0ac71k; ZFY=HBvkjYNnzBevESVYLLPWzJPNXq3Yt:AHh:AxhPd0HDmpo:C; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1673539462; ab_sr=1.0.1_MGEyYzMzYWQzODkzNzVmMDJiNWRiOTYwODJhNjY1ZTVhMDI1Nzc0OTE4MGUwMTU2MjkyZGZiZTBjZGRjMWYwYzMxYjY3YjQ0YTcxZGIxOWE5NjRkYjU5MjEyZjNjYmQwZGEwZmQ3OTI0NjIxODIxN2I3NmUxNGEyMzM1M2Y2ZDc3YWQ2YjE2NzEyNzlkNzdhZDkzYjM4NDRkZWUzYTFiNzk0YWJmZDRmMTc3MGYxODc5NzRjZmNmYmQwZmNkZTFj; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1673540620'
# }
# data = {
#     'from': 'zh',
#     'to': 'en',
#     'query': '香蕉',
#     'transtype': 'realtime',
#     'simple_means_flag': '3',
#     'sign': '816986.562283',
#     'token': 'fdd69a7c544421a1202958c3fcdbcef5',
#     'domain': 'common',
# }
# # 在源代码中能发现
# html = requests.post(url, headers=head_data, data=data)
# html.encoding='utf-8'
# print(html.json())

# 三、session的使用
# 通过get获取session，在通过同一个session进行post请求
# 写法:
# import requests
# session=requests.session()#创建session对象
# session.post()#请求session的id
# session.post()#通过session的id进行访问
