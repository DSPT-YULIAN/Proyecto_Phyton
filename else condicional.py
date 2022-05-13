# -*- coding: utf-8 -*-
"""
Created on Thu May 12 22:00:35 2022

@author: Yulian
"""
print("Verificacion de acceso")

#int(input()) transformar texto de entrada con la funcion inpunt a entero int
edad_usuario=int(input("Introduzca su edad  ")) # declaracion de variable

if edad_usuario<18:
    print("No puede pasar")
else:
    print("puede pasar")

print("Finalizado")

#******elif******

print("Verificacion de acceso con doble condicion")

edad_usuario=int(input("Introduzca su edad  ")) # declaracion de variable
if edad_usuario<18:
    print("No puede pasar")
    
elif edad_usuario>100:         # valida toda la estructura ( if - elif)
    print("edad incorrecta")
    
else:
    print("puede pasar") # cuando no se cumple if-elif entra 

print("Finalizado")