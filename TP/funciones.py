from usuarios import usuarios

menu_inicio = '''
1. Registrarse como nuevo usuario
2. Iniciar sesión
3. Salir del sistema
'''

def validar_rango(desde:int, hasta:int, mensaje:str)->int:
    numero = int(input(f"{mensaje} ({desde}-{hasta}): "))
    while numero < desde or numero > hasta:
        numero = int(input(f"Error. {mensaje} ({desde}-{hasta}): "))

    return numero

def validar_dato(dato1:str, dato2:str, mensaje:str)->str:
    dato = input(f"{mensaje} ({dato1},{dato2}):")
    while dato != dato1 and dato != dato2:
        dato = input(f"Error. {mensaje} ({dato1},{dato2}):")

    return dato

def crear_usuario()->list:
    usuario = [
        len(usuarios) + 1,
        input("Ingrese su mail: "),
        int(input("Ingrese contraseña: ")),
        validar_dato("usuario","admin", "Registrarse como"),
        input("Ingrese nombre: "),
        #input("Ingrese apellido: "),       Puesto en comentario temporalmente para hacer mas rapido el registro
        #int(input("Ingrese edad: ")),
        #input("Pais en el que vive: "),
        #input("Ingrese DNI: "),
        #input("Ingrese fecha: "),
        True
        ]

    return usuario


def buscar_usuario(lista:list, nombre:str, contra:str)->bool:
    inicio = False
    
    for i in range(len(lista)):
        if lista[i][4] == nombre and lista[i][2] == contra:
            inicio = True

    return inicio

def iniciar_secion(lista:list):
    nombre = input("Ingrese su nombre: ")
    contraseña = input("Ingrese su contraseña: ")
    while buscar_usuario(lista, nombre, contraseña) != True:
        print("Nombre o contraseña incorrectos")
        nombre = input("Ingrese su nombre: ")
        contraseña = input("Ingrese su contraseña: ")  


