from django.http import HttpResponse
from django.template import loader  # 导入loader方法
from django.shortcuts import render  # 导入reder方法
from django.template import Template, Context  # 调用template、以及上下文处理器方法


def test_html(request):
    # 获取模板对象
    t = loader.get_template('index/test.html')
    html = t.render(
        {'books': [{'name':'西游记', 'price': 15},
                   {'name':'水浒传', 'price': 10},
                   {'name':'老人与海', 'price': 20},
                   {'name':'朋友', 'price': 30},
                   {'name':'红楼梦', 'price': 25},
                   {'name':'古诗三百首', 'price': 8}]})  # 以字典形式传递数据并生成html
    return HttpResponse(html)  # 以 HttpResponse方式响应html

