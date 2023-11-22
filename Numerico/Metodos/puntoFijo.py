import re
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate as tab

class puntoFijo:

    def convertir_expresiones(expresion):
        # Añadir 'e' a la lista de funciones matemáticas
        patron = r'\b(sin|cos|tan|sqrt|exp|log|log10|e)|(\*\*|\^|\+|\-|\*|\/)'
        
        def sustituir(match):
            if match.group(1):
                if match.group(1) == 'e':
                    return 'np.e'  # Usar np.e para la constante de Euler
                return f'np.{match.group(1)}'
            elif match.group(2) == '^':
                return '**'
            else:
                return match.group(2)

        return re.sub(patron, sustituir, expresion)


    def metodo_punto_fijo(expr_f, expr_g, x_inicial, tolerancia, iteraciones_maximas):
        expr_f_converted = puntoFijo.convertir_expresiones(expr_f)
        expr_g_converted = puntoFijo.convertir_expresiones(expr_g)
        f = eval(f"lambda x: {expr_f_converted}")
        g = eval(f"lambda x: {expr_g_converted}")
        
        iteracion_actual = 0
        e_rel = float('inf')
        tabla_resultados = [[iteracion_actual, x_inicial, g(x_inicial), f(x_inicial), "NA", "NA"]]
        
        while iteracion_actual <= iteraciones_maximas:
            x_nuevo = g(x_inicial)
            error_actual = abs(x_nuevo - x_inicial)
            e_rel = error_actual / abs(x_nuevo) if x_nuevo != 0 else float('inf')
            
            tabla_resultados.append([iteracion_actual, x_inicial, g(x_inicial), f(x_inicial), error_actual, e_rel])
            
            if error_actual < tolerancia:
                break

            x_inicial = x_nuevo
            iteracion_actual += 1

        if iteracion_actual > iteraciones_maximas:
            print("Solución no encontrada, iteraciones utilizadas: ", iteracion_actual)

        

        x = np.linspace(-10, 10, 1000)
        y_f = f(x)
        y_g = g(x)
        plt.plot(x, y_f, color='red', label='f(x)')
        plt.plot(x, y_g, color='blue', label='g(x)')
        plt.axhline(0, color='black', linestyle='-', linewidth=1)
        plt.axvline(0, color='black', linestyle='-', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)/g(x)")
        plt.title("Gráfico de las Funciones")
        plt.legend()
        plt.grid(True)
        plt.show()
        return tabla_resultados


    def ejecutar(expr_f, expr_g, x_inicial, tolerancia, iteraciones_maximas):
        try:
            resultados = puntoFijo.metodo_punto_fijo(expr_f, expr_g, x_inicial, tolerancia, iteraciones_maximas)
            return resultados, None
        except Exception as e:
            return None, f"Ocurrió un error al calcular el punto fijo: {e}"    
