from django.db import models


# Create your models here.
class Userinfo(models.Model):
    """用户表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class books(models.Model):
    """书城"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sellingPrice = models.IntegerField()
    purchasingPrice = models.IntegerField()
    count = models.IntegerField()
