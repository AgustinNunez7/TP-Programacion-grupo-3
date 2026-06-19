from validaciones import *
from informacion import mostrar_todos_los_usuarios
from usuarios import usuarios

def registrar_usuario(lista : list) -> None:
    """Registra un nuevo usuario en el sistema."""
    usuario_nuevo = []

    id = len(lista) + 1
    usuario_nuevo.append(id)

    email_ingresado = input("Ingrese su email: ")
    while validar_dato_existente(email_ingresado, lista, 1) or not validar_que_sea_gmail(email_ingresado) or email_ingresado == "":
        email_ingresado = input("El mail debe ser un mail valido, no puede estar vacio y no puede estar en uso. Ingrese otro: ")
    usuario_nuevo.append(email_ingresado)

    contraseña_ingresada = input("Ingrese su contraseña: ")
    while not validar_rango(len(contraseña_ingresada), 6, 20):
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

    edad_ingresada = input("Ingrese su edad (debe ser un numero mayor a 0): ")
    while not validar_mayor_a(edad_ingresada, 0):
        edad_ingresada = input("La edad debe ser un numero mayor a 0. Reingrese la edad: ")
    usuario_nuevo.append(int(edad_ingresada))

    nacionalidad_ingresada = input("Ingrese su nacionalidad: ")
    while nacionalidad_ingresada == "" or not validar_que_sea_letras(nacionalidad_ingresada):
        nacionalidad_ingresada = input("La nacionalidad no puede estar vacia y debe contener solo letras. Ingrese su nacionalidad: ")
    usuario_nuevo.append(nacionalidad_ingresada)

    dni_ingresado = input("Ingrese su DNI (debe ser un numero): ")
    while validar_dato_existente(dni_ingresado, lista, 8) or len(dni_ingresado) != 8 or not validar_numero(dni_ingresado):
        dni_ingresado = input("Este DNI ya está en uso o no es válido. El DNI debe ser un numero de 8 digitos. Ingrese otro: ")
    usuario_nuevo.append(int(dni_ingresado))

    fecha_ingresada = input("Ingrese su fecha de registro (formato YYYY-MM-DD): ")
    while len(fecha_ingresada) != 10 or fecha_ingresada[4] != "-" or fecha_ingresada[7] != "-":
        fecha_ingresada = input("El formato de la fecha no es válido. Ingrese su fecha de registro (formato YYYY-MM-DD): ")
    usuario_nuevo.append(fecha_ingresada)

    usuario_nuevo.append(True)

    lista.append(usuario_nuevo)

def eliminar_usuario(lista : list) -> None:
    """Elimina un usuario del sistema."""
    email_ingresado = input("Ingrese el email del usuario que desea eliminar: ")
    while email_ingresado == "" or not validar_que_sea_gmail(email_ingresado) or not validar_dato_existente(email_ingresado, lista, 1):
        email_ingresado = input("El mail no puede estar vacio y debe estar registrado. Ingrese el email del usuario que desea eliminar: ")

    for i in range(len(lista)):
        if lista[i][1] == email_ingresado:
            print(f"El usuario con email {email_ingresado} ha sido eliminado.")
            lista[i][10] = False
            break


def iniciar_sesion(lista : list) -> list:
    """Inicia sesion en el sistema."""
    guardar_indice_usuario = -1
    email_ingresado = input("Ingrese su email: ")
    while email_ingresado == "" or not validar_que_sea_gmail(email_ingresado):
        email_ingresado = input("El mail no puede estar vacio y debe ser valido. Ingrese su email: ")

    contraseña_ingresada = input("Ingrese su contraseña: ")
    while contraseña_ingresada == "":
        contraseña_ingresada = input("La contraseña no puede estar vacia. Ingrese su contraseña: ")

    for i in range(len(lista)):
        if lista[i][1] == email_ingresado and lista[i][2] == contraseña_ingresada:
            guardar_indice_usuario = i
            break
    
    return guardar_indice_usuario

