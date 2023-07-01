# #家庭作业
# # 使用正则表达式获取链家网数据
#
# # 获取链家网前5页的数据 爬取标题 爬*-* 位置 总价格和单价
# # 保存到text文件里面 一条数据存一行
# # 作业提交保存数据的截图

# 第一种做法（追加）
# import requests
# import re
#
# f = open('房子数据.txt', 'a+', encoding='utf-8')
# for i in range(1, 6):
#     url = f'https://cs.lianjia.com/ershoufang/pg{i}/'
#     head_data = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
#     }
#     html = requests.get(url, headers=head_data)
#     # print(html.text)
#     title = re.findall('data-is_focus="" data-sl="">(.*?)</a>', html.text)
#     pos = re.findall('data-el="region">(.*?)</a>.*?target="_blank">(.*?)</a>', html.text)
#     totalPrices = re.findall('</i><span class="">(.*?)</span><i>(.*?)</i>', html.text)
#     unitPrice = re.findall('data-price=".*?"><span>(.*?)</span>', html.text)
#     for i in range(len(title)):
#         f.write(f'标题：{title[i]}\t')
#         f.write(f'位置：{pos[i][0]}-{pos[i][1]}\t')
#         f.write(f'总价格：{totalPrices[i][0]}{totalPrices[i][1]}\t')
#         f.write(f'单价:{unitPrice[i]}\n')
# f.close()

# 第二种做法（重置）
# import requests
# import re
#
# f = open('房子数据.txt', 'w', encoding='utf-8')
# message = []
#
# for i in range(1, 6):
#     url = f'https://cs.lianjia.com/ershoufang/pg{i}/'
#     head_data = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
#     }
#     html = requests.get(url, headers=head_data)
#     # print(html)
#     title = re.findall('data-is_focus="" data-sl="">(.*?)</a>', html.text)
#     pos = re.findall('data-el="region">(.*?)</a>.*?target="_blank">(.*?)</a>', html.text)
#     totalPrices = re.findall('</i><span class="">(.*?)</span><i>(.*?)</i>', html.text)
#     unitPrice = re.findall('data-price=".*?"><span>(.*?)</span>', html.text)
#     for i in range(len(title)):
#         message.append((title[i], pos[i], totalPrices[i], unitPrice[i]))
# # print(message)
# for title, pos, totalPrices, unitPrice in message:
#     f.write(f'{title}|{pos[0]}-{pos[1]}|{totalPrices[0]}{totalPrices[1]}|{unitPrice}\n')
# f.close()

# 所学内容
# 1.换行爬取
# import re
#
# data = '<div ' \
#        '  id="2">(.*?)' \
#        '</div>'
# title = re.findall('<div id="2">(.*?)</div>', data, re.S)
