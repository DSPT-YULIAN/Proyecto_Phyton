# -*- coding: utf-8 -*-
"""
Created on Tue May 10 09:28:34 2022

@author: Yulian
"""
##################### Listas #####################

#indice [0] [1] [2] [3] positivo
#indice [-4] [-3] [-2] [-1] negativo no tiene en cuenta el 0

# Sintaxis

# Nombrelista=[elem1,elem2,elem3]

milista=["Yulian","Nataly","Dylan", "Nina","Kiara"] # texto entre comillas

print(milista[:]) # (:) para imprimir lista completa

print(milista[3])  # Imprimir indice seleccionado --+ de izquierda a derecha
print(milista[-3]) # Imprimir indice seleccionado - - de derecha a izquierda

print(milista[0:3]) # Porcion de lista 
print(milista[:3]) # el mismo resultado izquiera a derecha
print(milista[3:]) # el mismo resultado derecha izquiera

# Agregar elementos al final de la lista
# Funcion .append
# nombrelista.append("titi")

milista.append("titi")

print(milista[:])

# Agregar elementos en un punto de la lista
# Funcion .insert
# nombrelista.insert("titi")

milista.insert(2, "cat")

print(milista[:])

# Agregar varios elementos a las lista
# Funcion .extend ([])
# nombrelista.extend(["titi"])

milista.extend(["perro", "gato","conejo"])
print(milista[:])

# Conocer el indice
# Funcion .index ()
# nombrelista.index("Dylan")

print(milista.index("Dylan"))

# Comprobar si el elemento esta en la lista

print("Nataly" in milista)
print("Ana" in milista)

# Eliminar elementos de una lista
# Funcion.remove()
#nombrelista,remove()

milista.remove("cat")
print(milista[:])

# Eliminar ultimo elemento de las lista
# Funcion.pop()
#nombrelista,pop()

milista.pop()
print(milista[:])

#unir listas 


milista2=["pescado", "tiburon","delfin",1]
milista3=["pajaro" , "aguila" ,"colibri",2 ]

lista4=milista+milista2+milista3
print(lista4[:])

# Repetidor (*)

milista2=["pescado", "tiburon","delfin",1] * 5 
print(milista2[:])

