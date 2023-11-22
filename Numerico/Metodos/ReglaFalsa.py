import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import sympy as sp

class reglaFalsa:

    def reemplazar_funciones_matematicas(expr):
        x = sp.symbols('x')
        # Asegurarse de que 'e' se interpreta como la constante matemática
        expr_convertida = sp.sympify(expr, locals={'e': sp.exp(1)})
        expr_with_numpy = sp.lambdify(x, expr_convertida, 'numpy')
        return expr_with_numpy
    
    def false_position_method(expr, a, b, tol, n):
        func = reglaFalsa.reemplazar_funciones_matematicas(expr)
        f = lambda x: func(x)

        if f(a) * f(b) >= 0:
            print("El intervalo no cambia de signo.")
            return

        resultados = []
        e_abs = abs(b - a)
        c = a - (f(a) * (b - a)) / (f(b) - f(a))

        for i in range(1, n + 1):
            if f(c) * f(a) < 0:
                b = c
            else:
                a = c

            c_new = a - (f(a) * (b - a)) / (f(b) - f(a))
            e_abs = abs(c_new - c)
            e_rel = e_abs / abs(c_new) if c_new != 0 else float('inf')
            resultados.append([i, a, b, c, f(c), e_abs, e_rel])

            if e_abs < tol:
                break

            c = c_new

        if i == n:
            print("Solución no encontrada para la tolerancia de:", tol, "--- Iteraciones Utilizadas:", n)

        

        # Gráfico
        x = np.linspace(-10, 10, 1000)
        y = f(x)

        plt.plot(x, y, color='red', label='Función')
        plt.axhline(0, color='black', linestyle='-', linewidth=1)
        plt.axvline(0, color='black', linestyle='-', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title(f"Gráfico de la Función: {expr}")
        plt.legend()
        plt.grid(True)
        plt.show()
        return resultados

    def ejecutar(expr, a, b, tol, n):
        try:
            resultados = reglaFalsa.false_position_method(expr, a, b, tol, n)
            return resultados, None
        except Exception as e:
            return None, f"Ocurrió un error al calcular la regla falsa: {e}"