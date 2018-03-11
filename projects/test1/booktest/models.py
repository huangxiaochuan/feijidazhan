# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
#图书表结构
class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()
    def __str__(self):
        return self.btitle.encode('utf-8')

#英雄表结构
class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=1000)
    hbook=models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname.encode('utf-8')


