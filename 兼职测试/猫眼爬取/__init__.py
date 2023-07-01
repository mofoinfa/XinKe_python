import requests_html
import time
import random
from fontTools.ttLib import TTFont
import re
import hashlib
import json
import ddddocr
import io
from PIL import Image, ImageDraw, ImageFont
import openpyxl

class MaoYan():

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.wb.create_sheet('表1',0)
        self.ws = self.wb.active
        self.ws.append(['最新影片','票房占比','综合票房','排片场次'])
        self.session = requests_html.HTMLSession()
        self.ocr = ddddocr.DdddOcr()
        self.url = 'https://piaofang.maoyan.com/dashboard-ajax?'
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Cookie": "_lxsdk_cuid=18673fcc542c8-0838ff9a967645-7d5d5474-144000-18673fcc542c8; _lxsdk=F674EEA0AEB711EDAA5BB1A1595AB3D213896FAC360247C89ED56961EDCE0841; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1676634067,1677031589; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1677031600; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_s=18676e19511-f7e-ce7-ba%7C%7C22",
            "Host": "piaofang.maoyan.com",
            "Pragma": "no-cache",
            "Referer": "https://piaofang.maoyan.com/dashboard?requestCode=b52679642af2b58757e0de64e8066504vuzud",
            "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Microsoft Edge\";v=\"109\", \"Chromium\";v=\"109\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 Edg/109.0.1518.61"
        }
        self.headers_woff = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "s3plus.meituan.net",
            "Origin": "http://pf.fe.st.maoyan.com",
            "Pragma": "no-cache",
            "Referer": "http://pf.fe.st.maoyan.com/"
        }
        self.time = int(time.time()*1000)
        self.index = int(1000*random.random())

    def get_sign_key(self,index,time):
        e = f'method=GET&timeStamp={time}&User-Agent=TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDYuMDsgTmV4dXMgNSBCdWlsZC9NUkE1OE4pIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDkuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYgRWRnLzEwOS4wLjE1MTguNjE=&index={index}&channelId=0&sVersion=2&key=A013F70DB97834C0A5492378BD76C53A'
        res = hashlib.md5(e.encode())
        resp = res.hexdigest()
        return resp

    def get_url(self):
        url = f'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=18673fcc542c8-0838ff9a967645-7d5d5474-144000-18673fcc542c8&timeStamp={self.time}&User-Agent=TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDYuMDsgTmV4dXMgNSBCdWlsZC9NUkE1OE4pIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDkuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYgRWRnLzEwOS4wLjE1MTguNjE%3D&index={self.index}&channelId=0&sVersion=2&signKey={self.get_sign_key(self.index,self.time)}'
        return url

    def data_exchange(self,num,font_list):
        count = ''
        num_list = num.strip().split(';')
        for num in num_list:
            if num:
                for data in font_list[1:]:
                    if num.startswith('.'):
                        key = 'uni' + num[1:].upper()
                        if key in data:
                            count = count+'.'+data.get(key)
                    else:
                        key = 'uni' + num.upper()
                        if key in data:
                            count = count+data.get(key)
        return count+'万'

    def parse_detail(self,response,font_list):
        res = re.sub('&#x','',response)
        json_data = json.loads(res)
        for data in json_data['movieList']['data']['list']:
            movie_name = data['movieInfo']['movieName']
            releaseinfo = data['boxRate']
            num = data['boxSplitUnit']['num']
            showcount = data['showCount']
            num_new = self.data_exchange(num,font_list)
            movie_data_list = [movie_name,releaseinfo,num_new,showcount]
            print(movie_data_list)
            self.save(movie_data_list)

    def font_to_img(self,txt, filename):
        img_size = 1024
        img = Image.new('1', (img_size, img_size), 255)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(filename, int(img_size * 0.7))
        txt = chr(txt)
        x, y = draw.textsize(txt, font=font)
        draw.text(((img_size - x) // 2, (img_size - y) // 2), txt, font=font, fill=0)
        return img

    def get_woff_detail(self,url,response):
        self.headers.update(self.headers_woff)
        resp = self.session.get(url).content
        with open('updatafont.woff',mode='wb')as f:
            f.write(resp)
        font = TTFont('updatafont.woff')
        font.saveXML('updatafont.xml')
        font_dic = font.getBestCmap().items()
        analysis_res = []
        for i, Glyphname in font_dic:
            pil = self.font_to_img(i, 'updatafont.woff')
            pil.save('aaa.png')
            bytes_io = io.BytesIO()
            pil.save(bytes_io, format="PNG")
            res = self.ocr.classification(bytes_io.getvalue())
            analysis_res.append({Glyphname: res})

        self.parse_detail(response,analysis_res)


    def get_response(self):
        url = self.get_url()
        self.session.headers = self.headers
        res = self.session.get(url)
        woff = re.findall('v1/(.*?)"',res.text)[-1]
        woff_url = 'http://s3plus.meituan.net/v1/' + woff[:-1]
        self.get_woff_detail(woff_url,res.text)

    def save(self,data):
        self.ws.append(data)
        self.wb.save('猫眼电影实时数据.xlsx')

    def start(self):
        self.get_response()

if __name__ == '__main__':
    s = MaoYan()
    s.start()