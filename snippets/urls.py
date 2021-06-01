# -*- coding: utf-8 -*-
# @Date    : 2021-05-28 17:31 
# @Author  : yepeng
# @Des:
from django.conf.urls import url
from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     url(regex=r'^snippets/$', view=views.snippet_list),
#     url(regex=r'^snippets/(?P<pk>[0,9]+)/$', view=views.snippet_detail)
# ]
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>', views.snippet_detail)
# ]

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>', views.SnippetDetail.as_view()),
    path('snippets/test', views.Test.as_view()),
]
format_suffix_patterns(urlpatterns=urlpatterns)
