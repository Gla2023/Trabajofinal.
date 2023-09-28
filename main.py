# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:21:05 2023

@author: glady
"""
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from matplotlib.patches import Polygon

# Función para calcular el punto de equilibrio
def punto_equilibrio(oferta, demanda):
    x = sp.Symbol('x')
    
    # Definir una función para encontrar la raíz positiva más cercana
    def equilibrio_func(x):
        return oferta.subs('x', x) - demanda.subs('x', x)
    
    # Encontrar el punto de equilibrio usando brentq
    equilibrio = brentq(equilibrio_func, 0, 100)  # Ajusta el rango según tus necesidades
    
    return equilibrio

# Función para calcular la integral entre a y b de una función f(x)
def integral(f, a, b):
    x = sp.Symbol('x')
    integral = sp.integrate(f, (x, a, b))
    return integral

# Pedir al usuario las funciones de oferta y demanda
oferta_str = input("Ingrese la función de oferta (ejemplo: 42*x): ")
demanda_str = input("Ingrese la función de demanda (ejemplo: 1000-0.4*x*x): ")

x = sp.Symbol('x')
oferta = sp.sympify(oferta_str)
demanda = sp.sympify(demanda_str)

# Calcular el punto de equilibrio
equilibrio = punto_equilibrio(oferta, demanda)
print (f"El precio de equilibrio es {equilibrio}")

# Aserción para verificar el cálculo del punto de equilibrio
assert abs(equilibrio - 19.999999999999996) < 1e-10, f"Error en el punto de equilibrio: {equilibrio}"

# Calcular el superávit de los consumidores (exceso de demanda)
exceso_demanda = abs(integral(demanda, 0, equilibrio) - (equilibrio * demanda.subs(x, equilibrio)))
print(f"El exceso de demanda es {exceso_demanda}")
# Calcular el superávit de los productores (exceso de oferta)
exceso_oferta = abs((equilibrio * oferta.subs(x, equilibrio)) - integral(oferta, 0, equilibrio))
print(f"El exceso de oferta es {exceso_oferta}")
# Aserción para verificar el cálculo del superávit de los consumidores
assert abs(exceso_demanda - 2133.33333333333) < 1e-10, f"Error en el superávit de los consumidores: {exceso_demanda}"

# Aserción para verificar el cálculo del superávit de los productores
assert abs(exceso_oferta - 8400.00000000000) < 1e-10, f"Error en el superávit de los productores: {exceso_oferta}"

# Crear un rango de valores de x para graficar
x_values = np.linspace(0, equilibrio * 2, 400)
oferta_values = [oferta.subs(x, val) for val in x_values]
demanda_values = [demanda.subs(x, val) for val in x_values]

# Crear áreas sombreadas para el superávit de los consumidores y productores
fig, ax = plt.subplots()
ax.plot(x_values, oferta_values, label='Oferta', color='blue')
ax.plot(x_values, demanda_values, label='Demanda', color='red')
ax.scatter(equilibrio, oferta.subs(x, equilibrio), color='green', label='Equilibrio')

# Área sombreada para el superávit de los consumidores (debajo de la curva de demanda)
polygon_points = [(x_val, demanda.subs(x, x_val)) for x_val in x_values if x_val <= equilibrio]
polygon_points.append((equilibrio, oferta.subs(x, equilibrio)))
polygon = Polygon(polygon_points, closed=True, alpha=0.2, facecolor='orange', edgecolor='none')
ax.add_patch(polygon)

# Área sombreada para el superávit de los productores (debajo de la curva de oferta)
polygon_points = [(x_val, oferta.subs(x, x_val)) for x_val in x_values if x_val <= equilibrio]
polygon_points.append((equilibrio, demanda.subs(x, equilibrio)))
polygon = Polygon(polygon_points, closed=True, alpha=0.2, facecolor='purple', edgecolor='none')
ax.add_patch(polygon)

ax.set_xlabel('Cantidad')
ax.set_ylabel('Precio')
ax.legend()
ax.grid()
plt.show()
