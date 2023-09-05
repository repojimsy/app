from django.contrib import admin
from core.lecturas.models import Medidor, Lectura

#admin.site.register(Medidor)
#admin.site.register(Lectura)

@admin.register(Medidor)
class Medidoradmin(admin.ModelAdmin):
    list_display = ('nombres', 'suministro', 'sed')
    ordering = ('suministro',)
    search_fields = ('nombres', 'suministro', 'sed')

@admin.register(Lectura)
class Lecturaadmin(admin.ModelAdmin):
    list_display = ('medidor', 'usuario', 'valor_lectura')
    ordering = ('suministro',)
    search_fields = ('usuario', 'suministro')