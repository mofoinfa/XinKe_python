from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

# 扩展user模型类
class MyUser(AbstractUser):
    qq = models.CharField('QQ号码', max_length=20)
    weChat = models.CharField('微信账号', max_length=20)
    mobile = models.CharField('手机号码', max_length=11, unique=True)
    # 设置返回值
    def __str__(self):
        return self.username
