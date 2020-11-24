# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_per_page = 20
    model = Order
    search_fields = ['no']
    list_display = ('no', 'price', 'pay_type', 'state', 'create_time', 'update_time',)
    exclude = ['create_time', 'update_time', ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
