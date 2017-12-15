from django.db import models
from db.base_model import BaseModels
from tinymce.models import HTMLField


# Create your models here.
# ��Ʒģ����
class GoodsType(BaseModels):
    name = models.CharField(max_length=20, verbose_name='��������')
    logo = models.CharField(max_length=20, verbose_name='��ʶ')
    # ��Ϊ�Ըı�djangoĬ�ϴ洢��ʽ���Կ������дupload
    image = models.ImageField(upload_to='imagfiles', verbose_name='��ƷͼƬ')

    class Meta:
        db_table = 'df_goods_type'
        verbose_name = '��Ʒ����'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# ��ƷSKUģ��
class GoodSKU(BaseModels):
    status_choices = (
        (0, '����'),
        (1, '����')
    )
    typeof = models.ForeignKey('GoodsType', verbose_name='��Ʒ����')
    goods = models.ForeignKey('Goods', verbose_name='��ƷSPU')
    name = models.CharField(max_length=20, verbose_name='��Ʒ����')
    desc = models.CharField(max_length=256, verbose_name='��Ʒ���')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='��Ʒ�۸�')
    unite = models.CharField(max_length=20, verbose_name='��Ʒ��λ')
    image = models.ImageField(upload_to='goods', verbose_name='��ƷͼƬ')
    stock = models.IntegerField(default=1, verbose_name='��Ʒ���')
    sales = models.IntegerField(default=0, verbose_name='��Ʒ����')
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='��Ʒ״̬')

    class Meta:
        db_table = 'df_goods_sku'
        verbose_name = '��Ʒ'
        verbose_name_plural = verbose_name


# ��ƷSPUģ��
class Goods(BaseModels):
    name = models.CharField(max_length=20, verbose_name='��ƷSPU����')
    detail = HTMLField(blank=True, verbose_name='��Ʒ����')

    class Meta:
        db_table = 'df_goods'
        verbose_name = '��ƷSPU'
        verbose_name_plural = verbose_name


# ��ҳ�ֲ���Ʒչʾģ��
class IndexGoodsBanner(BaseModels):
    sku = models.ForeignKey('GoodSKU')
    image = models.ImageField(upload_to='banner', verbose_name='ͼƬ')
    index = models.SmallIntegerField(default=0, verbose_name='չʾ˳��')

    class Meta:
        db_table = 'df_index_banner'
        verbose_name = '��ҳ�ֲ���Ʒ'
        verbose_name_plural = verbose_name


# ��ҳ������Ʒչʾģ��
class IndexTypeGoodsBanner(BaseModels):
    DISPLAY_TYPE_CHOICES = (
        (0, "����"),
        (1, "ͼƬ")
    )

    type = models.ForeignKey('GoodsType', verbose_name='��Ʒ����')
    sku = models.ForeignKey('GoodSKU', verbose_name='��ƷSKU')
    display_type = models.SmallIntegerField(default=1, choices=DISPLAY_TYPE_CHOICES, verbose_name='չʾ����')
    index = models.SmallIntegerField(default=0, verbose_name='չʾ˳��')

    class Meta:
        db_table = 'df_index_type_goods'
        verbose_name = "��ҳ����չʾ��Ʒ"
        verbose_name_plural = verbose_name


class IndexPromotionBanner(BaseModels):
    '''��ҳ�����ģ����'''
    name = models.CharField(max_length=20, verbose_name='�����')
    url = models.CharField(max_length=256, verbose_name='�����')
    image = models.ImageField(upload_to='banner', verbose_name='�ͼƬ')
    index = models.SmallIntegerField(default=0, verbose_name='չʾ˳��')

    class Meta:
        db_table = 'df_index_promotion'
        verbose_name = "��ҳ�����"
        verbose_name_plural = verbose_name
