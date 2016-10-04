#!/usr/bin/python
# -*- coding: utf-8 -*-

from obsapp.models import Ogrenci,OgretimGorevlisi
class CustomAuthentication(object):
    def authenticate(self,username=None,password=None):
        try:
            ogrenci = Ogrenci.objects.get(ogrenciNo=username,parola=password)
            return ogrenci
        except Ogrenci.DoesNotExist:
            return None
    def authenticateogret(self,username=None,password=None):
        try:
            ogretimelemani = OgretimGorevlisi.objects.get(sicilNo=username,parola=password)
            return ogretimelemani
        except OgretimGorevlisi.DoesNotExist:
            return None

