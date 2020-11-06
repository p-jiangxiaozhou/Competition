from django.db import models


class Goods(models.Model):
    name = models.CharField(u'商品名称', max_length=100, null=False, )
