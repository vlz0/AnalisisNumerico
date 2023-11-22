import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate 
import sympy as sp
import matplotlib.colors as mcolors


class newton:

    def reemplazar_funciones_matematicas(expr):
        x = sp.symbols('x')
        # Asegurarse de que 'e' se interpreta como la constante matemática
        expr_convertida = sp.sympify(expr, locals={'e': sp.exp(1)})
        expr_with_numpy = sp.lambdify(x, expr_convertida, 'numpy')
        return expr_with_numpy



    def metodo_newton(expr_f, expr_df, x0, tolerancia, max_iteraciones):
        # Convertir las expresiones en funciones ejecutables
        f = newton.reemplazar_funciones_matematicas(expr_f)
        df = newton.reemplazar_funciones_matematicas(expr_df)
        resultados = []
        e_abs = 1
        i = 0
        
        while i < max_iteraciones:
            if df(x0) == 0:
                raise ValueError("Solución no encontrada. Derivada igual a 0.")
            
            x1 = x0 - f(x0) / df(x0)
            e_abs = abs(x1 - x0)
            e_rel = e_abs / abs(x1) if x1 != 0 else float('inf')
            resultados.append([i, x1, f(x1), e_abs, e_rel])
            
            if e_abs < tolerancia:
                mensaje_resultado = "Solución encontrada en x =", x1, "en", i, "iteraciones."
                break
            
            x0 = x1
            i += 1
        
        if i >= max_iteraciones:
            print("Solución no encontrada para la tolerancia:", tolerancia, "Iteraciones utilizadas:", i)
        
        

        # Definir las funciones para graficar
        funcion = newton.reemplazar_funciones_matematicas(expr_f)

        # Graficar la función y las iteraciones
        x = np.linspace(-10, 10, 400)
        y = funcion(x)
        plt.plot(x, y, label='Función')
        colores = list(mcolors.TABLEAU_COLORS.values())

        for i, iteracion in enumerate(resultados):
            color = colores[i % len(colores)]
            plt.scatter(iteracion[1], iteracion[2], color=color, marker='x', label=f'Iteración {iteracion[0]}')

        plt.axhline(0, color='black', linestyle='-', linewidth=1)
        plt.axvline(0, color='black', linestyle='-', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Gráfico de la Función y Puntos de Iteración")
        plt.legend()
        plt.grid(True)
        plt.show()
        
        return resultados
    
    def ejecutar(expr_f, expr_df, x0, tolerancia, max_iteraciones):
        try:
            resultados = newton.metodo_newton(expr_f, expr_df, x0, tolerancia, max_iteraciones)
            return resultados, None
        except Exception as e:
            return None, f"Ocurrió un error al calcular con el método de Newton: {e}"