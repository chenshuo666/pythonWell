#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

from django.conf.urls import url, include
from django.contrib import admin
from .views import getAbout,getBlog,getContact,getHome,getLogin,getLogin_blog,getPortfolio,getRegister

urlpatterns = [
    url(r'^login', getLogin),
    url(r'^home', getHome),
    url(r'^about', getAbout),
    url(r'^blog', getBlog),
    url(r'^contact', getContact),
    url(r'^login_blog', getLogin_blog),
    url(r'^portfolio', getPortfolio),
    url(r'^register', getRegister)
]