# Codigo 1, determinar si un numero es positivo o negativo
#print("\nEste programa determinara si un valor es positivo o negativo")
#numero = float(input("Dijite su numero: "))

#if (numero >= 0):
#    print("El numero", numero, "es positivo")

#else: 
#    print("El numero", numero, "es negativo")

#print("---------------------------------------------")



# Codigo 2, formula para sacar el resultado de una suma potenciada al cuadrado
#print("Este es un programa para sacar el resultado de una suma potenciada al cuadrado\n")
#x =float(input("Dijite el primer valor numerico: "))
#y= float(input("Dijite el segundo valor numerico: "))
#resultado = (x + y) ** 2

#print("\nEl resultado de la operacion es: ",resultado)

#print("---------------------------------------------")


# Codigo 3, formula para sacar el resultado del valor b al cuadrado, restandole 4*a*c
#print("\nEste es un progrma que saca el resultado" + 
#       " del valor b al cuadrado, restandole 4*a*c")

#a = float(input("Dijite el valor de a: "))
#b = float(input("Dijite el valor de b: "))
#c = float(input("Dijite el valor de c: "))

# Se calcula la ecuacion
#resultado = (b ** 2) - (4 * a * c)

#print("El resultado de esta operacion es", resultado)

#print("---------------------------------------------")



# Codigo 4, lineas correctas e incorrectas
# salto de linea
#print("")
#print("Como te llamas?")

#nombre = input()

#print("Hola", nombre)

# Incorrecta, esto imprime la linea tal y como fue escrita: Hola, {nombre}
#print("Hola, {nombre}")

# Correcta, imprime "Hola" y el valor de la variable
#print(f"Hola, {nombre}")


# Codigo 5, suma de dos numeros ingresados

# Captura de datos para las variables
#a, b = map(float, input("\nDigite 2 valores separados: ").split())

# Operacion aritmetica
#total = a + b

#print(f"El resultado de {a} + {b} es {total}")



# Codigo 6, operador de asignaciones

""""Operadores de asignaciones"""

# valor de cada variable
a, b, c = 10, 5, 2

print("Valor de la variable 'a':", a)
print("Valor de la variable 'b':", b)

c = a + b 
print("Operador = | El valor de la variable 'c' es:", c)

# La variable 'c' ahora vale '15' por lo cual se suma 'a'
c += a
print("Operador += | El valor de la variable 'c' es:", c)

c *= a
print("Operador *= | El valor de la variable 'c' es:", c)


c /= a
print("Operador /= | El valor de la variable 'c' es:", c)

c = 2
c %= a
print("Operador %= | El valor de la variable 'c' es:", c)

c **= a
print("Operador **= | El valor de la variable 'c' es:", c)

c //= a
print("Operador //= | El valor de la variable 'c' es:", c)


