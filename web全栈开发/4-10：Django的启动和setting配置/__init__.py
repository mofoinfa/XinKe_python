# # 家庭作业
# # 简述一下MVC设计模式和MTV设计模式。
# 1、MVC
# 1. 用户通过浏览器向服务器发起 request 请求，Controller 接受请求后，同时向 Model 和 View 发送指令
# 2. Mole 根据指令与数据库交互并选择相应业务数据，然后将数据发送给 Controller
# 3. View 接收到 Controller 的指令后，加载用户请求的页面，并将此页面发送给 Controller
# 4. Controller 接收到 Model 和 View 的数据后，将它们组织成响应格式发送给浏览器，浏览器通过解析后把页面展示出来
#
# 2.MTV
# 1. 用户通过浏览器对服务器发起 request 请求，服务器接收请求后，通过 View 的业务逻辑层进行分析，同时向 Model 层和 Template 层发送指令；
# 2. Mole 层与数据库进行交互，将数据返回给 View 层；
# 3. Template 层接收到指令后，调用相应的模板，并返回给 View 层；
# 4. View 层接收到模板与数据后，首先对模板进行渲染（即将相应的数据赋值给模板），然后组织成响应格式返回给浏览器，浏览器进行解析后并最终呈现给用户。


# 所学内容
# 一、Django的初步运用
# 1.Django的安装
# pip install django==3.2
# 清华源：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==3.2
#
# 2.Django项目创建
# （1）方法一（终端-cmd）：
# cd到目标文件夹后：django-admin startproject Bookstore
#
# （2）方法二（推荐）：
# Pycharm新建一个项目
#
# 3.访问Django项目
# 指令：python manage.py runserver
#
# 二、setting的配置
# 1.BASE_DIR
# 绑定文件的依赖路径
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# 2.DEBUG
# 用于配置 Django 项目的启用模式，有两种取值方式：
# DEBUG = True用于在开发环境中使用，属于调试模式，在项目的运行过程中会暴露一些错误信息以方便调试。
# DEBUG = False用于线上环境，表示不启用调试模式。
#
# 3.ALLOWED_HOSTS
# 用于编辑添加自己的应用
#
# 4.LANGUAGE_CODE和TIME_ZONE
# 分别代表语言配置项和当前服务端时区的配置项，我们常用的配置如下所示：
# LANGUAGE_CODE 取值是英文：'en-us'或者中文：'zh-Hans'；
# TIME_ZONE 取值是世界时区 'UTC' 或中国时区 'Asia/Shanghai'。
# 案例：
# # 设置为中文模式
# LANGUAGE_CODE = 'zh-Hans'
# TIME_ZONE = 'Asia/Shanghai'
#
# 5.数据库（DATABASES）
# （1）安装mysqlclient
# 方法1：pip install mysqlclient
# 方法2：https://www.lfd.uci.edu/~gohlke/pythonlibs/在此文件中下载whl进行安装
# （2）在setting中配置数据库信息
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'bookstoredb',
#         'USER': 'root',
#         'PASSWORD': 'xzy472260102',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }
