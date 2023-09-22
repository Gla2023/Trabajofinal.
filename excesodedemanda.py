# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:21:58 2023

@author: glady
"""
import equilibrio
import fl1
from scipy.integrate import quad

def calcular_area():
    """ 
   Input
   output
   type
    """
    x_equilibrio = equilibrio()
    f_x = fl1()
    g_x= equilibrio()
    h= f_x - g_x
    integral_result = quad(h, 0, x_equilibrio)
    return  integral_result

    print("El valor de la integral de h(x)", integral_result)

 
  