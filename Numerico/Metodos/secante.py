import re
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate as tab

class secante:

    def actualizar_expresion(expresion):
        patron = r'\b(sin|cos|tan|sqrt|exp|log|log10)|(\*\*|\^|\+|\-|\*|\/)'
        
        
        def sustituir(correspondencia):
            if correspondencia.group(1):
                return f'np.{correspondencia.group(1)}'
            elif correspondencia.group(2) == '^':
                return '**'
            else:
                return correspondencia.group(2)

        return re.sub(patron, sustituir, expresion)


    def metodo_secante(expr, x_0, x_1, tolerancia, max_iteraciones):
        expr_np = secante.actualizar_expresion(expr)
        func = eval(f"lambda x: {expr_np}")
        error_abs = abs(x_1 - x_0)
        iteracion = 2
        tabla_resultados = [[0, x_0, func(x_0), "", ""]]
        tabla_resultados.append([1, x_1, func(x_1), "", ""])

        while iteracion <= max_iteraciones:
            if func(x_1) == func(x_0):
                print('Solución no encontrada (error en los valores iniciales)')
                break
            
            x_2 = x_1 - ((func(x_1) * (x_1 - x_0)) / (func(x_1) - func(x_0)))
            error_abs = abs(x_1 - x_2)
            error_rel = error_abs / abs(x_2) if x_2 != 0 else float('inf')

            tabla_resultados.append([iteracion, x_2, func(x_2), error_abs, error_rel]) 
            
            if error_abs < tolerancia:
                break
            
            x_0 = x_1
            x_1 = x_2
            iteracion += 1
        
        
        if iteracion < max_iteraciones:
            print('Aproximación de la raíz encontrada en x = ', x_2)
        

        if iteracion < max_iteraciones:
            print('Aproximación de la raíz encontrada en x = ', x_2)

        x = np.linspace(-10, 10, 1000)
        y = func(x)

        plt.plot(x, y, color='red', label='Función')
        plt.axhline(0, color='black', linestyle='-', linewidth=1)
        plt.axvline(0, color='black', linestyle='-', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title(f"Gráfico de la Función: {expr}")
        plt.legend()
        plt.grid(True)
        plt.show()
        
        return tabla_resultados
    
    def ejecutar(expr, x_0, x_1, tolerancia, max_iteraciones):
        return secante.metodo_secante(expr, x_0, x_1, tolerancia, max_iteraciones)


