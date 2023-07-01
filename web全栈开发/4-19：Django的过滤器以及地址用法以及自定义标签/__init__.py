# 家庭作业
# 利用Django框架实现一个有15个a标签的页面
# 要求：
# 1、利用django模板的url标签
# 2、每个a标签都对应一个页面（herf属性不能相同）
# 3、a标签的文本也不能相同（就是a标签括起来的部分）
# 需要提供视图函数的代码截图，模板文件的代码截图，子路由代码图、最终效果图。（共四张）

# 所学内容
# 一、过滤器（例举以下为常用过滤器）
# （1）使用 length 过滤器得到变量的长度
#     实例：<p>hello:{{world|length}}</p>#world为传入字典的键
#
# （2）dictsort 它指定字典的键为参数，最后返回按照指定键排序的列表
#     # 数据
#     {'value':[
#         {'name': 'C语言', 'num':2 },
#         {'name': 'Django官网', 'num': 1},
#         {'name': 'Python官网', 'num': 3},
#     ]}
#     # 过滤器
#     <p>hello:{{value|dictsort:"num"}}</p>
#     #综上，结果根据num的值大小进行从小到大的排序
# （3）add相加方法，数字进行加法，列表进行合并
#     # 数据
#     {'value':'5'}
#     # 过滤器
#     {{ value|add:2 }}
#     # 数据
#     {'value':['python','Django','Flask'],'list':['Tonado','celery']}
#     # 过滤器
#     {{value|add:list}}
#
# 二、地址urls
# 1.path方法函数定义
# （1）方法导入
# 方法一：from django.urls import path
# 方法二：from django.conf.urls import url

# 2.父子地址的继承
#     介绍：为了防止所有路径都写在父路径里所以一般需要让子路径继承于父路径，代码如下
#      初步运用：
#       （1）父urls内:
#           from django.urls import path, include
#           urlpatterns = [
#               path('admin/', admin.site.urls),
#               path('index/', include("index.urls")),#继承app的urls
#           ]
#       （2）子urls内：
#           urlpatterns = [
#               path('test1/', views.test_html),#同目录下views内的方法名
#           ]

# 3.urls的应用
# （1）初步运用
#     介绍：引用地址时，urls.py中地址蚕食name可以被html的模板语言调用
#     urls.py:
#         urlpatterns = [
#             path('Hello_MyWeb/', views.Hello_MyWeb, name='url_name'),
#             path('test_url/', views.test_url)
#         ]
#     html""
#         {% url 'url_name' %}
# （2）调用数字
#     urls.py:
#         urlpatterns = [
#             path('Hello_MyWeb/<int:id>', views.Hello_MyWeb, name='hello')
#         ]
#     html:
#         <p><a href="{% url 'hello' 1 %}" >点我查看django课程</a></p>
# （3）调用字符
#     urls.py:
#         urlpatterns = [
#             path('Hello_MyWeb/<str:name>', views.Hello_MyWeb, name='hello')
#         ]
#     html:
#         <p><a href="{% url 'hello' 王德发 %}" >点我查看django课程</a></p>
# （4）深层次运用
#     urls.py:
#         app_name='index'
#         urlpatterns = [
#             path('Hello_MyWeb/', views.Hello_MyWeb, name='hello')
#         ]
#     html:
#         <p><a href="{% url 'index:hello' %}" >点我查看django课程</a></p>
# 三、自定义标签
# （1）建立自定义标签步骤如下：
# 1.在setting的INSTALLED_APPS内添加应用
# 2.在对应的app下建立包templatetags（名字不能变）
# 3.在包下建立py文件index_tags.py （名字不能变）
# 4.在index_tags.py头部添加如下代码：
#     from django import template
#     register = template.Library()
# 5.按照以下格式创立自定义标签
#     @register.simple_tag#每个函数头必加
#     def addstr_tag(strs):
#         return 'Hello%s' % strs
#
# 二、html中的调用方式
# {% addstr_tag 'Django BookStore' %}#addstr_tag为函数名，'Django BookStore'为变量
#
# 三、实战，创建四个加减乘除的自定义标签
# 代码如上方项目的defined文件所示