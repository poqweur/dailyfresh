from django.db import models
from db.base_model import BaseModels


# Create your models here.

# ������
class OrderInfo(BaseModels):
    # ֧����ʽ
    PAY_METHODS = {
        '1': "��������",
        '2': "΢��֧��",
        '3': "֧����",
        '4': '����֧��'
    }
    # �ֽ��֧����
    PAY_METHODS_ENUM = {
        "CASH": 1,
        "ALIPAY": 2
    }
    # ����״̬
    ORDER_STATUS_ENUM = {
        "UNPAID": 1,
        "UNSEND": 2,
        "UNRECEIVED": 3,
        "UNCOMMENT": 4,
        "FINISHED": 5
    }

    PAY_METHOD_CHOICES = (
        (1, '��������'),
        (2, '΢��֧��'),
        (3, '֧����'),
        (4, '����֧��'),
    )

    ORDER_STATUS = {
        1: '��֧��',
        2: '������',
        3: '���ջ�',
        4: '������',
        5: '�����'
    }

    ORDER_STATUS_CHOICES = (
        (1, '��֧��'),
        (2, '������'),
        (3, '���ջ�'),
        (4, '������'),
        (5, '�����')
    )

    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='����id')
    user = models.ForeignKey('user.User', verbose_name='�û�', null=True)
    addr = models.ForeignKey('user.Address', verbose_name='��ַ')
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='֧����ʽ')
    total_count = models.IntegerField(default=1, verbose_name='��Ʒ����')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='��Ʒ�ܼ�')
    transit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='�����˷�')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='����״̬')
    trade_no = models.CharField(max_length=128, default='', verbose_name='֧�����')

    class Meta:
        db_table = 'df_order_info'
        verbose_name = '������Ϣ'
        verbose_name_plural = verbose_name


# ������Ʒģ��
class OrderGoods(BaseModels):
    order = models.ForeignKey('OrderInfo', verbose_name='����')
    sku = models.ForeignKey('goods.GoodSKU', verbose_name='��ƷSKU')
    count = models.IntegerField(default=1, verbose_name='��Ʒ��Ŀ')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='��Ʒ�۸�')
    comment = models.CharField(max_length=256, default='', verbose_name='����')

    class Meta:
        db_table = 'df_order_goods'
        verbose_name = '������Ʒ'
        verbose_name_plural = verbose_name
