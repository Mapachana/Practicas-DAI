"""composeexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# galerias/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_template', views.test_template, name="test_template"),
    path('padre', views.padre, name="padre"),
    path('cuadros', views.ver_cuadros, name="cuadros"),
    path('cuadro/crear', views.crear_cuadro, name="crear_cuadro"),
    path('cuadro/modificar/<str:pk>', views.modificar_cuadro, name="modificar_cuadro"),
    path('cuadro/eliminar/<str:pk>', views.eliminar_cuadro, name="eliminar_cuadro"),
    path('galeria/crear', views.crear_galeria, name="crear_galeria")
]


