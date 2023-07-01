from ckeditor.fields import RichTextField
from django.db import models

from django.db import models

# 器材表
from mdeditor.fields import MDTextField


# 数据
class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()


class Tie_zi(models.Model):
    data = RichTextField()


class Comment(models.Model):
    # 之前为 body = models.TextField()
    body = RichTextField()


class UserProfile(models.Model):
    pass
