# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:54:52 2023

@author: glady
"""
import generarcantidadproducto
import pedirparametros
def demanda(a, b):
    """
    INPUT none
    OUTPUT Demand linear function
    type data: array
        
    Función lineal: f(x) = ax + b
    x=cantidad de producto
    f(x)= precio
    """
    cantidad_producto=generarcantidadproducto()
    a_demanda, b_demanda= pedirparametros()
    demanda = a_demanda * cantidad_producto + b_demanda
    return demanda
