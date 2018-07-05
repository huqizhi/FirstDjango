#from __future__ import with_statement
from django.http import HttpResponse
import time
from django.shortcuts import render
from blog.models import Article
import json
import logging
from django.db import transaction

# Create your views here.


def index(request):
    t = time.ctime()
    #articles = Article.objects.all() #取值为循环获取oneEntity.id,oneEneity.name
    articles = Article.objects.all().values_list("id", "name") #取值为循环获取oneEntity[0],oneEneity[1]
    #{"time":t}将t变量值渲染为html文件中的{{time}}，在后端渲染之后传给前端
    return render(request,"blog/index.html", {"time":t, "articles":articles})

#@transaction.on_commit
def add(request):
    # 方式一：
    """
    b = Article(name="python 入门", content="python入门讲义，胡启志讲解", userId=21025024)
    b.save()
    b = Article(name="python 进阶", content="python进阶必学，大神讲解", userId=21025024)
    b.save()
    b = Article(name="python web框架Django", content="python web框架Django，完整学习加项目体验",userId=21025024)
    b.save()
    """
    # 方式二：
    response_data = {}
    response_data['result'] = 0
    response_data['msg'] = '添加失败'
    try:
        #with transaction.on_commit():
        name, content, userId = "", "", 21025024
        if request.method == "get":
            name=request.GET.get("name")
            content=request.GET.get("content")
        else:
            name = request.POST.get("name")
            content = request.POST.get("content")

        newId = Article.objects.create(name=name, content=content, userId=userId)
        response_data['result'] = 1
        response_data['msg'] = '添加成功'
        response_data['newId'] = newId.id

    except EnvironmentError:
        logging.error(str(EnvironmentError))

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def to_info(request, id):
    tmp_article = Article.objects.get(id=id)
    isAjax = int(request.GET.get("ajax", 0))
    if isAjax != 1:
        isAjax = 0

    return render(request, "blog/info.html", {"article": tmp_article, "isAjax": isAjax})


def to_add(request):
    isAjax = int(request.GET.get("ajax", 0))
    if isAjax != 1:
        isAjax = 0
    return render(request, "blog/addArticle.html", {"isAjax": isAjax})