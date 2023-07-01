from django.contrib import admin #Django自动在admin.py文件中导入
from data_base.models import book,Userinfo #这个需要我们自己导入相应的模型类（数据表）
admin.site.register([book,Userinfo])