from django.shortcuts import render, HttpResponse, redirect
from .forms import *

# Create your views here.

def index(request):
    '''
    Funcion con la direccion home (pagina principal de la aplicacion)
    '''
    cuadros = Cuadro.objects.all().order_by('nombre')
    context = {'cuadros': cuadros}
    return render(request, 'galerias/cuadros.html', context)

def helloworld(request):
    '''
    Hello world en django
    '''
    return HttpResponse('Hello World!')

def test_template(request):
    '''
    Metodo de prueba de plantilla
    '''
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'galerias/test.html', context)

def padre(request):
    '''
    Funcion para renderizar la plantilla de la que heredan todas las paginas
    '''
    context = {}
    return render(request, 'galerias/parent.html', context)

def ver_cuadros(request):
    '''
    Pagina que muestra todos los cuadros ya creados, con enlaces a crear, modificar y borrar
    '''
    cuadros = Cuadro.objects.all().order_by('nombre')
    context = {'cuadros': cuadros}
    return render(request, 'galerias/cuadros.html', context)

def crear_cuadro(request):
    '''
    Funcion para crear un cuadro
    '''
    form = CuadroForm()
    context = {'form': form }

    if request.method == 'POST':
        form = CuadroForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cuadros')
    else:
        form = CuadroForm()

    return render(request, 'galerias/crear_cuadro.html', context)

def modificar_cuadro(request, pk):
    '''
    Funcion para modificar un cuadro existente
    '''
    try:
        cuadro = Cuadro.objects.get(id=pk)
    except:
        return redirect('cuadros')

    form = CuadroForm(instance=cuadro)
    context = {'form': form, 'error': None }

    if request.method == "POST":
        form = CuadroForm(request.POST, request.FILES, instance=cuadro)
        if form.is_valid():
            form.save()
            return redirect('cuadros')
        else:
            context['error'] = form.errors

    return render(request, 'galerias/crear_cuadro.html', context)

def eliminar_cuadro(request, pk):
    '''
    Funcion para eliminar un cuadro existente
    '''
    try:
        cuadro = Cuadro.objects.get(id=pk)
    except:
        return redirect('cuadros')

    context = {'cuadro' : cuadro}
    if request.method == "POST":
        cuadro.delete()
        return redirect('cuadros')

    return render(request,'galerias/borrar_cuadro.html', context)

def ver_galerias(request):
    '''
    Funcion para la pagina que muestra todas las galerias, con enlaces a crear, modificar y borrar galerias
    '''
    galerias = Galeria.objects.all().order_by('nombre')
    context = {'galerias': galerias}
    return render(request, 'galerias/galerias.html', context)


def crear_galeria(request):
    '''
    Funcion para crear una nueva galeria
    '''
    form = GaleriaForm()
    context = {'form': form }

    if request.method == 'POST':
        form = GaleriaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('galerias')

    else:
        form = GaleriaForm()

    return render(request, 'galerias/crear_galeria.html', context)

def modificar_galeria(request, pk):
    '''
    Funcion para modificar una galeria existente
    '''
    try:
        galeria = Galeria.objects.get(id=pk)
    except:
        return redirect('galerias')
    
    form = GaleriaForm(instance=galeria)
    context = {'form': form, 'error': None }

    if request.method == "POST":
        form = GaleriaForm(request.POST, instance=galeria)
        if form.is_valid():
            form.save()
            return redirect('galerias')
        else:
            context['error'] = form.errors

    return render(request, 'galerias/crear_galeria.html', context)

def eliminar_galeria(request, pk):
    '''
    Funcion para eliminar una galeria existente
    '''
    try:
        galeria = Galeria.objects.get(id=pk)
    except:
        return redirect('galerias')
    
    context = {'galeria' : galeria}
    if request.method == "POST":
        galeria.delete()
        return redirect('galerias')
        
    return render(request,'galerias/borrar_galeria.html', context)
