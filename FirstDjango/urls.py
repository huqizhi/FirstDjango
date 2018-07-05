"""FirstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import views
"""
    模块内url引入：url(父正则，include引入子模块的urls.py文件)
    注意：子模块的urls.py文件路径是父正则+子模块的路径的
"""
#子模块配置自己的url路径路由，这里include包含进来--推荐
urlpatterns = [
    path('', views.index),
    url(r'^blog/', include("blog.urls")),
]
#配置所有模块的url路径路由--不推荐
#urlpatterns = [
    # url('^blog$', views.index),
    # path('blog/index', views.index),
    # path('blog/add', views.add),
    # path('blog/toadd', views.to_add),
    # url('^blog/toinfo/(\d+)$', views.to_info)
#]
