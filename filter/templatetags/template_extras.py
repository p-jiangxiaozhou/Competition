# -*- coding: utf-8 -*-
from django import template

register = template.Library()
app_extras = {"Brand": "品牌管理", "Category": "分类管理",
              "Sku": "商品管理", "Color": "颜色管理",
              "User": "材料商管理", "Order": "订单管理",
              "cinema": "影视管理"}


@register.filter()
def transto(value):
    extras_value = value
    if value in app_extras:
        extras_value = app_extras.get(value)
    return extras_value
