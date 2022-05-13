# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:47:30 2022

@author: Yulian
"""
#******************Condicioneles********
# Control de flujo

#************************* IF (SI)************************************

# Condiciones   
# verdadero / true  cumple
# Falso / False no cumple

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="no pasa"
    return valoracion

print(evaluacion(4))

print ("Evaluacion de notas de alumnos")

nota_alumno=input("ingrese la nota del alumno:  ")      # Variable ingresada por teclado

def evaluacion(nota):                  #funcionm
    valoracion="aprobado"              #instruccion
    if nota<5:                         #condicional
        valoracion="no pasa"           #instruccion
    return valoracion                  #retorna
 
print(evaluacion(int(nota_alumno)))   #funcion int trasforma texto de input a #