def modificar_usuario(lista : list) -> None:
    """Modifica los datos de un usuario existente."""
    mostrar_todos_los_usuarios(usuarios)
    email_ingresado = input("Ingrese el email del usuario que desea modificar: ")
    while email_ingresado == "" or not validar_que_sea_gmail(email_ingresado) or not validar_dato_existente(email_ingresado, lista, 1):
        email_ingresado = input("El mail no puede estar vacio y debe estar registrado. Ingrese el email del usuario que desea modificar: ")
    
    for i in range(len(lista)):
        if lista[i][1] == email_ingresado:
            print(f"Modifique uno de los siguientes datos: {lista[i][1]} - {lista[i][2]} - {lista[i][3]} - {lista[i][4]} - {lista[i][5]} - {lista[i][6]} - {lista[i][7]} - {lista[i][8]} - {lista[i][9]} - {lista[i][10]}")
            break
    
    opciones = ["mail", "contraseña", "rol", "nombre", "apellido", "edad", "nacionalidad", "dni", "fecha de registro", "activo"]
    dato_a_modificar = input("Ingrese el dato que desea modificar (mail, contraseña, rol, nombre, apellido, edad, nacionalidad, dni, fecha de registro, activo): ")
    while not validar_tipo_dato(dato_a_modificar, opciones):
        dato_a_modificar = input("El dato ingresado no es valido. Ingrese el dato que desea modificar (mail, contraseña, rol, nombre, apellido, edad, nacionalidad, dni, fecha de registro, activo): ")

    for i in range(len(lista)):
        if email_ingresado == lista[i][1]:
            if dato_a_modificar == "mail":
                nuevo_mail = input("Ingrese el nuevo mail: ")
                while validar_dato_existente(nuevo_mail, lista, 1) or not validar_que_sea_gmail(nuevo_mail) or nuevo_mail == "":
                    nuevo_mail = input("El mail debe ser un mail valido y no puede estar vacio, y no puede estar en uso. Ingrese otro: ")
                lista[i][1] = nuevo_mail
            elif dato_a_modificar == "contraseña":
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                while validar_rango(len(nueva_contraseña), 6, 20):
                    nueva_contraseña = input("La contraseña debe tener entre 6 y 20 caracteres. Ingrese otra: ")
                lista[i][2] = nueva_contraseña
            elif dato_a_modificar == "rol":
                nuevo_rol = input("Ingrese el nuevo rol (admin o jugador): ")
                while not validar_tipo_dato(nuevo_rol, ["jugador", "admin"]):
                    nuevo_rol = input("El rol debe ser 'admin' o 'jugador'. Ingrese el nuevo rol: ")
                lista[i][3] = nuevo_rol
            elif dato_a_modificar == "nombre":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                while nuevo_nombre == "" or not validar_que_sea_letras(nuevo_nombre):
                    nuevo_nombre = input("El nombre no puede estar vacio y debe contener solo letras. Ingrese el nuevo nombre: ")
                lista[i][4] = nuevo_nombre
            elif dato_a_modificar == "apellido":
                nuevo_apellido = input("Ingrese el nuevo apellido: ")
                while nuevo_apellido == "" or not validar_que_sea_letras(nuevo_apellido):
                    nuevo_apellido = input("El apellido no puede estar vacio y debe contener solo letras. Ingrese el nuevo apellido: ")
                lista[i][5] = nuevo_apellido
            elif dato_a_modificar == "edad":
                nueva_edad = input("Ingrese la nueva edad (debe ser un numero mayor a 0): ")
                while validar_mayor_a(nueva_edad, 0):
                    nueva_edad = validar_numero(input("La edad debe ser un numero mayor a 0. Reingrese la nueva edad: "))
                lista[i][6] = int(nueva_edad)
            elif dato_a_modificar == "nacionalidad":
                nueva_nacionalidad = input("Ingrese la nueva nacionalidad: ")
                while nueva_nacionalidad == "" or not validar_que_sea_letras(nueva_nacionalidad):
                    nueva_nacionalidad = input("La nacionalidad no puede estar vacia y debe contener solo letras. Ingrese la nueva nacionalidad: ")
                lista[i][7] = nueva_nacionalidad
            elif dato_a_modificar == "dni":
                nuevo_dni = input("Ingrese el nuevo DNI (debe ser un numero): ")
                while validar_dato_existente(nuevo_dni, lista, 8) or len(nuevo_dni) != 8 or validar_numero(nuevo_dni):
                    nuevo_dni = validar_numero(input("Este DNI ya está en uso o no es válido. El DNI debe ser un numero de 8 digitos. Ingrese otro: "))
                lista[i][8] = int(nuevo_dni)
            elif dato_a_modificar == "fecha de registro":
                nueva_fecha = validar_numero(input("Ingrese la nueva fecha de registro (formato YYYY-MM-DD): "))
                while len(nueva_fecha) != 10 or nueva_fecha[4] != "-" or nueva_fecha[7] != "-":
                    nueva_fecha = validar_numero(input("El formato de la fecha no es válido. Ingrese la nueva fecha de registro (formato YYYY-MM-DD): "))
                lista[i][9] = nueva_fecha
            elif dato_a_modificar == "activo":
                nuevo_activo = input("Ingrese el nuevo estado de activo (True o False): ")
                while not validar_tipo_dato(nuevo_activo, ["True", "False"]):
                    nuevo_activo = input("El estado de activo debe ser 'True' o 'False'. Ingrese el nuevo estado de activo: ")
                nuevo_activo = bool(nuevo_activo)
                lista[i][10] = nuevo_activo
            print(f"El usuario con email {email_ingresado} ha sido modificado.")
            break