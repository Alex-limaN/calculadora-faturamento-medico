from django.contrib import admin
from django.urls import path
from api.views import CalculadoraView # Remova a ListarConveniosView daqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/calcular/', CalculadoraView.as_view(), name='calcular'),
    # Remova também a linha que usava a ListarConveniosView, se ela existir abaixo
]