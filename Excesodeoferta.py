# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:10:24 2023

@author: glady
"""

import equilibrio
import fl1
import fl2
from scipy.integrate import quad

def calcular_area():
    """ 
   Input
   output
   type
    """
    demanda=fl1.demanda()
    oferta= fl2.oferta()
    x_equilibrio = equilibrio.precio_equilibrio(demanda, oferta)
    f_x = equilibrio.precio_equilibrio(x_equilibrio[0])
    g_x= oferta(x_equilibrio[0])
    h= f_x - g_x
    integral_result2 = quad(h, 0, x_equilibrio[0])
    return  integral_result2