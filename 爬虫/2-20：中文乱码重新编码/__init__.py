# 家庭作业
# https://www.shixiseng.com/interns
# 获取实习僧的一页数据显示出来
# 字体反爬  自定义字体文件  10
# 通过编码 -》 绘制出文字

# import requests
# import re
# import io
# from fontTools.ttLib import TTFont
#
#
# def get_font():
#     """获取文字文件"""
#     initial_link = re.findall('@font-face {    font-family: myFont;    src: url\((.*?)\);}', html.text)
#     correct_link = 'https://www.shixiseng.com' + initial_link[0]
#     print(correct_link)
#     ttf = TTFont(io.BytesIO(requests.get(correct_link).content))  # 获取该地址中的文字
#     ttf.save('wz.ttf')  # 保存为ttl格式
#     ttf.saveXML('wz.xml')
#     # https://www.shixiseng.com/interns#网站的源地址
#     # /interns/iconfonts/file?rand=0.23140103281109337#字体地址
#     # https://www.shixiseng.com/interns/iconfonts/file?rand=0.23140103281109337#拼接
#
#
# def wz_transcoding():
#     """
#     进行文字转码
#     :return:
#     """
#     wz_dict = '  0123456789一师x会四计财场DHLPT聘招工d周L端p年hx设程二五天tXG前KO网SWcgkosw广市月个BF告NRVZ作bfjnrvz三互生人政AJEI件M行QUYaeim软qu银y联'
#     # 获取uni字体
#     uni_list = re.findall(' <GlyphID id="(.*?)" name="(.*?)"/>', open('wz.xml', 'r').read())
#     # 获取乱码数据
#     messyCode_list = re.findall('<map code="(.*?)" name="(.*?)"/>', open('wz.xml', 'r').read(), re.S)
#     messyCode_list = list(set(messyCode_list))
#     # print(messyCode_list)
#     uni_dict, messyCode_dict = {}, {}  # 创建字典
#     for i, j in uni_list:
#         uni_dict[j] = i
#     for i, j in messyCode_list:
#         messyCode_dict[i] = j
#     return wz_dict, uni_dict, messyCode_dict
#
#
# def parse_data(data):
#     data = str(data).replace('0x78', '')#将格式不同的第一次进行转化
#     raplace_data = re.findall('0x....', data)#利用正则表达式获取所有可能的情况
#     raplace_data = list(set(raplace_data))#去重
#     for i in raplace_data:
#         index = uni_dict[messyCode_dict[i]]#得到解码的编号
#         # print(wz_dict[int(index)])
#         data=data.replace(i, wz_dict[int(index)])#替换乱码为正确的中文
#     return data
#
#
# url = 'https://www.shixiseng.com/interns'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
# }
#
# html = requests.get(url, headers=headers)
# internship = re.findall('class="title ellipsis font".*?>(.*?)</a>', html.text)
# salary = re.findall('class="day font".*?>(.*?)</span>', html.text)
# internship = [str(i).replace('&#', '0') for i in internship]  # 根据xml更改原本的数据
# salary = [str(i).replace('&#', '0') for i in salary]  # 根据xml更改原本的数据
#
# # get_font()
# wz_dict, uni_dict, messyCode_dict = wz_transcoding()  # 获得解析字典
# internship = [parse_data(i) for i in internship]
# salary = [parse_data(i) for i in salary]
# print(internship)
# print(salary)


# 所学内容
# 一、获取文字地址
# 1.在源文件内搜索@font
# 2.根据网页首地址进行拼接，拼接成完整的地址

# 二、获取文件的ttf,xml文件对比文字
# from fontTools.ttLib import TTFont
# import io
# import requests
# data=TTFont(io.BytesIO(requests.get('文字网址').content))
# data.save('xxx.ttf')#保存后用该项目文件夹内的app打开，获取文字信息
# data.saveXML('xxx.xml')#保存后，通过正则获取文件中内容并转化成字典形式
