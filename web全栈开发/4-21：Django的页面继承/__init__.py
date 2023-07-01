# 利用所学模板继承知识：
#
# 1、写一个父模板（需要写4个block标签）
#
# 2、再写一个子模板进行继承（需要对4个block标签进行重写）

# 作业如上方文件代码所示

#所学内容
# 一、页面继承
# 1.继承步骤
# （1）在父页面写入以下模块：
#     {% block content %}
#         <p>这是主体内容可以被子模板重写</p>
#     {% endblock content %}
#  上方的content可以随意改写
#
# （2）在子页面最上方写入{% extends 'index/base.html' %}#index/base.html为继承的父页面文件名称
# （3）运用父页面一样的语句进行重写，语句如下
#     {% block content %}
#             <p>这改写内容</p>
#     {% endblock content %}
# 2.实例代码如templates文件夹下的两个html所示
