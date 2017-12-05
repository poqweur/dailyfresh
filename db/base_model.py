from django.db import models

class BaseModels(models.Model):
    create_time=models.DateTimeField(verbose_name='����ʱ��',auto_now_add=True)#auto_now_add�������ô���ʱ��Ĳ���
    update_time=models.DateTimeField(verbose_name='����ʱ��',auto_now=True)#auto_now���ø���ʱ��
    is_delete=models.BooleanField(default=False,verbose_name='ɾ�����')

    class Meta:
        #˵�����Ǹ�������
        abstract=True