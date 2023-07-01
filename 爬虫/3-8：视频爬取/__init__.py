# 获取a站的博主视频，数量超过5个
# https://www.acfun.cn/
import json
import math
import os
import re
from concurrent.futures import ThreadPoolExecutor

import requests

from FileData import FileData


class AVideo:
    def __init__(self):
        self.video_save_path = r'/爬虫/3-8：视频爬取\\视频\\'  # 视频存放的路径
        self.quality = '1080P'  # 选择分辨率 2160P 1080P+ 1080P 720P 540P 360P
        self.user_id = 12892608  # 视频作者的id
        self.pool = ThreadPoolExecutor(5)  # 创建线程W

        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/105.0.0.0 '
                                      'Safari/537.36'}

        self.file_data = FileData('acfun_video.txt')  # 生成文件操作的对象
        self.url = f'https://www.acfun.cn/u/{self.user_id}'  # 链接凭借
        self.page_total = self.page_get()  # 获取所有页数
        self.video_url_get()  # 获取页面的链接

    def m3u8_url_get(self, video_info, video_url):
        """获取m3u8链接"""
        # 需要保存的分辨率
        m3u8_url = video_info['video_dict'][self.quality]
        html = requests.get(m3u8_url)  # 请求m3u8文件
        ts_list = []
        for i in str(html.text).splitlines():  # 筛选出ts文件
            if '.ts?' in i:
                ts_list.append('https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/' + i)
        self.video_dow(ts_list, video_info, video_url)

    def video_dow(self, ts_list, video_info, video_url):
        """下载视频"""
        paths = self.crate_path(video_info)  # 下载的时候确认存储的路径
        mp4_path = os.path.join(paths,
                                f"{video_info['video_name']}-{self.quality}.mp4")
        f = open(mp4_path, 'ab')
        print(f"{video_info['video_name']}-{self.quality}.mp4 正在下载")
        for index, i in enumerate(ts_list, start=1):
            f.write(requests.get(i).content)
            # print(f"\r目前{index}/总共{len(ts_list)} {video_info['video_name']}-{self.quality}.mp4", end='')
        print(f"{video_info['video_name']}-{self.quality}.mp4 下载成功")
        f.close()
        self.file_data.add_id(video_url + self.quality)

    def crate_path(self, video_info):
        """创建存放视频的用户文件"""
        # 拼接路径
        paths = os.path.join(self.video_save_path, video_info['user_name'])
        try:  # 捕获文件已经存在的异常
            os.makedirs(paths)
        except FileExistsError:
            pass
        return paths

    def json_get(self, data):
        """获取json视频数据"""
        data_code = re.findall('videoInfo = (.*?);', data)[0]
        data_code = json.loads(data_code)  # 将字符串转换为字典格式

        # coverCdnUrls [{url} {url}] 视频封面
        cover_img = data_code['coverCdnUrls'][0]['url']

        # 各个分辨率数据
        video_url = data_code['currentVideoInfo']['ksPlayJson']
        video_json = json.loads(video_url)['adaptationSet'][0]['representation']
        video_dict = {}
        for i in video_json:  # 获取视频的链接和分辨率
            video_dict[i['qualityLabel']] = i['backupUrl'][0]

        # 视频的名字
        video_name = self.rinse_data(data_code['title'])
        # 用户名称
        user_name = self.rinse_data(data_code['user']['name'])
        # 把数据封装到字典中进行返回
        video_info = {'cover_img': cover_img,
                      'video_dict': video_dict,
                      'video_name': video_name,
                      'user_name': user_name}
        return video_info

    def video_url_get(self):
        """获取所有页面的视频链接"""
        for page in range(1, self.page_total + 1):
            data = {
                'quickViewId': 'ac-space-video-list',
                'reqID': '6',
                'ajaxpipe': '1',
                'type': 'video',
                'order': 'newest',
                'page': page,
                'pageSize': '20',
                't': '1670501439798',
            }  # 更具data里面的page参数进行翻页

            html = requests.get(self.url, params=data, headers=self.headers)

            ac_id = re.findall('"(/v/ac\d+)', html.text)  # 获取page页的所有的视频id
            ac_id = ['https://www.acfun.cn' + i for i in ac_id]  # 对id进行拼接

            for url in ac_id:  # 创建线程池
                self.pool.submit(self.pool_start, url)

    def pool_start(self, video_url):

        # 判断视频是否保存
        if self.file_data.select_id(video_url + self.quality):
            pass  # 如果已经保存就跳过
        else:
            html = self.html_get(video_url)  # 获取网页数据
            video_info = self.json_get(html)  # 获取信息
            self.m3u8_url_get(video_info, video_url)  # 保存视频

    def html_get(self, url):
        """传入url，获取网页源代码"""
        html = requests.get(url, headers=self.headers)
        return html.text

    def page_get(self):
        """获取有多少页视频"""
        html = requests.get(self.url, headers=self.headers)
        page_total = re.findall('视频<span>(\d+)</span>', html.text)
        page_total = math.ceil(int(page_total[0]) / 20)  # 向上去整
        return page_total

    def rinse_data(self, str_data):
        """清晰字符串中非法的字符"""
        return ''.join(re.findall('\w', str_data))

AVideo()
