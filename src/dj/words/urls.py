# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<from_iso>\w+)/(?P<word>\w+)/$', views.words, name='words'),
    url(r'^(?P<from_iso>\w+)/(?P<word>\w+)/(?P<to_iso>\w+)/$', views.word, name='word')
]
