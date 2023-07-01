# 家庭作业
# 获取微博日榜前5天的数据(https://www.newrank.cn/public/info/list.html?period=weibo_day)###
# import execjs
# import requests
#
# url = 'https://www.newrank.cn/xdnphb/main/v1/weibo_day/rank'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
# }
#
# # 输入的日期
# day = ['2023-02-28', '2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04']
#
# # 通过js获取数据
# f = open('wb.js', 'r', encoding='utf-8')
# wb = f.read()
# f.close()
# # 获取nonce
# f = open('star_hank.txt', 'w', encoding='utf-8')
# js = execjs.compile(wb)
# for date in day:
#     f.write(date + ':')
#     nonce = js.call('nonce')
#     # 获取xyz
#     h = f"/xdnphb/main/v1/weibo_day/rank?AppKey=joker&end={date}&rank_name=个人认证&rank_name_group=&start={date}" \
#         + "&nonce=" + nonce
#     xyz = js.call('b', h)
#     # print(xyz)
#     data = {
#         'end': date,
#         'rank_name': '个人认证',
#         'rank_name_group': '',
#         'start': date,
#         'nonce': nonce,
#         'xyz': xyz
#     }
#     html = requests.post(url, headers=headers, data=data)
#     # print(html.json())
#     wb_data = html.json()['value']['datas']
#     for i in wb_data:
#         f.write(i['name'] + ',')
#     f.write('\n')
# f.close()

# 所学内容
# 一、导入模块
# pip3 install PyExecJS
#
# 二、js反向使用
# import execjs
# 1.定义
# <1>将网页复制的js代码存入一个新的javascrip文件
#
# <2>读取文件
# f=open('wb.js','r',encoding='utf-8')
# wb_js=f.read()
# f.close()
#
# <3>定义可用的js文件
# js=execjs.compile(wb_js)
#
# <4>调用
# data=js.call('函数名','变量')

# 二、写出百度翻译的脚本（https://fanyi.baidu.com/#zh/en/）
# import execjs
# import requests
#
# url = 'https://fanyi.baidu.com/v2transapi'
#
# cookies = {
#     'BIDUPSID': 'C7D9963B67BA811E923F2D407E629C10',
#     'PSTM': '1617448568',
#     '__yjs_duid': '1_d31de959fb659416cd56b3df01ca74c71620300019707',
#     'BAIDUID': '8099F3C8D6ED2F15F4829FE2620342B5:FG=1',
#     'REALTIME_TRANS_SWITCH': '1',
#     'FANYI_WORD_SWITCH': '1',
#     'HISTORY_SWITCH': '1',
#     'SOUND_SPD_SWITCH': '1',
#     'SOUND_PREFER_SWITCH': '1',
#     'APPGUIDE_10_0_2': '1',
#     'BAIDUID_BFESS': '8099F3C8D6ED2F15F4829FE2620342B5:FG=1',
#     'ZFY': 'UNhchDEPpAGJHDUVC9lcP:AyTGZ2:Ae9:AETENHvxkO7mw:C',
#     '__bid_n': '1842c6732ebb26fd8f4207',
#     'FPTOKEN': 'oeuYR2uWCFoQcVr7ryaH/JzqYzuE2gX+upC2kTv80KedKGSeC2UVExknlBFC+AsQe5TlzLzna5S/KJq41b75E2jMhV+5DHBw+wUsz8g8LEiFmSqDJS9HOJ7Pl3eV8IbVFvbGUNGK11Zhen2FcZoMDzPutxtzZ6q2c/XyOkw9DFWcLywFX5NIGxZG3mjlSwmvtYAZJyK5EREHasuYSfog890IxDTfX2KC/6L7yQHXbH+Y9UXD4K2EQqDtSgkgfqCOZQR5bdfEhscEtl3Zh2k8je1acRX2unvW6kjAk4BNcWs1VCBpA/Y6GqiRcGuVlEH/cpBReVhB2iu4RD5BQ+kCtvMxUgVZGaHMaJ5KG+D1xsLM2cwsEHMK/pfaQovHKfg+40PwLA9/+EvZpgdew5j6gA==|Ue9SVTxwfKKsTI7RpUSGZ/zVmJkq25iHE/jFuQ/cRVA=|10|3e4bb7ad8887e5b62ffa25c7eadc1ed9',
#     'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1677847484,1678025134',
#     'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1678025134',
#     'ab_sr': '1.0.1_YzAxOWEwMzUyMzcyMzVhZjY1YzY1ZjVkYTVlM2E2ZTVjMGE2NzhlOGNiY2Y5NDc1Y2U1ZjBiMTJkY2JjYzMwMjlkZGFjMGU4MTkyODU4ZTNmNDIzZGU1NjMxMTViNWYzMDYwMzg1NDAzNDNiNzU0YjQ0OWNkMjc2OTk0MGZmMWM1NDQxZDZkOTZmNjMyOGQ3Yzk2MGE5Y2UxODJiOTQxMA==',
# }
#
# headers = {
#     'Accept': '*/*',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'Acs-Token': '1678025134384_1678025250157_E+kaCiJRueq7bTR18uE6/JZ/XVsSD/St/m2/NGcRDorT1tdV+MYWNdfNNe+kgC9EVgvmmk6XFLWLgvMCDFtbCjok4ZFsxWbdrIZJHZ3T2gt06qMUBfVqSwp90KkZotJGCfEx24x/gi4p0m+EfNLGor8Vu54bO/yCB57r13N1DhbfrA2Hzhm+folh67moy0vuNYYpUoEcOP/A6aBIeftJDz55o4jIOMaxhmXhj6zPK5INGcTKSLXecf7kV4o2WjUi8fJQZ4941YQ9eExQttv3/NYB77We1SV2lI2GccVbSmirx4naqd0EVCphs4hwOuuNOGVEyDXSmsb9b6MSNRGt/WgbOnfuF99pWwWG42JVLkueLx2Hv5Kj9f2Fiog9KbJ7',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Origin': 'https://fanyi.baidu.com',
#     'Pragma': 'no-cache',
#     'Referer': 'https://fanyi.baidu.com/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
#     'X-Requested-With': 'XMLHttpRequest',
#     'sec-ch-ua': '\\',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '\\',
# }
# f = open('百度翻译.js', 'r', encoding='utf-8')
# t_js = f.read()
# f.close()
# js = execjs.compile(t_js)
# content = input('请输入需要翻译的内容：')
# sigh = js.call('translate', content)
# data = {
#     'from': 'zh',
#     'to': 'en',
#     'query': content,
#     'transtype': 'translang',
#     'simple_means_flag': '3',
#     'sign': sigh,
#     'token': '2c4b78a3bc1452bc67250e97812625b8',
#     'domain': 'common',
# }
#
# response = requests.post(url, headers=headers, data=data, cookies=cookies)
# for i in response.json()['trans_result']['data']:
#     print(i['dst'])

