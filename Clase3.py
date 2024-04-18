#######################
# Curso: Python nivel 1
# Autor: Roberto Lee
# Ejemplo: captura de datos
# Fecha: 15-04-2024
# Version 1
#######################

# Mostramos mensaje en pantalla
print("Programa de muestreo de captura de datos por pantalla\n")

# Definimos una variable tipo string y le asignamos un valor
variable = "aprendiendo Python"

''' definimos dos variables nuevas, en este caso nombre y apellido,
luego con la palabra input capturamos el valor que vamos asignar
a la variable'''

# Uso de la palabra reservada input para captura de datos
nombre = input("Hola cual es tu nombre: ")
apellido = input("\nCual es tu apellido: ")
edad = input("\nIngresa tu edad ")

# Uniendo los valores de las variables
# las " " y el espacio intermedio nos da un espacio entre palabras
salida = nombre + " " + apellido + " " + "con " + edad + " de edad esta " + variable

# Mostramos resultado en pantalla
print("\n", salida)
print("\nPrograma finalizado....")
