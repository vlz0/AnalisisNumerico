"""
URL configuration for Numerico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path 
from Numerico import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',views.saludo, name='saludo'), 
    path('biseccion/', views.biseccion_view, name = 'Biseccion'), 
    path('PuntoFijo/',views.PuntoFijo_view,name='PuntoFijo'), 
    path('ReglaFalsa/',views.ReglaFalsa_view,name='ReglaFalsa'),
    path('Newton/',views.Newton_view,name='Newton'),
    path('Secante/',views.Secante_view,name='Secante'),
    path('RaicesMultiples/',views.RaicesMultiples_view,name='RaicesMultiples'),  
    
    
    
    path('JacobiGaussSeidel/', views.JacobiGaussSeidel, name = 'JacobiGaussSeidel'),  
    path('SOR/', views.SOR, name = 'SOR'),  
    
    
    
    path('Vandermonde/', views.Vandermonde, name = 'Vandermonde'),  
    path('NewtonInterpolante/', views.NewtonInterpolante, name = 'NewtonInterpolante'),  
    path('Lagrange/', views.Lagrange, name = 'Lagrange'),  
    path('Spline/', views.Spline, name = 'Spline'),  
]
