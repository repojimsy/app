from django.shortcuts import render, get_object_or_404, redirect
from .models import Medidor, Lectura
#import pandas as pd
from .forms import UploadExcelForm
from django.forms import formset_factory
from django.http import JsonResponse
from .forms import LecturaForm
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.views.generic import CreateView

@login_required
def lista_lecturas(request):
    lecturas = Lectura.objects.all()
    title = 'Listado de Lecturas'
    return render(request, 'lecturas/lista_lecturas.html', {'lecturas': lecturas, 'title':title})

@login_required
def lista_medidores(request):
    title = 'Listado de Usuarios'
    medidor = Medidor.objects.all()
    return render(request, 'lecturas/lista_medidores.html', {'medidor': medidor, 'title':title})


@login_required
def crear_lectura(request):
    title = 'Creación de una Lectura'
    if request.method == 'POST':
        form = LecturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_lecturas')
    else:
        form = LecturaForm()
    return render(request, 'lecturas/crear_lectura.html', {'form': form, 'title':title})

@login_required
def editar_lectura(request, lectura_id):
    lectura = get_object_or_404(Lectura, pk=lectura_id)
    if request.method == 'POST':
        form = LecturaForm(request.POST, instance=lectura)
        if form.is_valid():
            form.save()
            return redirect('lista_lecturas')
    else:
        form = LecturaForm(instance=lectura)
    return render(request, 'lecturas/editar_lectura.html', {'form': form, 'lectura': lectura})

def eliminar_lectura(request, lectura_id):
    lectura = get_object_or_404(Lectura, pk=lectura_id)
    if request.method == 'POST':
        lectura.delete()
        return redirect('lista_lecturas')
    return render(request, 'lecturas/confirmar_eliminacion.html', {'lectura': lectura})


@login_required
def cargar_datos_desde_excel(request):
    title = 'Agregar Usuarios'
    if request.method == 'POST' and request.FILES['archivo_excel']:
        archivo_excel = request.FILES['archivo_excel']
        if archivo_excel.name.endswith('.xlsx'):
            df = pd.read_excel(archivo_excel)
            for index, row in df.iterrows():
                # Comprueba si ya existe un medidor con el mismo número de serie
                if not Medidor.objects.filter(suministro=row['suministro']).exists():
                    Medidor.objects.create(
                        nombres=row['nombres'],
                        direccion=row['direccion'],
                        suministro=row['suministro'],
                        nserie=row['nserie'],
                        marcaMedidor=row['marcaMedidor'],
                        tarifa=row['tarifa'],
                        fases=row['fases'],
                        sed=row['sed']
                    )

            return redirect('lista_medidores')  # Redirecciona a la lista de medidores o la página que desees
    return render(request, 'lecturas/cargar_medidores.html',{'title':title})






