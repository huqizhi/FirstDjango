from django.urls import path
from django.conf.urls import url, include
from blog import views
urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('add', views.add),
    path('toadd', views.to_add),
    url('^toinfo/(?P<id>\d+)/$', views.to_info),
    #url('^toinfo/(\d+)$', views.to_info),
]