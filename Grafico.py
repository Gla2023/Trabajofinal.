# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:19:28 2023

@author: glady
"""
import generarcantidadproducto
import fl1
import fl2
import equilibrio
import matplotlib.pyplot as plt
import excesodedemanda
import Excesodeoferta

def graficar_oferta_demanda():
    """
    INPUT none
    OUTPUT Supply and demand graph
    type graph
        
    """
    cantidad_producto= generarcantidadproducto.cantidad_productos()
    funcionoferta= fl2.oferta()
    funciondemanda=fl1.demanda()
    x_equilibrio = equilibrio.precio_equilibrio(funciondemanda, funcionoferta)
    integral_result=excesodedemanda.calcular_area()
    integral_result2=Excesodeoferta.calcular_area()
    # Graficar la función de oferta
    plt.plot(cantidad_producto, funcionoferta, label="Oferta")

    # Graficar la función de demanda
    plt.plot(cantidad_producto, funciondemanda, label="Demanda")
      # Agregar el punto de equilibrio al gráfico
    plt.scatter(x_equilibrio[0], x_equilibrio[1], color='red', label='Punto de Equilibrio')

    plt.plot

    # Personalizar la gráfica
    plt.xlabel("Cantidad de Producto")
    plt.ylabel("Precio")
    plt.title("Funciones de Oferta y Demanda")
    plt.legend()

   
    # Anotar el área calculada en el gráfico
    plt.annotate(f'Área = {integral_result:.2f}', xy=(x_equilibrio[0], x_equilibrio[1]), xytext=(50, 50),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->'))
    plt.annotate(f'Área = {integral_result2:.2f}', xy=(x_equilibrio[0], x_equilibrio[1]), xytext=(50, 50),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->'))

    plt.xlabel('Cantidad de Producto')
    plt.ylabel('Precio')
    plt.legend()
    plt.grid(True)
    plt.show()

  
