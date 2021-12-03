from django.shortcuts import render, HttpResponse

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
    context = {}
    return render(request, 'galerias/cuadros.html', context)