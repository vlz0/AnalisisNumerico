from django.http import HttpResponse 
from django.shortcuts import render 
from django.template import Template, Context

def saludo(request):  
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/home.html") 
    plt=Template(doc_externo.read()) 
    doc_externo.close() 
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento )   

def biseccion(request): 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo1/biseccion.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento )




def PuntoFijo(request): 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo1/PuntoFijo.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 
 

def ReglaFalsa(request) : 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo1/ReglaFalsa.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 

def Newton(request) : 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo1/Newton.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 

def Secante(request) : 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo1/Secante.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 


def RaicesMultiples(request) : 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo1/RaicesMultiples.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 




def JacobiGaussSeidel(request): 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo2/JacobiGaussSeidel.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento )  


def SOR(request): 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo2/SOR.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento )  


def Vandermonde(request) : 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo3/Vandermonde.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 
 

def NewtonInterpolante(request) : 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo3/NewtonInterpolante.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 

def Lagrange(request) : 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo3/Lagrange.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 

def Spline(request) : 
    doc_externo=open("C:/Users/encal/Desktop/final numerico/Numerico/Numerico/plantillas/capitulo3/Spline.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()  
    ctx=Context({}) 
    documento=plt.render(ctx)
    return HttpResponse(documento ) 




