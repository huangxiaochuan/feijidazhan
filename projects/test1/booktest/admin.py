# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.
class HerrInfoline(admin.TabularInline):
    model = HeroInfo
    extra = 3

#定义一个类
class BookInfoAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10

    #分组页
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']})
    ]
    inlines = [HerrInfoline]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
