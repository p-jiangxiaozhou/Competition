from django.db import models
from common.common import get_file_path


class Start(models.Model):
    name = models.CharField(u'明星名称', max_length=20, null=False, )
    avatar = models.ImageField(u'明星头像', max_length=100, upload_to=get_file_path, null=False, )
    sex = models.SmallIntegerField(u'性别', null=False, default=0, )

    class Meta:
        db_table = 'mdc_start'
        verbose_name = verbose_name_plural = (u'明星信息')

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(u'电影名称', max_length=45, null=False, )
    director = models.CharField(u'导演', max_length=20, null=False, )

    class Meta:
        db_table = 'mdc_movie'
        verbose_name = verbose_name_plural = (u'电影信息')

    def __str__(self):
        return self.name
