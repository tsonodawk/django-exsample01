from django.db import models
from django.urls import reverse


class Employee(models.Model):
    """従業員"""
    name = models.CharField('氏名', max_length=255)
    age = models.IntegerField('年齢', blank=True, default=0)
    birthday = models.DateField('誕生日', blank=True, null=True)
    hiredate = models.DateField('入社日', blank=True, null=True)
    retiredate = models.DateField('退社日', blank=True, null=True)
    createddate = models.DateTimeField('登録日時', auto_now_add=True)
    lastmodifieddate = models.DateTimeField('最終更新日時', auto_now=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     """
    #     更処理完了時の戻り先URL
    #     """
    #     return reverse('employee:index')
