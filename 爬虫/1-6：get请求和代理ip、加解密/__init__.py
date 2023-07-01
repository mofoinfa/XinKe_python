# 家庭作业
# 获取链家网的前5页数据，并且保存到txt或者html文件
# https://cs.lianjia.com/ershoufang
# import requests
#
# for i in range(1, 6):
#     url = f'https://cs.lianjia.com/ershoufang/pg{i}/'
#     head_data = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
#     }
#
#     html = requests.get(url, headers=head_data)
#     f = open(f'链家网第{i}页.txt', 'w+', encoding='utf-8')
#     f.write(html.text)
#     f.close()


# 所学内容
# 一、安装两个必要的包
# 1.dlib:pip install urllib3#用于解密数据
# 实例用法：将网页的加密参数进行解密
# from urllib import parse
#
# print(f"加密：{parse.urlencode({'wd': '西瓜'})}")  # 将西瓜进行加密，传参需要是一个字典类型
# print(f"解密：{parse.unquote('wd=%E6%A8%A1%E5%9D%97%E4%B8%8B%E8%BD%BD')}")  # 解密，参数可以为一个字符串

# 2.request：# pip install requests 在命令窗口或者终端安装请求模块
# 实例用法1：抓取百度数据---无形参
# import requests
# url = 'https://www.baidu.com/'
# # 请求的标头，表示自己的信息，可以使用伪装的
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
# }
# html = requests.get(url, headers=headers)
# print(html.text)
# 实例用法2：抓取百度搜索的西瓜页面---有形参
# import requests
#
# url = 'https://www.baidu.com/s'
# # 请求的标头，表示自己的信息，可以使用伪装的
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
#                   'Cookie': 'BIDUPSID=C7D9963B67BA811E923F2D407E629C10; PSTM=1617448568; __yjs_duid=1_d31de959fb659416cd56b3df01ca74c71620300019707; BAIDUID=8099F3C8D6ED2F15F4829FE2620342B5:FG=1; ZFY=MCi57kdTrBXzChzcR7AWLORLg6WXBFaH8Y3gp2OU4tc:C; BAIDUID_BFESS=8099F3C8D6ED2F15F4829FE2620342B5:FG=1; __bid_n=1842c6732ebb26fd8f4207; BDUSS=B6bDc2T1RkVFh-cEVVLUVTckptc05sQS0yMGE5TGJ-alE4M2V0RndYVDRwNHhqRVFBQUFBJCQAAAAAAAAAAAEAAADPCGOF0%7Eu2ydL4utMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgaZWP4GmVjaV; BDUSS_BFESS=B6bDc2T1RkVFh-cEVVLUVTckptc05sQS0yMGE5TGJ-alE4M2V0RndYVDRwNHhqRVFBQUFBJCQAAAAAAAAAAAEAAADPCGOF0%7Eu2ydL4utMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgaZWP4GmVjaV; FEID=v10-7500759fb136a2207f831939edd3f66a9dbbfaf6; BD_UPN=12314753; __xaf_fpstarttimer__=1672904134379; __xaf_thstime__=1672904134580; __xaf_fptokentimer__=1672904134582; RT="z=1&dm=baidu.com&si=5oabnppokmg&ss=lcrxb765&sl=3&tt=2r8&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=374&ul=al8c&hd=ala3"; FPTOKEN=E17R1Ak3W0t4z0qAmQv4GyT92MSBdEUpk6iwWpXog2PEpfC5MCX6WtNbCVZfE8evrEogtRcmzTQIM0zM71/iLV/1OGAMfTiF8v5r/XMmBddN+7vwh5W2B5ELmWixxiC+afoQAyl6Yzwp6IjV24blaHfUe6y0yGZ/zb6Xn5YpdAKlH0n9UW0Uj7Ic1jVn8o1rnzJmmuzhgdU8aIrtrJE9zmS4feE7NuVjEAf2Qku6MSGzk7JWUVl9Ai4wvcD252zlt7916j8M1YnmysmLD2Fza8HmYkE4IffujmetWCiQuwqpYUXtLCQRltDJRNFfhlhpW9y2Xd99+QSEy3BWv9QKr6PS3p51Ts9niw9uwcjfVHozpDLt3GSvcDOnR62sExinNQ/3zc1oe7dVSXhm7+WOVw==|qm/Ix0+N8azTsYmSESE0bHuNeuVdMmsCqJqPDkDXARw=|10|2a45ddbdaa43c3676f92ec2a900d8391; BD_HOME=1; BA_HECTOR=a50h0l2h2k2l2k8l01058g921hs08dh1l; BD_CK_SAM=1; PSINO=6; delPer=0; H_PS_PSSID=36560_37972_37646_37551_37518_37907_38022_36920_38035_37990_36803_37919_38041_26350_37957_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; channel=bing; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1673536372; BDRCVFR[feWj1Vr5u3D]=-_EV5wtlMr0mh-8uz4WUvY; sugstore=1; H_PS_645EC=498avnh4Y48DQcxYyvcymcWpWNxmmSNlDa06Cn0s0YINsBF520y%2BOeNO6%2FsAOvxP7Bfe; B64_BOT=1; baikeVisitId=d2465c1a-08af-4adb-91f6-7ebbf6f0a115; COOKIE_SESSION=109_0_7_8_4_16_1_0_7_7_0_3_601314_0_0_0_1665404568_0_1673536382%7C9%23539517_16_1664527897%7C9; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1673536546'
# }
# # 页面后的形参，可以抓包负载的数据进行调用
# params = {
#     'wd': '西瓜',
#     'rsv_spt': '1',
#     'rsv_iqid': '0xb64c1adf00126f27',
#     'issp': '1',
#     'f': '8',
#     'rsv_bp': '1',
#     'rsv_idx': '2',
#     'ie': 'utf-8',
#     'tn': 'baiduhome_pg',
#     'rsv_enter': '1',
#     'rsv_dl': 'tb',
#     'rsv_sug3': '7',
#     'rsv_sug1': '4',
#     'rsv_sug7': '101',
#     'rsv_sug2': '0',
#     'rsv_btype': 'i',
#     'inputT': '2130',
#     'rsv_sug4': '2631',
#     'rsv_sug': '1',
# }
# html = requests.get(url, headers=headers, params=params)
# html.encoding = 'utf-8'  # 将字符转化为中文
# print(html.text)

# 二、代理ip
# 1.类型
# 普通代理  告诉你我使用了代理 告诉你真实IP地址
# 匿名代理  告诉你我使用了代理 不会告诉我的真实ip地址
# 高匿代理  不会告诉使用了代理，更不会告诉真实ip地址
# 2.写法

# import requests

# url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'
# head_data = {
#     # 字典，需要有一个键值对
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
# }
#
# # 代理ip（）
# proxies = {
#     'HTTPS': '112.28.228.35:28828'  # 页面显示的头文件是什么就用什么（http->HTTP，https->HTTPS）
# }
# # html = requests.get(url, proxies=proxies, headers=head_data)
# # print(html.text)


# 三、get爬虫的步骤
# 1.找数据（查找数据在哪个网址）
# 2.确认数据是否在该源代码中
# ps：如果在，则一定是get请求
# 3.如果请求失败，可能是headers没有写全，或者是params没有写全
