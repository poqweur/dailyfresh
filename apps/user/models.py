from django.db import models  # ����ŵ��Ǳ��ж�Ӧ���ֶ�
# �����Լ���д��ģ�͸���
from db.base_model import BaseModels
# todo:��չ���е��û�ģ��,�����ĵ��Զ����û���֤
from django.contrib.auth.models import AbstractUser


# �û���
class User(AbstractUser, BaseModels):
    # Ԫ��ѡ��
    class Meta:
        # ���ݿ��еı���
        db_table = 'df_user'
        # վ������ʾ������
        verbose_name = '�û�'
        # վ����ȡ��������ʾ
        verbose_name_plural = verbose_name


# ��ַ��
class Address(BaseModels):
    user = models.ForeignKey('User', verbose_name='�����û�')
    receiver = models.CharField(max_length=20, verbose_name='�ռ���')
    addr = models.CharField(max_length=256, verbose_name='�ռ���ַ')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='��������')
    phone = models.CharField(max_length=11, verbose_name='��ϵ��ʽ')
    is_default = models.BooleanField(default=False, verbose_name='�Ƿ�Ĭ��')

    class Meta:
        db_table = 'df_address'
        verbose_name = '��ַ'
        verbose_name_plural = verbose_name
