# 所学内容
# 一、应用创建
# 1.创建命令
# （1）cd到目标文件下
# （2）输入代码：python manage.py startapp index
#
# 2.配置
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'index',#如此所示
# ]
# 二、数据库搭建
# 1.配置变量
# （1）安装mysqlclient
# 方法1：pip install mysqlclient
# 方法2：https://www.lfd.uci.edu/~gohlke/pythonlibs/在此文件中下载whl进行安装
# （2）在setting中配置数据库信息
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'bookstoredb',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': ' ',
#         'PORT': '3306',
#     }
# }
#
# 2.在应用中的modle文件中创建class类
# （1）创建代码如下：
# class Userinfo(models.Model):
# （2）创建类型如下：
# 地址："""https://blog.csdn.net/qq_42486675/article/details/106772211?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168242788116782425186686%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=168242788116782425186686&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-4-106772211-null-null.142^v86^control_2,239^v2^insert_chatgpt&utm_term=Django%E7%9A%84%E6%95%B0%E6%8D%AE%E5%BA%93%E5%AD%97%E6%AE%B5%E7%B1%BB%E5%9E%8B&spm=1018.2226.3001.4187"""
# 列举几个常用类型：
# (1) AutoField
# 自增的整型字段，必填参数primary_key=True,则成为数据库的主键，无该字段时，django会自动创建主键id字段。
#
# (2) BigAutoField
# 一个64位整数，非常类似与AutoField，但是范围是从1~9223372036854775807。
#
# (3) BigIntegerField
# 一个64位整数，非常类似于IntegerField，不同之处在于保证可以匹配从-9223372036854775808到9223372036854775807。
# 此字段默认表单小部件是TextInput。
#
# (4) BooleanField
# 一个真假字段，该字段默认表单控件是CheckboxInput或者NullBooleanSelect。
# 当没有设置default值是，BooleanField的值为None。
#
# (5) IntegerField
# 整数类型字段，数值范围是—2147483648~2147483647.
#
# (6) CharField
# 字符类型，必须提供max_length参数。代表字符的最大长度。
#
# (7) DateField
# 日期类型，日期格式为YYYY-MM-DD，相当于python中的datetime.date实例。
# 参数：
# <1>auto_now：每次修改保存修改为当前日期时间，对于“最后修改的” 时间戳有用。
# 在使用Model.save()保存时有效，使用QuerySet.update() 时不会自动更新。
# <2>auto_now_add：新创建对象时自动添加当前日期时间，用于“创建时间”时使用。
# <3>uto_now和auto_now_add和default参数是互斥的，不能同时设置。
#
# (8) FloatField
# 代表在python中由float实例表示的浮点数。
#
# (9) ImageField
# 继承FileField所有的方法，但还验证上传的对象为有效的图像。除了 可用于特殊属性FileField，
# 一个ImageField也具有height和width 属性。为了便于查询这些属性，ImageField有两个额外的可选参数。
# 在数据库中创建的为varchar列，默认最大长度为100字符。
# ImageField.height_field：每次保存模型实例时，模型字段的名称都会自动填充图像的高度。
# ImageField.width_field：每次保存模型实例时，模型字段的名称都会自动填充图像的宽度。
#
# 3.数据库迁移
# cd到目标文件终端输入一下代码：
# python manage.py makemigrations
# python manage.py migrate

# 4.超级管理员
# 1.创建超级管理员指令
# python manage.py createsuperuser --username='用户名' --email=admin@163.com
# 指令执行后会输入两次密码
#
# 2.将要管理的表导入对于app的index文件内
# 代码如下：
# from django.contrib import admin #Django自动在admin.py文件中导入
# from index.models import Book, Author,UserInfo #这个需要我们自己导入相应的模型类（数据表）
# admin.site.register([Book,Author,UserInfo])
