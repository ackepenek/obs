# Create your views here.

from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from forms import LoginForm,UpdateForm
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.models import User
from models import KimlikBilgileri

from django.core.urlresolvers import reverse
def update(request):
    kimlikbil = KimlikBilgileri.objects.get(kullanici=request.user.id)
    ogrenci = request.user
    data={'username':ogrenci.username,'firstname':ogrenci.first_name,'lastname':ogrenci.last_name,'email':ogrenci.email,'adres1':kimlikbil.adres1,'adres2':kimlikbil.adres2,'adres3':kimlikbil.adres3,'websayfasi':kimlikbil.websayfasi}
    form = UpdateForm(data)
    return render_to_response('ogrenci/update.html',{'form':UpdateForm()})
def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    return render_to_response("ogrenci/index.html")
def logout(request):
    user_logout(request)
    return HttpResponseRedirect(reverse("loginuser"))
def login(request):

    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            ogrenci = authenticate(username=username,password=password)
            if ogrenci is not None:
                auth_login(request,ogrenci)
            else:
                return render_to_response('ogrenci/login.html',{'title':'Login', 'form':LoginForm()})
            return HttpResponseRedirect(reverse("index"))
        else:
            return render_to_response('ogrenci/login.html',{'title':'Login', 'form':LoginForm()})
    else:
        return render_to_response('ogrenci/login.html',{'title':'Login', 'form':LoginForm()})

