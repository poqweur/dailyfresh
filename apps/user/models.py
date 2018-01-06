#coding:utf-8
from django.db import models  # 这里放的是表中对应的字段
# 导入自己重写的模型父类
from db.base_model import BaseModels
# todo:扩展已有的用户模型,中文文档自定义用户认证
from django.contrib.auth.models import AbstractUser


# 用户表
class User(AbstractUser, BaseModels):
    # 元类选项
    class Meta:
        # 数据库中的表名
        db_table = 'df_user'
        # 站点中显示的名字
        verbose_name = '用户'
        # 站点中取消复数显示
        verbose_name_plural = verbose_name


# 地址表
class Address(BaseModels):
    user = models.ForeignKey('User', verbose_name='所属用户')
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系方式')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name
