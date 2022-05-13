# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:14:33 2022

@author: Yulian
"""

# operadores logicos 
# and ( y si ademmas )
# or  ( O si no)

print(" Programa de becas año 2022")

distancia_escuala=int(input(" Digite la distancia que se encuentra de la U. "))
print(distancia_escuala)

numero_hermanos=int(input("Digite el numero de hermanos  "))
print(numero_hermanos)

salario_familiar=int(input(" Digite su salario anual  "))
print(salario_familiar)

if distancia_escuala>40 and numero_hermanos>2 and salario_familiar<=20000:
    
    print("Tiene derecho a la beca")
    
else:
    
    print("No tiene derecho a la beca")
    
    #******************************************
    
print(" Programa de becas año 2022")

distancia_escuala=int(input(" Digite la distancia que se encuentra de la U. "))
print(distancia_escuala)

numero_hermanos=int(input("Digite el numero de hermanos  "))
print(numero_hermanos)

salario_familiar=int(input(" Digite su salario anual  "))
print(salario_familiar)

if distancia_escuala>40 and numero_hermanos>2 or salario_familiar<=20000:
# Si no se cumplen las dos primera y se cumple la ultima igual queda aprobado
    
    
    print("Tiene derecho a la beca")
    
else:
    
    print("No tiene derecho a la beca")
    
    
print("****************************Ejercicios 2****************************")
    
#******************************************************************************
# in

print(" Cursos Intersemestrales  ")
print("Inteligencia artificial - sistemas expertos - programacion")

opcion=input("Asignatura escogida  ")

#Funciones
#.lower() = trasformar valor a minusculas
#.upper() = transformar valor en mayusculas

asignatura=opcion.lower() #"Convertir la informacion guardada en minuscula"

if asignatura in ("Inteligencia artificial" , "sistemas expertos","programacion"):
    print("Asignatura escogida  " + asignatura)
    
else:
    
    print("la asignatura no esta contemplada")






