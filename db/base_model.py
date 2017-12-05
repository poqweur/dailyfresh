from django.db import models

class BaseModels(models.Model):
    create_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)#auto_now_add就是设置创建时间的参数
    update_time=models.DateTimeField(verbose_name='更新时间',auto_now=True)#auto_now设置更新时间
    is_delete=models.BooleanField(default=False,verbose_name='删除标记')

    class Meta:
        #说明这是个抽象类
        abstract=True