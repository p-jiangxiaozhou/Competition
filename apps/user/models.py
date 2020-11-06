from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)
from common.common import get_file_path
from datetime import datetime


class UserManager(BaseUserManager):
    def create_user(self, account, nick, password=None, **extra_fields):
        """
        创建一个用户，账号，和密码
        """
        now = datetime.now()
        if not account:
            raise ValueError(u'必须填写账号')
        user = self.model(account=account, nick=nick, create_time=now, update_time=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, account, nick, password, **extra_fields):
        """
        创建一个超级用户
        """
        u = self.create_user(account=account, nick=nick, password=password, **extra_fields)
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u

    class Meta:
        app_label = (u'basesite')


class User(AbstractBaseUser, PermissionsMixin):
    account = models.CharField(u'账号', max_length=30, unique=True, )
    email = models.CharField(u'邮箱', max_length=50, unique=True, )
    nick = models.CharField(u'昵称', max_length=20, unique=True, )
    avatar = models.ImageField(u'头像', upload_to=get_file_path, max_length=100, blank=True)
    is_superuser = models.BooleanField(u'是否超级管理员', default=False, )
    is_staff = models.BooleanField(u'是否管理员', default=True, )
    is_active = models.BooleanField(u'是否有效', default=True, )
    create_time = models.DateTimeField(u'注册时间', auto_now_add=True, )
    update_time = models.DateTimeField(auto_now=True, )

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = (u'管理员帐号')

    objects = UserManager()
    USERNAME_FIELD = 'account'
    REQUIRED_FIELDS = ['nick', ]
    EMAIL_FIELD = 'email'

    def get_full_name(self):
        return self.nick

    def get_short_name(self):
        return self.nick

    def __str__(self):
        return self.email
