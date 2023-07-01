from django.http import HttpResponse
from django.template import loader  # 导入loader方法


def test_html(request):
    # 获取模板对象
    dic = {'num': {}}
    for i in range(15):
        dic['num'][i+1] = i * 25
    print(dic)
    t = loader.get_template('index/test.html')
    html = t.render(dic)  # 以字典形式传递数据并生成html
    return HttpResponse(html)  # 以 HttpResponse方式响应html

def defined(request):
    t = loader.get_template('index/defined.html')
    html = t.render({'num': 3})  # 以字典形式传递数据并生成html
    return HttpResponse(html)  # 以 HttpResponse方式响应html
