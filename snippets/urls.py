# -*- coding: utf-8 -*-
# @Date    : 2021-05-28 17:31 
# @Author  : yepeng
# @Des:
from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(regex=r'^snippets/$', view=views.snippet_list),
    url(regex=r'^snippets/(?P<pk>[0,9]+)/$', view=views.snippet_detail)
]
