from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('atualiza_cliente/', views.att_clientes, name="atualiza_cliente"),
    path('update_cliente/<int:id>', views.update_cliente, name="update_cliente"),
    path('atualiza_carro/<int:id>', views.att_carro, name="atualiza_carro"),
    path('excluir_carro/<int:id>', views.excluir_carro, name="excluir_carro")
]