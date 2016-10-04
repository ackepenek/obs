#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('OgrenciBilgiSistemi',
    url(r'^$',"obsapp.views.index",name="index"),
    url(r'^login/$',"obsapp.views.login",name="loginuser"),
    url(r'^logout/$',"obsapp.views.logout",name="logoutuser"),
    url(r'^update/$',"obsapp.views.update",name="updateuser"),
)
