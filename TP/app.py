from usuarios import usuarios
from funciones import *

continuar = True

while continuar == True:
    print(menu_inicio)

    opcion = validar_rango(1,3, "Elija una opcion")

    if opcion == 1:
        usuarios.append(crear_usuario())
        print("Usuario registrado")
    elif opcion == 2:
        print("Se elijio opcion 2")
    else:
        print("Se salio del sistema")
        continuar = False

    
