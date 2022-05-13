# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:15:38 2022

@author: Yulian
"""

#********Dicionarios ***********
# Permite almacenar valores de direfentes tipos (Entero, Cadenas, decimales)

# Clave : valor

my_diccionario={"Alemania":"berlin","Colombia" :"Bogota" ,"España" :"Madrid"}
print(my_diccionario["Colombia"])

my_diccionario["Italia"] = "Roma" # Agregar elementos al diccionario
print(my_diccionario)

# Eliminar elemento del diccionario 
# Metodo del
del my_diccionario["Alemania"]
print(my_diccionario)

# Metodo Keys  muestra las claves
print(my_diccionario.keys())

# Metodo Keys  muestra las claves

print(my_diccionario.values())

# Metodo len longitud del diccionario

print(len(my_diccionario))