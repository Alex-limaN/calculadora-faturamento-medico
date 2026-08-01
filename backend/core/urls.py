from django.contrib import admin
from django.urls import path
from api.views import CalculadoraView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/calcular/', CalculadoraView.as_view(), name='calcular'), 
]