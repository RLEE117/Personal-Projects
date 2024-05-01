def fondo_maniobra(ac, pc):
    formula1 = ac - pc
    if formula1 >= 0:
        print("Su empresa se encuentra con un equilibrio financiero positivo.")
    else:
        print("Su empresa se encuentra en un estado de perdida.")
        resultado += formula1
    print("Este el resultado de la formula 1", resultado)
    #print("Este es el resultado de la formula 1: ", fondo_maniobra(ac, pc))
    
    return formula1

def razon_corriente(ac, pc):
    formula2 = ac / pc
    if formula2 <= 1:
        print("Su empresa no cuenta con la capacidad para cumplir con sus obligaciones a corto plazo.")
    elif formula2 > 2:
        print("Su empresa cuenta con la capacidad para cumplir con sus obligaciones a corto plazo.")
    print("Este es el resultado de la formula 2: ", razon_corriente(ac, pc))
    #    resultado2 += formula2
    return formula2

def prueba_acida(ac, pc, inv):
    formula3 = (ac - inv) / pc
    if formula3 > 1:
        print("Su empresa cuenta con la capacidad para cumplir con las obligaciones a corto plazo.")
    elif formula3 < 1:
        print("Su empresa es incapaz de cumplir con sus obligaciones a largo plazo.")
    print("Este es el resultado de la formula 3: ", prueba_acida(ac, pc, inv))
    #    resultado3 += formula3
    return formula3

ac = float(input("Ingrese el dato del activo corriente: "))
pc = float(input("Ingrese el dato del pasivo corriente: "))
inv = float(input("Ingrese el dato del inventario: "))


