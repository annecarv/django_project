from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('novo_servico/', views.novo_servico, name='novo_servico'),
    path('listar_servicos/', views.listar_servicos, name='listar_servicos'),
    path('servico/<str:protocolo>/', views.servico, name='servico'),
    path('gerar_os/<str:protocolo>/', views.gerar_os, name='gerar_os')
]