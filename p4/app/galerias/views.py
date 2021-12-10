from django.shortcuts import render, HttpResponse, redirect
from .forms import *

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'galerias/test.html', context)

def padre(request):
    context = {}
    return render(request, 'galerias/parent.html', context)

def ver_cuadros(request):
    cuadros = Cuadro.objects.all().order_by('nombre')
    context = {'cuadros': cuadros}
    return render(request, 'galerias/cuadros.html', context)

def crear_cuadro(request):
    form = CuadroForm()
    context = {'form': form }

    if request.method == 'POST':
        form = CuadroForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cuadros')

    else:
        form = CuadroForm()

    return render(request, 'galerias/crear_cuadro.html', context)

def modificar_cuadro(request, pk):
    cuadro = Cuadro.objects.get(id=pk)
    form = CuadroForm(instance=cuadro)
    context = {'form': form, 'error': None }

    if request.method == "POST":
        form = CuadroForm(request.POST, instance=cuadro)
        if form.is_valid():
            form.save()
            return redirect('cuadros')
        else:
            context['error'] = form.errors

    return render(request, 'galerias/crear_cuadro.html', context)

def eliminar_cuadro(request, pk):
    cuadro = Cuadro.objects.get(id=pk)
    context = {'cuadro' : cuadro}
    if request.method == "POST":
        cuadro.delete()
        return redirect('cuadros')
    return render(request,'galerias/borrar_cuadro.html', context)

def crear_galeria(request):
    form = GaleriaForm()
    context = {'form': form }

    if request.method == 'POST':
        form = GaleriaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cuadros')

    else:
        form = GaleriaForm()

    return render(request, 'galerias/crear_galeria.html', {'form': form})