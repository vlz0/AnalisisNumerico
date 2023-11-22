import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import sympy as sp

class biseccion:
    
    def reemplazar_funciones_matematicas(expr):
        x = sp.symbols('x') 
        expr_convertida = sp.sympify(expr, locals={'e': sp.exp(1)})
        expr_with_numpy = sp.lambdify(x, expr_convertida, 'numpy')
        return expr_with_numpy
    
    def biseccion(f, a, b, tol, max_iter):
        resultados = []
        mensaje_resultado = ""
        if f(a) * f(b) >= 0:
            mensaje_resultado = "El intervalo [a,b] no cambia de signo"
            return resultados, mensaje_resultado

        e_abs = abs(b - a)
        c_t = a  # Inicializar c_t para calcular el error relativo en la primera iteración
        i = 1
        while i <= max_iter and e_abs > tol:
            a_ant = a
            c = (a + b) / 2
            e_rel = abs(c - c_t) / abs(c) if c != 0 else float('inf')
            c_t = c

            if f(c) == 0:
                mensaje_resultado = f"Solución encontrada en x = {c}, en la iteración {i}."
                return mensaje_resultado

            if f(a) * f(c) < 0:
                b = c
            else:
                a = c

            e_abs = abs(b - a)
            resultados.append([i, a_ant, c, b, f(c), e_abs, e_rel])

            if e_abs < tol:
                mensaje_resultado = f"Solución encontrada en x = {c}, en la iteración {i}."
                break
            i += 1

        if i > max_iter:
            mensaje_resultado= "Solucion no encontrada para la tolerancia especificada"

        x = np.linspace(-10, 10, 1000)
        y = f(x)

        plt.plot(x, y, color='red', label='Función')
        plt.axhline(0, color='black', linestyle='-', linewidth=1)
        plt.axvline(0, color='black', linestyle='-', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Gráfico de la Función")
        plt.legend()
        plt.grid(True)
        plt.show()
        return resultados, mensaje_resultado
        

    def ejecutar(f, a, b, tol, max_iter):
        try:
            resultados, mensaje_resultado = biseccion.biseccion(f, a, b, tol, max_iter)
            return resultados, mensaje_resultado
        except Exception as e:
            return None, f"Ocurrió un error al calcular la biseccion: {e}"