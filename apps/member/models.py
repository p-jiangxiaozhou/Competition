#-*- coding: utf-8 -*-
from django.db import models
from ..sku.models import Goods


class Order(models.Model):
    state_choices = (
        (0, '待支付'),
        (1, '已支付'),
        (2, '待发货'),
        (3, '已发货'),
        (4, '退换货中'),
        (5, '完成'),
        (9, '作废'),
        (10, '已用积分兑换'),
    )
    no = models.CharField(u'订单编号', max_length=20, null=False, unique=True, )
    price = models.DecimalField(u'价格', max_digits=10, decimal_places=2, null=False, )
    state = models.SmallIntegerField(u'订单操作', choices=state_choices, null=False, default=0, )
    is_active = models.BooleanField(u'是否有效', default=False, )
    create_time = models.DateTimeField(u'添加时间', auto_now_add=True, )
    update_time = models.DateTimeField(u'更新时间', auto_now=True, )

    class Meta:
        db_table = 'omc_order'
        verbose_name = verbose_name_plural = (u'订单信息')

    def __str__(self):
        return self.no
