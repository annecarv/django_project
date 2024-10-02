from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def my_view(request):
    return HttpResponse('Teste ok')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('servicos/', include('servicos.urls'))
]
