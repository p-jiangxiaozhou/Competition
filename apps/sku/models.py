from django.db import models
from common.common import get_file_path
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(u'分类名称', max_length=20, null=False, )
    parent = models.ForeignKey('self', verbose_name='上级分类', null=True, blank=True, default=0,
                               on_delete=models.CASCADE, )
    is_active = models.BooleanField(u'是否有效', default=True, )
    create_time = models.DateTimeField(u'添加时间', auto_now_add=True, )
    update_time = models.DateTimeField(u'更新时间', auto_now=True, )

    class Meta:
        db_table = 'mdc_category'
        verbose_name = verbose_name_plural = (u'分类信息表')

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(u'商品名称', max_length=100, null=False, )
    sub_title = models.CharField(u'小标题', max_length=200, null=True, blank=True, )
    img = models.ImageField(u'封面图', max_length=100, upload_to=get_file_path, null=False, )
    category = models.ForeignKey(Category, verbose_name='商品分类', null=False, blank=False, on_delete=models.PROTECT, )
    price = models.DecimalField(u'商品价格', null=False, max_digits=10, decimal_places=2, default=0.00, )
    discount = models.DecimalField(u'优惠价', null=True, max_digits=10, decimal_places=2, blank=True, )
    integral = models.IntegerField(u'商品积分', null=True, blank=True, default=0, )
    summary = RichTextUploadingField(verbose_name='商品详情', null=True, blank=True, )
    is_active = models.BooleanField(u'是否有效', default=False, )
    create_time = models.DateTimeField(u'添加时间', auto_now_add=True, )
    update_time = models.DateTimeField(u'更新时间', auto_now=True, )

    def img_tag(self):
        return u'<img src="%s" width="200px" />' % self.img.url

    img_tag.short_description = u'封面图'
    img_tag.allow_tags = True

    class Meta:
        db_table = 'mdc_goods'
        verbose_name = verbose_name_plural = (u'商品信息表')

    def __str__(self):
        return self.name


class GoodsPic(models.Model):
    goods = models.ForeignKey(Goods, verbose_name='商品信息', null=False, blank=False, on_delete=models.CASCADE, )
    url = models.ImageField(u'图片地址', null=False, blank=False, max_length=100, upload_to=get_file_path, )
    create_time = models.DateTimeField(u'添加时间', auto_now_add=True, )
    update_time = models.DateTimeField(u'更新时间', auto_now=True, )

    class Meta:
        db_table = 'mdc_goods_pic'
        verbose_name = verbose_name_plural = (u'商品图片表')

    def __str__(self):
        return self.url.name
