from django.http import HttpResponse 
from django.shortcuts import render 
from django.template import Template, Context
from .Metodos.biseccion import biseccion as bis
from .Metodos.puntoFijo import puntoFijo as pf
from .Metodos.ReglaFalsa import reglaFalsa as rf
from .Metodos.newton import newton as mn
from .Metodos.secante import secante as sec
from .Metodos.Multiples_Raices import MultRaices as mr
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
    mensaje_error = None
    mensaje_resultado = None
    if request.method == 'POST':
        try:
            expr_str = request.POST.get('funcion')
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            tol = float(request.POST.get('tolerancia'))
            max_iter = int(request.POST.get('num_iteraciones'))

            f = crear_funcion(expr_str)  # Convierte la cadena en una función
            tabla_resultados, mensaje_resultado = bis.ejecutar(f, a, b, tol, max_iter)
        except Exception as e:
            mensaje_error = f"Ocurrio un error al procesar la funcion: {e}"

    return render(request, 'capitulo1/biseccion.html', {
        'tabla_resultados': tabla_resultados,
        'mensaje_error' : mensaje_error,
        'mensaje_resultado': mensaje_resultado
        })




def PuntoFijo_view(request):
    tabla_resultados = None
    mensaje_error = None
    if request.method == 'POST':
        try:
            expr_f = request.POST.get('funcion_f')
            expr_g = request.POST.get('funcion_g')
            x0 = float(request.POST.get('x0'))
            tolerancia = float(request.POST.get('tolerancia'))
            num_iteraciones = int(request.POST.get('num_iteraciones'))

            tabla_resultados, mensaje_error = pf.ejecutar(expr_f, expr_g, x0, tolerancia, num_iteraciones)
        except Exception as e:
            mensaje_error = f"Ocurrió un error en la vista: {e}"

    return render(request, 'capitulo1/PuntoFijo.html', {
        'tabla_resultados': tabla_resultados,
        'mensaje_error': mensaje_error
    })



def ReglaFalsa_view(request):
    tabla_resultados = None
    mensaje_error = None
    if request.method == 'POST':
        try:
            expr = request.POST.get('funcion')
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            tol = float(request.POST.get('tolerancia'))
            n = int(request.POST.get('num_iteraciones'))

            tabla_resultados, mensaje_error = rf.ejecutar(expr, a, b, tol, n)
        except Exception as e:
            mensaje_error = f"Ocurrió un error en la vista: {e}"

    return render(request, 'capitulo1/ReglaFalsa.html', {
        'tabla_resultados': tabla_resultados,
        'mensaje_error': mensaje_error
    })

def Newton_view(request):
    tabla_resultados = None
    mensaje_error = None
    if request.method == 'POST':
        try:
            expr_f = request.POST.get('funcion')
            expr_df = request.POST.get('derivada')
            x0 = float(request.POST.get('x0'))
            tolerancia = float(request.POST.get('tolerancia'))
            n = int(request.POST.get('num_iteraciones'))

            tabla_resultados, mensaje_error = mn.ejecutar(expr_f, expr_df, x0, tolerancia, n)
        except Exception as e:
            mensaje_error = f"Ocurrió un error en la vista: {e}"

    return render(request, 'capitulo1/Newton.html', {
        'tabla_resultados': tabla_resultados,
        'mensaje_error': mensaje_error
    })

def Secante_view(request):
    tabla_resultados = None
    mensaje_error = None
    if request.method == 'POST':
        try:
            expr = request.POST.get('funcion')
            x_0 = float(request.POST.get('x0'))
            x_1 = float(request.POST.get('x1'))
            tolerancia = float(request.POST.get('tolerancia'))
            max_iteraciones = int(request.POST.get('num_iteraciones'))

            tabla_resultados, mensaje_error = sec.ejecutar(expr, x_0, x_1, tolerancia, max_iteraciones)
        except Exception as e:
            mensaje_error = f"Ocurrió un error en la vista: {e}"

    return render(request, 'capitulo1/Secante.html', {
        'tabla_resultados': tabla_resultados,
        'mensaje_error': mensaje_error
    })


def RaicesMultiples_view(request):
    tabla_resultados = None
    mensaje_error = None
    mensaje_resultado = None
    if request.method == 'POST':
        try:
            expr_f = request.POST.get('funcion')
            expr_df = request.POST.get('derivada')
            expr_d2f = request.POST.get('derivada2')
            x0 = float(request.POST.get('x0'))
            tolerancia = float(request.POST.get('tolerancia'))
            max_iteraciones = int(request.POST.get('num_iteraciones'))

            tabla_resultados, mensaje_resultado = mr.ejecutar(expr_f, expr_df, expr_d2f, x0, tolerancia, max_iteraciones)
        except Exception as e:
            mensaje_error = f"Ocurrió un error en la vista: {e}"

    return render(request, 'capitulo1/RaicesMultiples.html', {
        'tabla_resultados': tabla_resultados,
        'mensaje_error': mensaje_error,
        'mensaje_resultado': mensaje_resultado
    })




def JacobiGaussSeidel(request): 
    doc_externo=open("./Numerico/plantillas/capitulo2/JacobiGaussSeidel.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento )  


def SOR(request): 
    doc_externo=open("./Numerico/plantillas/capitulo2/SOR.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento )  


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




