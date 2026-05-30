from usuarios import usuarios

def mostrar_menu_principal() -> None:
    """Muestra el menu principal de opciones al usuario."""
    print("""\n|------------------ Menu de opciones ------------------|\n1) Registrarse como nuevo usuario\n2) Iniciar sesion\n3) Salir del sistema\n 
    """)

def mostrar_menu_jugador() -> None:
    """Muestra el menu de opciones para el jugador."""
    print("""\n|------------------ Menu de opciones ------------------|\n1) Ver datos personales\n2) Jugar juego 1\n3) Jugar juego 2\n4) Ver puntajes\n5) Cerrar sesion\n 
    """)

def mostrar_menu_admin() -> None:
    """Muestra el menu de opciones para el administrador."""
    print("""\n|------------------ Menu de opciones ------------------|\n1) Ver estadisticas\n2) Modificar usuario\n3) Eliminar usuario\n4) Cerrar sesion\n 
    """)

def validar_dato_existente(dato:str, lista:list, indice:int) -> None:
    """Valida que el dato ingresado por el usuario no exista en la lista."""

    existe = False
    for i in range(len(lista)):
        if str(lista[i][indice]) == dato:
            print("El dato ingresado ya existe. Intente nuevamente.")
            existe = True
            break

    return existe

def validar_que_sea_gmail(dato:str) -> bool:
    """Valida que el dato ingresado por el usuario sea un mail de gmail."""
    es_gmail = True
    dato_validar = len(dato) - 10
    # Es lo unico que se me ocurrio para validar xd
    if dato[dato_validar+1] == "@":
        if dato[dato_validar+2] == "g":
            if dato[dato_validar+3] == "m":
                if dato[dato_validar+4] == "a":
                    if dato[dato_validar+5] == "i":
                        if dato[dato_validar+6] == "l":
                            if dato[dato_validar+6] == ".":
                                if dato[dato_validar+7] == "c":
                                    if dato[dato_validar+9] == "o":
                                        if dato[dato_validar+10] == "m":
                                            es_gmail = False
    
    return es_gmail
    # if dato[dato_validar:] != "@gmail.com":
    #     print("El mail ingresado no es un mail de gmail. Intente nuevamente.")
    #     es_gmail = False

def validar_que_sea_letras(dato:str) -> bool:
    """Valida que el dato ingresado por el usuario sea solo letras."""
    es_letras = True
    for i in range(len(dato)):
        validar = ord(dato[i])
        if validar < 65 or validar > 122 or (validar > 90 and validar < 97):
            print("El dato ingresado debe contener solo letras. Intente nuevamente.")
            es_letras = False
            break

    return es_letras

def validar_numero(dato : str):
    """Valida que el dato ingresado sea un numero y no este vacio."""
    while dato == "":
        dato = input("El dato ingresado esta vacio. Reingrese el dato: ")

    validar = ord(dato[0])
    while validar <= 44 or validar >= 58 or validar == 46 or validar == 47:
        dato = input("El dato no es un numero. Reingrese el dato: ")
        validar = ord(dato[0])
        
    return dato

