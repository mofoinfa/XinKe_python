# 家庭作业(详见zzsc)
# https://sc.chinaz.com/tupian/ 使用scrpay图片管道下载站长素材的前5页图片，存储格式任意

# 所学内容
# 一、scrapy图片的存取
# 1.导入模块
from scrapy.pipelines.images import ImagesPipeline
# ps:需要安装两个模块
# pip install pillow
# pip install image

# 2.存入设置
# <1>在items中设置:image_urls=scrapy.Field()
# <2>图片的存储链接一定为列表格式

# 3.在setting的设置
# <1>存取管道设置
# 'scrapy.pipelines.images.ImagesPipeline': 300,
# <2>存取路径设置（必须为绝对路径）
# IMAGES_STORE = '绝对路径'
# eg:IMAGES_STORE = 'D:\\pycharm\\python\\项目\\python培训\\爬虫\\2-27：\\zzsc\\zzsc\\img\\
# 二、图片更改名字
# 1.点击ctrl进入（from scrapy.pipelines.images import ImagesPipeline）ImagesPipeline的底层逻辑

# 2.重写函数get_media_requests()和函数file_path(self, request, response=None, info=None, *, item=None)

# 3.两个函数细解释
# def get_media_requests(self, item, info):
#     urls = ItemAdapter(item).get(self.images_urls_field, [])#拿取传过来的链接
#     return [Request(u, callback=NO_CALLBACK) for u in urls]#对链接进行一个处理
# def file_path(self, request, response=None, info=None, *, item=None):
#     image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()#根据特征值进行取名
#     return f"full/{image_guid}.jpg"

# 4.在pipelines内重写方法
# class DuitangPipeline(ImagesPipeline):#继承ImagesPipeline
#     def get_media_requests(self, item, info):
#         requests_list = []
#         urls = super().get_media_requests(item, info)
#         for index, i in enumerate(urls):
#             i.name = item['name'][index]#添加一个新名字
#             requests_list.append(i)
#         return requests_list
#
#     def file_path(self, request, response=None, info=None, *, item=None):
#         return f'{request.name}.jpg'#重写写名字
#
# 实战：保存堆糖第一页页的图片,并设置名字为id('https://www.duitang.com/category/?cat=wallpaper)
# 详见duiTang案例

