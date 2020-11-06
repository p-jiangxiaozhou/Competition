from django.db import models


class Order(models.Model):
    no = models.CharField(u'订单编号', max_length=20, null=False, unique=True, )
