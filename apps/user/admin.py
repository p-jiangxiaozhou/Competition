# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from common.common import md5hex


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    model = User
    readonly_fields = ('last_login',)

    exclude = ['is_superuser', 'groups', 'create_time', 'update_time',
               'user_permissions']
    list_display = ('account', 'nick', 'last_login', 'is_active',)
    list_editable = ['is_active', ]
    search_fields = ['account', 'nick', 'account']
    date_hierarchy = 'create_time'

    def get_queryset(self, request):
        return super(UserAdmin, self).get_queryset(request).filter(is_staff=True).exclude(is_superuser=True)

    def save_model(self, request, obj, form, change):
        obj.password = md5hex(obj.password)
        super(UserAdmin, self).save_model(request, obj, form, change)
        if not obj.is_superuser:
            group = Group.objects.get(name='普通管理员')
            obj.groups.add(group)
