# 家庭作业
# 1、写两个案例，分别使用到模板标签  if判断与for循环。截图即可（但是要清晰）
# 所学内容
# 一、模板
# 1.介绍
# 将数据返回给HTML网页
#
# 2.配置
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],  #指定模板文件的存放路径，格式：'DIRS': [os.path.join(BASE_DIR, 'templates')]
#         'APP_DIRS': True, #搜索APP里面的所有templates目录
#         'OPTIONS': {
#             'context_processors': [  #context_processors 用于配置模板上下文处理器
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# 3.模板响应返回数据的格式
# （1）方法一：通过 loader 获取模板，通过 HttpResponse 进行响应
# from django.http import HttpResponse
# from django.template import loader
# # 1.通过loader加载模板
# t = loader.get_template("模板文件名")
# # 2.将t转换成HTML字符串
# html = t.render(字典数据)
# # 3.用响应对象将转换的字符串内容返回给浏览器
# return HttpResponse(html)
#
# （2）方法二：使用 render 方法直接加载并响应模板
# from django.shortcuts import render
# return render(request,'模板文件名', 字典数据)
#
# 4.模板语言
# （1）HTML文件中输出接收的数据
# <1>{{name}}#返回的字典数据（name为字典的键，显示的是字典的值）
#
# <2>if表达式
#     {% if 条件表达式1 %}
#     {% elif 条件表达式2 %}
#     {% endif %}
#
# <3>for表达式
#     {% for 变量 in 可迭代对象 %}
#     ... 循环语句
#     {% empty %}
#     ... 可迭代对象无数据时填充的语句
#     {% endfor %}
#     常用迭代方法：
#         | forloop.counter    | 用来计数，查看当前迭代第几个元素（从1开始索引）     |
#         | forloop.revcounter | 表示当前循环中剩余的未被迭代的元素数量（从1开始索引）|
#         | forloop.first      | 如果当前迭代的是第一个元素，则为True             |
#         | forloop.last       | 如果当前迭代的是最后一个元素，则为True           |
#         | forloop.parentloop | 在嵌套循环中，用来引用外层循环的 forloop

# <4>urls语言
# 介绍：引用地址时，urls.py中地址蚕食name可以被html的模板语言调用
# urls.py:
#     urlpatterns = [
#         path('Hello_MyWeb/', views.Hello_MyWeb, name='url_name'),
#         path('test_url/', views.test_url)
#     ]
# html""
#     {% url 'url_name' %}
#

# <5>注释
# {% comment %}
# ...要被注释的内容放在两个标签中间
# {% endcomment %}
# （2）模板语言应用
# views文件下：
#     a = {}  # 创建空字典，模板必须以字典的形式进行传参
#     <1>字符-分写法：return render(request, 'test_html.html', {'name':'乔治'})
#     a['name'] = '乔治' #分写法：
#     <2>数组-分写法：return render(request, 'test_html.html', {'course':["Python", "C", "C++", "Java"]})
#     a['course'] = ["Python", "C", "C++", "Java"]
#     <3>字典-分写法：return render(request, 'test_html.html', {'b':{'course':'享学', 'address': '1'}})
#     a['b'] = {'name': '享学', 'address': 'https://www.baidu.com/'}
#     <4>函数名-分写法：return render(request, 'test_html.html', {'test_hello':test_hello})
#     a['test_hello'] = test_hello
#     <5>函数-分写法：return render(request, 'test_html.html', {'class_obj':Website()})
#     a['class_obj'] = Website()
#     return render(request, 'test_html.html', a)
# html文件下:
#     <p>字符{{ name }}</p>
#     <p>数组{{ course.0 }}</p>
#     <p>字典是{{ b }}</p>
#     <p>字典的元素a['address']是{{b.address}}</p>
#     <p>函数名：{{ test_hello }}</p>#调用值为返回的return
#     <p>函数内对象：{{class_obj.Web_name}}</p>
#

