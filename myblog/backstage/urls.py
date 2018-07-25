#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

from django.conf.urls import url, include
from django.contrib import admin
from .views import getIndex, getArticle, getNotice, getComment, getCategory, getLoginlog, getManageuser, getSetting, \
    getReadset,getFlink,getAddarticle

urlpatterns = [
    url(r'^index', getIndex),
    url(r'^article', getArticle),
    url(r'^notice', getNotice),
    url(r'^comment', getComment),
    url(r'^category', getCategory),
    url(r'^loginlog', getLoginlog),
    url(r'^manageuser', getManageuser),
    url(r'^setting', getSetting),
    url(r'^readset', getReadset),
    url(r'^flink',getFlink),
    url(r'^addarticle',getAddarticle)
]
