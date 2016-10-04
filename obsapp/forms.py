#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'label':'Kullanici Adi','placeholder': 'username'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'label':'Parola','placeholder': 'password'}))

class UpdateForm(forms.Form):
   username = forms.CharField(label='ogrenci no')
   firstname = forms.CharField(label='adi')
   lastname = forms.CharField(label='soyadi')
   email = forms.CharField(label='email')
   adres1 = forms.CharField(label='adres1')
   adres2 = forms.CharField(label='adres2')
   adres3 = forms.CharField(label='adres3')
   websayfasi = forms.CharField(label='websayfasi')

