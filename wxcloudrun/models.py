from datetime import datetime

from django.db import models


# Create your models here.
class Counters(models.Model):
    id = models.AutoField
    count = models.IntegerField(max_length=11, default=0)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Counters'  # 数据库表名

class Xueye( models.Model ):
    ZHUANGTAI_OPTION = (
        (0, '在读'),
        (1, '休学'),
        (2, '肆业'),
        (3, '结业'),
    )
    xueye_id = models.CharField( max_length=64, primary_key=True, verbose_name="学业编号" )
    xueye_xueyuan_name = models.CharField( max_length=15, blank=True, default='', verbose_name="报名姓名" )
    xueye_xueyuan_shenfen = models.CharField( max_length=20, blank=False, default='371323190000000000', verbose_name="身份证号" )
    xueye_banji = models.IntegerField( max_length=8, default=99, verbose_name="班级编号" )
    xueye_banji_name = models.CharField( max_length=150, blank=True, default='', verbose_name="班级名称" )
    zhaoshengjihua = models.IntegerField( max_length=8, default=99999999, verbose_name="招生计划" )
    chengji = models.SmallIntegerField( default=0, verbose_name="成绩" )
    zhuangtai = models.SmallIntegerField( choices = ZHUANGTAI_OPTION, default=0, verbose_name="状态" )

    def __str__(self):
        return self.xueye_id

    class Meta:
        ordering = ['xueye_id']
        verbose_name="xueye"
