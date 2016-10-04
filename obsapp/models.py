from django.db import models
from django.contrib.auth.models import User

class KimlikBilgileri(models.Model):
    kullanici = models.OneToOneField(User)
    tcNo = models.CharField(max_length=11,primary_key=True)
    yas = models.IntegerField()
    dogumTarihi = models.DateField()
    adres1 = models.CharField(max_length=30)
    adres2 = models.CharField(max_length=30)
    adres3 = models.CharField(max_length=30)
    websayfasi = models.CharField(max_length=30)
    def __unicode__(self):
        return tcNo

class Ders(models.Model):
    dersKodu = models.CharField(max_length=5,primary_key=True)
    dersAdi = models.CharField(max_length=30)
    dersSaati = models.IntegerField()
    dersKredisi = models.FloatField()
    def __unicode__(self):
        return dersKodu

class OgretimGorevlisi(models.Model):
    kimlikBilgisi = models.ForeignKey(KimlikBilgileri)
    unvan = models.CharField(max_length=20)
    def __unicode__(self):
        return sicilNo
class AcilanDers(models.Model):
    dersKodu = models.ForeignKey(Ders)
    ogretmen = models.ForeignKey(OgretimGorevlisi)
    class Meta:
        unique_together=('dersKodu','ogretmen')
    def __unicode__(self):
        return dersKodu

class Danisman(models.Model):
    ogretmenId = models.ForeignKey(OgretimGorevlisi,primary_key=True)
    sinif = models.IntegerField()
    class Meta:
        unique_together=('ogretmenId','sinif')
    def __unicode__(self):
        return ogretmenId

class Bolum(models.Model):
    bolumKodu = models.CharField(max_length=5,primary_key=True)
    bolumAdi = models.CharField(max_length=30)
    bolumBaskani = models.ForeignKey(OgretimGorevlisi)
    def __unicode__(self):
        return bolumKodu
class Ogrenci(models.Model):
    kimlikBilgisi = models.ForeignKey(KimlikBilgileri)
    sinif = models.IntegerField()
    danisman = models.ForeignKey(Danisman)
    bolum = models.ManyToManyField(Bolum,through='BolumKayit')
    def __unicode__(self):
        return ogrenciNo


class AldigiDersler(models.Model):
    ogrenciNo = models.ForeignKey(Ogrenci,primary_key=True)
    dersKodu = models.ForeignKey(Ders)
    aldigiNot = models.CharField(max_length=2)
    devamsizlik = models.IntegerField()
    class Meta:
        unique_together=('ogrenciNo','dersKodu')
    def __unicode_(self):
        return dersKodu


class BolumKayit(models.Model):
    ogrenciNo = models.ForeignKey(Ogrenci,primary_key=True)
    bolum = models.ForeignKey(Bolum)
    kayitYili = models.DateField()
    class Meta:
        unique_together=('ogrenciNo','bolum')
    def __unicode__(self):
        return bolum
class OgrenciMezuniyet:
    ogrenciNo = models.ForeignKey(Ogrenci,primary_key=True)
    mezuniyet = models.CharField(max_length=30)
    yil = models.DateField()
    derece = models.FloatField()
    def __unicode__(self):
        return ogrenciNo


