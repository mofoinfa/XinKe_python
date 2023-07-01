# 家庭作业
# 写两个视图函数
# 1个存储10本书
# 另一个查询10本书，展示在前端页面。
# 代码和效果都要截图
# 项目在上方文件中

# 所学内容
# 一、Django的数据库应用
# 1.导入相关model类（views.py）
# from index.models import Book #导入相关model类（index为创建文件夹，Book为其中的类）

# 2.orm(最常用)
# （1）数据插入
# <1>普通
# 向数据库插入数据(可在shell中使用一样的操作，指令：python manage.py shell )
# book=Book(title="Python",public="清华出版社",price="80.00",retail_price="80.00")
# book.save()# 调用save方法进行保存
# <2>判断插入
# Book.objects.get_or_create(name="Xiaolong")#先查询是否存在若不存在则新建该实例对象

# （2）单数据查询
# Book.objects.get(name="Tom")
#
# （3）修改
# book=Book.objects.all().get(name='Tom')
# book.name='hhh' book.update(name='测试开发交流会')

# （4）删除
# book = Book.objects.all().get(name='测试开发交流会')
# book.delete()


# 3.raw方法语句(常用)
# 以查询为例
#     veiws.py:
#         books=Book.objects.raw("select * from index_book") #书写sql语句
#         return render(request,"index/allbook.html",locals())
#     html:
#         {% for book in books %}
#             <p>{{book.title}}</p>
#         {% endfor %}

# 4.游标cursor执行SQL语句
# 代码如下：
# from django.db import connection
# with connection.cursor() as cur:
#     cur.execute('执行SQL语句')
