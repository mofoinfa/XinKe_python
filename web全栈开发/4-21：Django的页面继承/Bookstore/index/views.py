from django.http import HttpResponse
from django.template import loader  # 导入loader方法
from django.shortcuts import render  # 导入reder方法

def father_html(request):
    # 获取模板对象
    dic = {'num': {}}
    for i in range(15):
        dic['num'][i+1] = i * 25
    print(dic)
    t = loader.get_template('index/father.html')
    html = t.render(dic)  # 以字典形式传递数据并生成html
    return HttpResponse(html)  # 以 HttpResponse方式响应html

# 定义父模板视图函数
def father_html(request):
    return render(request, 'index/father.html')


# 定义子模板视图函数
def sun_html(request):
    name = 'xiaoming'
    course = ['python', 'django', 'flask']
    return render(request, 'index/sun.html', locals())