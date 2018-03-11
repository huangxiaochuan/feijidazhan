# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import *
from .models import *
#1 from django.template import RequestContext,loader

# Create your views here.
def index(request):
    #1 temp=loader.get_template('bootktest/index.html')
    #1 return HttpResponse(temp.render())
    bookList=BookInfo.objects.all()
    context={'list':bookList}
    return render(request,'bootktest/index.html',context)

def show(request,id):
    book=BookInfo.objects.get(pk=id)
    herolist=book.heroinfo_set.all()

    context={'list':herolist}
    return render(request,'bootktest/show.html',context)
