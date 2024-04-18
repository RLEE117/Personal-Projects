# Curso de python
# Autor: Roberto Lee
# Fecha: 17-04-2024
# ejemplo de control de flujo condicional,
# bifurcacion en el cual se utiliza lo siguiente:
# if (condicion):
#     acciones por realizar
# else:
#     acciones por realizar
# Version 1
##########################

# caracteres especiales
#-*- coding: utf-8 -*-

# determinar cual numero es mayor

# captura de datos
valor_1 = int(input("Ingrese el primer número >> "))
valor_2 = int(input("Ingrese el segundo número >> "))

# condicional de valor menor
if (valor_1 < valor_2):
    print("El ", valor_1, " es menor que ", valor_2)
else:
    print("El ", valor_2, " es menor que ", valor_1)
   
    
# captura de datos mayor
valor_3 = int(input("Ingrese el tercer número >> "))
valor_4 = int(input("Ingrese el cuarto número >> "))

# condicional de valor mayor
if (valor_3 > valor_4):
    print("El ", valor_3, " es mayor que ", valor_4)
else:
    print("El ", valor_4, " es mayor que ", valor_3)

