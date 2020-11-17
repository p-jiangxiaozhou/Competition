from django.contrib import admin
from .models import Brand, Category, Goods, GoodsPic


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_per_page = 20
    model = Brand
    search_fields = ['name']
    list_display = ('name', 'url', 'is_active', 'create_time', 'update_time',)
    exclude = ['create_time', 'update_time', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20
    model = Category
    search_fields = ['name']
    list_display = ('name', 'parent', 'is_active', 'create_time', 'update_time',)
    exclude = ['create_time', 'update_time', ]


class GoodsPicInline(admin.StackedInline):
    model = GoodsPic
    extra = 1
    max_num = 5


@admin.register(Goods)
class GoodsAdnin(admin.ModelAdmin):
    list_per_page = 20
    model = Goods
    inlines = (GoodsPicInline,)
    search_fields = ['name']
    list_display = ('name', 'img', 'category', 'price', 'discount', 'integral', 'is_active',)
    exclude = ['create_time', 'update_time', ]
