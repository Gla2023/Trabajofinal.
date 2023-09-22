# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 00:02:47 2023

@author: glady
"""
import fl1
import fl2
import generarcantidadproducto

def precio_equilibrio(demanda, oferta):
    """
    INPUT none
    OUTPUT precio de equilibrio de las funciones oferta y demanda ingresadas.
    type data float
        
    Interseccion: fl1 = fl2
    """
    demanda=fl1.demanda()
    oferta=fl2.oferta()
    cantidad_producto= generarcantidadproducto()
    for i in range(len(cantidad_producto)):
        if demanda[i] == oferta[i]:
            punto_equilibrio = (cantidad_producto[i], demanda[i])
            break
    return punto_equilibrio