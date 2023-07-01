# 家庭作业
# 使用伪分布式，获取站长素材的前20页图片(https://sc.chinaz.com/tupian/index.html)

# 所学内容
# 一、安装scrapy redies
#
# 1.安装步骤在（scrapy-redis 部署文件）文件夹内
# 2.下载模块pip install scrapy-redis
# 3.对下载的文件夹内的redis.windows-service.conf进行设置：
#     <1>注释掉bind 127.0.0.1
#     <2>把protected-mode yes改为protected-mode no
#
#
# 二、使用scrapy redies
# from scrapy_redis.spiders import RedisSpider
# 1.在文件夹内打开start.bat文件
# ps：其实主要是打开redies服务
#
# 2.spiders文件内进行继承
# class ImageSpider(RedisSpider):
#
# 3.导入键值对
# redis_key = 'Zzsc:start_urls'
#
# 4.setting文件内引入关键配置
# 主要代码：
# #使用scrapy_redis组件自己的调度器   setting文件设置
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"#调度器
# # 确保所有spider通过redis共享相同的重复过滤。
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"#过滤器
# # 可选 不清理redis队列，允许暂停/恢复抓取。 允许暂定,redis数据不丢失
# SCHEDULER_PERSIST = True
# False：表示每次数据重新获取
# True：表示暂停后继续获取
# # REDIS 主机和端口
# REDIS_HOST = '127.0.0.1'  # 写自己电脑的ip地址（公司可以写老板的ip）
# REDIS_PORT = 6379
#
# 5.启动程序（redis-cli.exe）
# lpush 键:值  网址
