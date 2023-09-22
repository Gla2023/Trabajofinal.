# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:56:17 2023

@author: glady
"""

import pedirparametros
import generarcantidadproducto

def oferta(a_oferta, b_oferta):
  """
    INPUT a y b, type float
    OUTPUT Linear function offer
    type data array
        
    Función lineal: f(x) = ax + b
    x=cantidad de producto
    f(x)= precio
  """  
  
  cantidad_producto = generarcantidadproducto.cantidad_productos()
  a_oferta, b_oferta= pedirparametros.pedir_parametros()
  oferta = a_oferta * cantidad_producto + b_oferta
  return oferta
 