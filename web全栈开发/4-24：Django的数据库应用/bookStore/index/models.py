from django.db import models

class book(models.Model):
    """书城"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sellingPrice = models.IntegerField()
    purchasingPrice = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return "title:%s pub:%s price:%s" % (self.name, self.sellingPrice, self.purchasingPrice)