def registrar_usuario(lista : list) -> None:
    """Registra un nuevo usuario en el sistema."""
    usuario_nuevo = []

    id = len(lista) + 1
    usuario_nuevo.append(id)

    email_ingresado = input("Ingrese su email: ")
    while validar_dato_existente(email_ingresado, lista, 1) or len(email_ingresado) < 10 or not validar_que_sea_gmail(email_ingresado):
        email_ingresado = input("Este mail ya está en uso o no es un mail de gmail. El mail no puede estar vacio. Ingrese otro: ")
    usuario_nuevo.append(email_ingresado)

    contraseña_ingresada = input("Ingrese su contraseña: ")
    while len(contraseña_ingresada) < 6 or len(contraseña_ingresada) > 20:
        contraseña_ingresada = input("La contraseña debe tener entre 6 y 20 caracteres. Ingrese otra: ")
    usuario_nuevo.append(contraseña_ingresada)

    rol = "jugador"
    usuario_nuevo.append(rol)

    nombre_ingresado = input("Ingrese su nombre: ")
    while nombre_ingresado == "" or not validar_que_sea_letras(nombre_ingresado):
        nombre_ingresado = input("El nombre no puede estar vacio y debe contener solo letras. Ingrese su nombre: ")
    usuario_nuevo.append(nombre_ingresado)

    apellido_ingresado = input("Ingrese su apellido: ")
    while apellido_ingresado == "" or not validar_que_sea_letras(apellido_ingresado):
        apellido_ingresado = input("El apellido no puede estar vacio y debe contener solo letras. Ingrese su apellido: ")
    usuario_nuevo.append(apellido_ingresado)

    edad_ingresada = int(validar_numero(input("Ingrese su edad (debe ser un numero mayor a 0): ")))
    while edad_ingresada <= 0:
        edad_ingresada = int(validar_numero(input("La edad debe ser un numero mayor a 0. Reingrese la edad: ")))
    usuario_nuevo.append(edad_ingresada)

    nacionalidad_ingresada = input("Ingrese su nacionalidad: ")
    while nacionalidad_ingresada == "" or not validar_que_sea_letras(nacionalidad_ingresada):
        nacionalidad_ingresada = input("La nacionalidad no puede estar vacia y debe contener solo letras. Ingrese su nacionalidad: ")
    usuario_nuevo.append(nacionalidad_ingresada)

    dni_ingresado = validar_numero(input("Ingrese su DNI (debe ser un numero): "))
    while validar_dato_existente(dni_ingresado, lista, 8) or len(dni_ingresado) != 8:
        dni_ingresado = validar_numero(input("Este DNI ya está en uso o no es válido. El DNI debe ser un numero de 8 digitos. Ingrese otro: "))
    usuario_nuevo.append(dni_ingresado)

    fecha_ingresada = input("Ingrese su fecha de registro (formato YYYY-MM-DD): ")
    while len(fecha_ingresada) != 10 or fecha_ingresada[4] != "-" or fecha_ingresada[7] != "-":
        fecha_ingresada = input("El formato de la fecha no es válido. Ingrese su fecha de registro (formato YYYY-MM-DD): ")
    usuario_nuevo.append(fecha_ingresada)

    usuario_nuevo.append(True)



# formato: [id, mail, password, rol, nombre, apellido, edad, nacionalidad, dni, fecha_registro, activo]

def main() -> None:
    """Funcion principal del programa."""
    bandera = True
    while bandera:
        mostrar_menu_principal()
        opcion = input("Seleccione una opcion (del 1 al 3): ")
        match opcion:
            case "1":
                registrar_usuario(usuarios)
            case "2":
                pass
            case "3":
                bandera = False
            case _:
                print("Opcion no valida. Intente nuevamente.")


# Consignas a implementar
# Sistema de acceso
# El sistema deberá contar con un menú principal que aparezca apenas se
# inicia y permita:
# 1. Registrarse como nuevo usuario
# 2. Iniciar sesión
# 3. Salir del sistema
# Usuarios de sistema y sus menu
# Usuario final (jugador):
# Una vez iniciada la sesión como jugador, el sistema deberá mostrar un menú
# con las siguientes opciones:
# 1. Ver datos personales
# 2. Jugar juego 1
# 3. Jugar juego 2
# 4. Ver puntajes
# 5. Cerrar sesión
# Consideraciones:
# ● En este sprint no es necesario implementar la lógica de los juegos ni de los puntajes.
# Las opciones correspondientes pueden mostrarse como funcionalidades en
# construcción o devolver valores simulados.
# ● La opción “Ver datos personales” deberá mostrar la información del usuario
# actualmente logueado (por ejemplo: nombre, edad, identificador).
# Usuario administrador:
# Una vez iniciada la sesión como administrador, el sistema deberá mostrar un
# menú con las siguientes opciones:
# 1. Ver estadísticas
# 2. Modificar usuario
# 3. Eliminar usuario
# 4. Cerrar sesión
# Submenú de estadísticas
# La opción “Ver estadísticas” deberá dirigir a un submenú donde se
# implementan al menos cinco de las siguientes consultas sobre los usuarios
# registrados:
# ● Obtener el promedio de edad de los usuarios
# ● Determinar el usuario más joven
# ● Determinar el usuario de mayor edad
# ● Calcular la cantidad total de usuarios registrados
# ● Mostrar la cantidad de usuarios mayores de una edad determinada (por
# ejemplo, mayores de 18 años)
# ● Determinar si existe un usuario con un nombre específico (búsqueda)
# ● Mostrar el listado completo de usuarios
# ● 3 estadísticas más pensadas por ustedes
# Gestión de usuarios
# El administrador deberá poder:
# ● Modificar los datos de un usuario existente (por ejemplo: nombre o
# edad)
# ● Eliminar un usuario del sistema
# Temas evaluados
# ● Entradas y salidas
# ● Condicionales simples, compuestos, anidados
# ● Estructuras iterativas (while, for)
# ● Funciones; funciones recursivas
# ● Listas
# ● Organización del código (módulos y paquetes)