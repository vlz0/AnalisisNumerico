import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate 
import sympy as sp

class MultRaices:

    def reemplazar_funciones_matematicas(expr):
        x = sp.symbols('x')
        # Asegurarse de que 'e' se interpreta como la constante matemática
        expr_convertida = sp.sympify(expr, locals={'e': sp.exp(1)})
        expr_with_numpy = sp.lambdify(x, expr_convertida, 'numpy')
        return expr_with_numpy



    def raices_multiples(expr_f, expr_df, expr_d2f, x0, tolerancia, max_iteraciones):
        func_f = MultRaices.reemplazar_funciones_matematicas(expr_f)
        func_df = MultRaices.reemplazar_funciones_matematicas(expr_df)
        func_d2f = MultRaices.reemplazar_funciones_matematicas(expr_d2f)
        def funcion(x):
            return func_f(x)

        def derivada(x):
            return func_df(x)

        def derivada2(x):
            return func_d2f(x)
        
        xAnterior = x0
        fAnterior = funcion(xAnterior)
        e_abs = 1000
        i = 0
        resultados = []
        mensaje_resultado = ""
        
        while i <= max_iteraciones:
            xActual = xAnterior - fAnterior * derivada(xAnterior) / ((derivada(xAnterior))**2 - fAnterior * derivada2(xAnterior))
            fActual = funcion(xActual)
            e_abs = abs(xActual-xAnterior)
            i += 1
            xAnterior = xActual
            fAnterior = fActual
            resultados.append([i,xAnterior,funcion(xAnterior),e_abs])    
            
            if e_abs<tolerancia:
                mensaje_resultado = f"Solución encontrada en x =", xAnterior, " Iteraciones:", i-1, " Error =", e_abs
                break
        
            if i > max_iteraciones:
                print("Solucion no encontrada para la tolerancia = ", tolerancia)
            
        headers = ["Iteraciones", "Xi", "f(x)", "Error"]
            
        # Graficar la función y las iteraciones
        x = np.linspace(-10, 3, 1000)
        y = funcion(x)
        dy = derivada(x)
        d2y = derivada2(x)

        plt.plot(x, y, color='red', label='Función')
        plt.plot(x, dy, color='blue', label='Derivada')
        plt.plot(x, d2y, color='green', label='2da Derivada')
        plt.axhline(0, color='black', linestyle='-', linewidth=1)
        plt.axvline(0, color='black', linestyle='-', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)/f'(x)/f''(x)")
        plt.title(f"Gráfico de la Función: {expr_f}, su Derivada: {expr_df} y su 2da Derivada: {expr_d2f}")
        plt.legend()
        plt.grid(True)
        plt.show()

        return resultados, mensaje_resultado
    
    def ejecutar(expr_f, expr_df, expr_d2f, x0, tolerancia, max_iteraciones):
        try:
            resultados, mensaje_resultado = MultRaices.raices_multiples(expr_f, expr_df, expr_d2f, x0, tolerancia, max_iteraciones)
            return resultados, mensaje_resultado
        except Exception as e:
            return None, f"Ocurrió un error al calcular las raíces múltiples: {e}"