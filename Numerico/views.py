from django.http import HttpResponse 
from django.shortcuts import render 
from django.template import Template, Context
from .Metodos.biseccion import biseccion as biseccion_metodo
from .Metodos.puntoFijo import puntoFijo as pf
from .Metodos.ReglaFalsa import reglaFalsa as rf
from .Metodos.newton import newton as mn
from .Metodos.secante import secante as sec
from .Metodos.Multiples_Raices import MultRaices as mr
from .Metodos.SOR import SOR 
import sympy as sp


def crear_funcion(expr_str):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    return sp.lambdify(x, expr, 'numpy')


def saludo(request):  
    doc_externo=open("./Numerico/plantillas/home.html") 
    plt=Template(doc_externo.read()) 
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento )   

def biseccion_view(request):
    tabla_resultados = None
    if request.method == 'POST':
        expr_str = request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        tol = float(request.POST.get('tolerancia'))
        max_iter = int(request.POST.get('num_iteraciones'))

        f = crear_funcion(expr_str)  # Convierte la cadena en una función
        tabla_resultados = biseccion_metodo.ejecutar(f, a, b, tol, max_iter)
    return render(request, 'capitulo1/biseccion.html', {'tabla_resultados': tabla_resultados})




def PuntoFijo_view(request):
    tabla_resultados = None
    if request.method == 'POST':
        expr_f = request.POST.get('funcion_f')
        expr_g = request.POST.get('funcion_g')
        x0 = float(request.POST.get('x0'))
        tolerancia = float(request.POST.get('tolerancia'))
        num_iteraciones = int(request.POST.get('num_iteraciones'))

        tabla_resultados = pf.ejecutar(expr_f, expr_g, x0, tolerancia, num_iteraciones)
    
    return render(request, 'capitulo1/PuntoFijo.html', {'tabla_resultados': tabla_resultados})



def ReglaFalsa_view(request):
    tabla_resultados = None
    if request.method == 'POST':
        expr = request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        tol = float(request.POST.get('tolerancia'))
        n = int(request.POST.get('num_iteraciones'))

        tabla_resultados = rf.ejecutar(expr, a, b, tol, n)
    
    return render(request, 'capitulo1/ReglaFalsa.html', {'tabla_resultados': tabla_resultados})

def Newton_view(request):
    tabla_resultados = None
    if request.method == 'POST':
        expr_f = request.POST.get('funcion')
        expr_df = request.POST.get('derivada')
        x0 = float(request.POST.get('x0'))
        tolerancia = float(request.POST.get('tolerancia'))
        n = int(request.POST.get('num_iteraciones'))

        tabla_resultados = mn.ejecutar(expr_f, expr_df, x0, tolerancia, n)
    
    return render(request, 'capitulo1/Newton.html', {'tabla_resultados': tabla_resultados})

def Secante_view(request):
    tabla_resultados = None
    if request.method == 'POST':
        expr = request.POST.get('funcion')
        x_0 = float(request.POST.get('x0'))
        x_1 = float(request.POST.get('x1'))
        tolerancia = float(request.POST.get('tolerancia'))
        max_iteraciones = int(request.POST.get('num_iteraciones'))

        tabla_resultados = sec.ejecutar(expr, x_0, x_1, tolerancia, max_iteraciones)
    
    return render(request, 'capitulo1/Secante.html', {'tabla_resultados': tabla_resultados})


def RaicesMultiples_view(request):
    tabla_resultados = None
    if request.method == 'POST':
        expr_f = request.POST.get('funcion')
        expr_df = request.POST.get('derivada')
        expr_d2f = request.POST.get('derivada2')
        x0 = float(request.POST.get('x0'))
        tolerancia = float(request.POST.get('tolerancia'))
        max_iteraciones = int(request.POST.get('num_iteraciones'))

        tabla_resultados = mr.ejecutar(expr_f, expr_df, expr_d2f, x0, tolerancia, max_iteraciones)
    
    return render(request, 'capitulo1/RaicesMultiples.html', {'tabla_resultados': tabla_resultados})




def JacobiGaussSeidel(request): 
    doc_externo=open("./Numerico/plantillas/capitulo2/JacobiGaussSeidel.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento )  


def SOR_view(request):
    resultados = None

    if request.method == 'POST':
        try:
            x0 = [float(val.strip()) for val in request.POST.get('x0').split(',')]
            A = [[float(val.strip()) for val in row.split(',')] for row in request.POST.get('A').split(';')]
            b = [float(val.strip()) for val in request.POST.get('b').split(',')]
            tolerancia = float(request.POST.get('tolerancia'))
            num_iteraciones = int(request.POST.get('num_iteraciones'))
            w = float(request.POST.get('w'))

            resultados = SOR.ejecutar(x0, A, b, tolerancia, num_iteraciones, w)
        except ValueError:
            resultados = [{"iteracion": "Error", "x": "Valores inválidos", "error": ""}]

    return render(request, 'capitulo2/SOR.html', {'resultados': resultados})


def Vandermonde(request) : 
    doc_externo=open("./Numerico/plantillas/capitulo3/Vandermonde.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 


def NewtonInterpolante(request) : 
    doc_externo=open("./Numerico/plantillas/capitulo3/NewtonInterpolante.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 

def Lagrange(request) : 
    doc_externo=open("./Numerico/plantillas/capitulo3/Lagrange.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 

def Spline(request) : 
    doc_externo=open("./Numerico/plantillas/capitulo3/Spline.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 




