def calcular_distancia(velocidad, tiempo):
    distancia = velocidad * tiempo
    return distancia

def calcular_tiempo(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo
 
def calcular_velocidad(distancia, tiempo):
    velocidad = distancia / tiempo
    return velocidad

# Funcion para hacer el llamado del menu y sus respectivas entradas
def menu():
    while True:
        print("\nMenu de seleccion para calcular las siguientes opciones:")
        print("1. Calcular velocidad")
        print("2. Calcular distancia")
        print("3. Calcular tiempo")
        print("4. Salir")

        opcion = input("\nSeleccione una opcion para realizar su respectivo calculo: ")

        if opcion == "1":
            distancia = float(input("Ingrese la distancia en metros: "))
            tiempo = float(input("Ingrese el tiempo en segundos: "))
            resultado = calcular_velocidad(distancia, tiempo)
            print("El resultado de la operacion es esta: ", resultado)
            break

        elif opcion == "2":
            velocidad = float(input("Ingrese la velocidad en metros por segundo: "))
            tiempo = float(input("Ingrese el tiempo en segundos: "))
            resultado = calcular_distancia(velocidad, tiempo)
            print("El resultado de la operacion es esta: ", resultado)
            break

        elif opcion == "3":
            distancia = float(input("Ingrese la distancia en metros: "))
            velocidad = float(input("Ingrese la velocidad en metros por segundo: "))
            resultado = calcular_tiempo(distancia, velocidad)
            print("El resultado de la operacion es esta: ", resultado)
            break

        elif opcion == "4":
            print("Marcaste la opcion de salida. Hasta luego.")
            break
        else: 
            print("La opcion que marcaste no es valida.")
            break

# Aca se llama a la funcion de menu
menu()