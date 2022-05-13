# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##################### Funciones #####################

#funciones sin parametros
# palabra reservada para llamar funciones "def"

print("funcion sin parametros")
def suma ():    # Declaracion
    print("Suma de numeros")
    num1=5      # cuerpo funcion
    num2=7
    print(num1+num2)

suma()          # llamada funcion

# funciones con paramentros 
print("funcion con parametros")
def suma (numero1,numero2):
    print(numero1+numero2)

suma(10,10)


# Funcion con return
# solicita los datos por consola
print("funcion con return")
def suma (numer1,numer2):
    resultado=numer1+numer2
    return(resultado)
print(suma(5,7))









