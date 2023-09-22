# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 00:07:05 2023

@author: glady
"""
import fl1
import fl2
import excesodedemanda
import equilibrio
def main():
    import Preciodeequilibrio
import equilibriocuadratica

def main():
    print("Vamos a modelizar la oferta y la demanda")
    Eleccion = input("Elige una opción:\n"
                     "l para función lineal\n"
                     "c para función cuadrática\n"
                     ":......")

    if Eleccion == "l":
                        Preciodeequilibrio()
        
       
    elif Eleccion == "c":
                        equilibriocuadratica()
       
    else:
        print("Elección inválida")


        if __name__ == "__main__":
            result = main()
    print(result)





    
    