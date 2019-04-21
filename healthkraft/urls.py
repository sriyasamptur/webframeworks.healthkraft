from django.conf.urls import url
from . import views

urlpatterns = [
    url('atkins/', views.atkins, name='atkins'),
    url('ketogenic/', views.ketogenic, name='ketogenic'),
    url('vegan/', views.vegan, name='vegan'),
    url('vegetarian/', views.vegetarian, name='vegetarian'),
    url('raw/', views.raw, name='raw'),
    url('zone/', views.zone, name='zone'),
]