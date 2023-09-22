# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 19:33:32 2023

@author: glady
"""

  # Graficar las funciones
    plt.figure(figsize=(10, 6))
    plt.plot(x, demanda, label="Función de Demanda")
    plt.plot(x, oferta, label="Función de Oferta")
    plt.axvline(precio_eq, color='r', linestyle='--', label="Precio de Equilibrio")
    plt.xlabel("Precio")
    plt.ylabel("Cantidad")
    plt.legend()
    plt.grid(True)
    plt.title("Modelo de Equilibrio de Mercado")
    plt.show()

    # Imprimir resultados
    print(f"Precio de Equilibrio: {precio_eq}")
    print(f"Exceso de Demanda: {exceso_demand}")
    print(f"Exceso de Oferta: {exceso_supply}")

if __name__ == "__main__":
    main()
Este código modulariza las funciones y te permite ingresar los parámetros de las funciones lineales y cuadráticas, calcula las funciones, encuentra el precio de equilibrio y el exceso de demanda/exceso de oferta, y luego grafica los resultados. Asegúrate de tener Matplotlib instalado para la visualización. Puedes ejecutar este código en Spyder o cualquier otro entorno de desarrollo de Python.





