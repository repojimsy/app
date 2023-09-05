from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.lista_lecturas, name='lista_lecturas'),
    path('lecturas/list_medidor', views.lista_medidores, name='lista_medidores'),
    path('lecturas/crear/', views.crear_lectura, name='crear_lectura'),
    #path('lecturas/editar/<int:lectura_id>/', views.editar_lectura, name='editar_lectura'),
    #path('lecturas/eliminar/<int:lectura_id>/', views.eliminar_lectura, name='eliminar_lectura'),
    # Otras URLs
    path('lecturas/cargar_medidores/', views.cargar_datos_desde_excel, name='cargar_medidores'),

    # Otras URLs
]


