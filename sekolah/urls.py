
from django.conf.urls import url
from django.contrib import admin
from sekolah import views

urlpatterns = [
    url(r'^guru/list/', view=views.daftar_guru, name='daftar_guru'),
    url(r'^guru/list/', view=views.api_daftar_guru, name='api_daftar_guru')
]