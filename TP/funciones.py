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

def mostrar_menu_estadisticas() -> None:
    """Muestra el menu de opciones de las opcion Estadisticas."""
    print("""\n|------------------ Estadisticas ------------------|\n1) Ver promedio de edad de los usuarios\n2) Ver el usuario mas joven\n3) Ver el usuario de mayor edad\n4) Ver cantidad de usuarios registrados\n5) Ver usuarios mayores a una edad ingresada\n6) Determinar si existe un usuario con un nombre específico\n7) Mostrar todos los usuarios\n8) Volver al menu anterior\n
    """)


def buscar_dato(dato, lista:list, indice:int = -1)->int:
    """Busca un dato en una lista y devuelve su indice.
        Si no lo encuentra devuelve -1"""

    indice_encontrado = -1
    if indice != -1:
        for i in range(len(lista)):
            if str(lista[i][indice]) == dato:
                indice_encontrado = i
                break
    else:
        for i in range(len(lista)):
            if str(lista[i]) == dato:
                indice_encontrado = i
                break
    
    return indice_encontrado

def buscar_max(lista:list, indice:int)->int:
    """Busca el numero mayor de una sublista por indice y devuelve su indice """

    max = lista[0][indice]
    indice_max = 0

    for i in range(len(lista)):
        if lista[i][indice] > max:
            max = lista[i][indice]
            indice_max = i
    
    return indice_max 

def buscar_min(lista:list, indice:int)->int:
    """Busca el numero menor de una sublista por indice y devuelve su indice """

    min = lista[0][indice]
    indice_min = 0

    for i in range(len(lista)):
        if lista[i][indice] < min:
            min = lista[i][indice]
            indice_min = i
    
    return indice_min 

def validar_dato_existente(dato:str, lista:list, indice:int = -1) -> bool:
    """Valida que el dato ingresado por el usuario exista en la lista."""

    existe = False
    if indice != -1:
        for i in range(len(lista)):
            if str(lista[i][indice]) == dato:
                existe = True
                break
    else:
        for i in range(len(lista)):
            if str(lista[i]) == dato:
                existe = True
                break

    return existe

def validar_que_sea_gmail(dato:str) -> bool:
    """Valida que el dato ingresado por el usuario sea un mail de gmail."""
    es_mail = False
    mail_excluido = "@"

    if validar_dato_existente("@", dato):
        for i in range(len(dato)):
            if dato[i] == "@":
                indice_arroba = i
                break

        for i in range(indice_arroba+1, len(dato)):
            mail_excluido += dato[i]

        if mail_excluido == "@gmail.com" or mail_excluido == "@arcade.com":
            es_mail = True

    return es_mail


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

def validar_numero(dato : str) -> str:
    """Valida que el dato ingresado sea un numero y no este vacio."""
    while dato == "":
        dato = input("El dato ingresado esta vacio. Reingrese el dato: ")
    es_numero = True
    while es_numero:
        for i in range(len(dato)):
            validar = ord(dato[i])
            if validar <= 44 or validar >= 58 or validar == 46 or validar == 47:
                print("El dato ingresado debe contener solo numeros. Intente nuevamente.")
                dato = input("Reingrese el dato: ")
                validar = ord(dato[i])
        es_numero = False
    
    return dato
        

def registrar_usuario(lista : list) -> None:
    """Registra un nuevo usuario en el sistema."""
    usuario_nuevo = []

    id = len(lista) + 1
    usuario_nuevo.append(id)
    email_ingresado = input("Ingrese su email: ")
    while validar_dato_existente(email_ingresado, lista, 1) or not validar_que_sea_gmail(email_ingresado) or email_ingresado == "" or len(email_ingresado) < 11:
        email_ingresado = input("El mail debe ser un mail valido y no puede estar vacio, y no puede estar en uso. Ingrese otro: ")
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

    edad_ingresada = validar_numero(input("Ingrese su edad (debe ser un numero mayor a 0): "))
    while int(edad_ingresada) <= 0:
        edad_ingresada = validar_numero(input("La edad debe ser un numero mayor a 0. Reingrese la edad: "))
    usuario_nuevo.append(int(edad_ingresada))

    nacionalidad_ingresada = input("Ingrese su nacionalidad: ")
    while nacionalidad_ingresada == "" or not validar_que_sea_letras(nacionalidad_ingresada):
        nacionalidad_ingresada = input("La nacionalidad no puede estar vacia y debe contener solo letras. Ingrese su nacionalidad: ")
    usuario_nuevo.append(nacionalidad_ingresada)

    dni_ingresado = validar_numero(input("Ingrese su DNI (debe ser un numero): "))
    while validar_dato_existente(dni_ingresado, lista, 8) or len(dni_ingresado) != 8:
        dni_ingresado = validar_numero(input("Este DNI ya está en uso o no es válido. El DNI debe ser un numero de 8 digitos. Ingrese otro: "))
    usuario_nuevo.append(int(dni_ingresado))

    fecha_ingresada = validar_numero(input("Ingrese su fecha de registro (formato YYYY-MM-DD): "))
    while len(fecha_ingresada) != 10 or fecha_ingresada[4] != "-" or fecha_ingresada[7] != "-":
        fecha_ingresada = validar_numero(input("El formato de la fecha no es válido. Ingrese su fecha de registro (formato YYYY-MM-DD): "))
    usuario_nuevo.append(fecha_ingresada)

    usuario_nuevo.append(True)

    lista.append(usuario_nuevo)


def iniciar_sesion(lista : list) -> list:
    """Inicia sesion en el sistema."""
    guardar_datos_usuario = []
    email_ingresado = input("Ingrese su email: ")
    while email_ingresado == "" or not validar_que_sea_gmail(email_ingresado) or email_ingresado == "" or len(email_ingresado) < 11:
        email_ingresado = input("El mail no puede estar vacio y debe ser valido. Ingrese su email: ")

    contraseña_ingresada = input("Ingrese su contraseña: ")
    while contraseña_ingresada == "":
        contraseña_ingresada = input("La contraseña no puede estar vacia. Ingrese su contraseña: ")

    for i in range(len(lista)):
        if lista[i][1] == email_ingresado and lista[i][2] == contraseña_ingresada:
            guardar_datos_usuario = lista[i]
            if lista[i][3] == "jugador":
                print(f"Bienvenido jugador {lista[i][4]} {lista[i][5]}!")
            elif lista[i][3] == "admin":
                print(f"Bienvenido admin {lista[i][4]} {lista[i][5]}!")
            break
    if guardar_datos_usuario == []:
        guardar_datos_usuario = ["invalid", "invalid", "invalid", "invalid", "invalid", "invalid", "invalid", "invalid", "invalid", "invalid", False]
    
    return list(guardar_datos_usuario)

def ver_datos_personales(usuario : list) -> None:
    """Muestra los datos personales del usuario logueado."""
    print("|------------------ Datos personales ------------------|")
    print(f"mail: {usuario[1]}\nnombre: {usuario[4]}\napellido: {usuario[5]}\nedad: {usuario[6]}\nnacionalidad: {usuario[7]}\ndni: {usuario[8]}\nfecha de registro: {usuario[9]}")

def eliminar_usuario(lista : list) -> None:
    """Elimina un usuario del sistema."""
    email_ingresado = input("Ingrese el email del usuario que desea eliminar: ")
    while email_ingresado == "" or not validar_que_sea_gmail(email_ingresado) or not validar_dato_existente(email_ingresado, lista, 1) or email_ingresado == "" or len(email_ingresado) < 11:
        email_ingresado = input("El mail no puede estar vacio y debe estar registrado. Ingrese el email del usuario que desea eliminar: ")

    for i in range(len(lista)):
        if lista[i][1] == email_ingresado:
            lista[i][10] = False
            print(f"El usuario con email {email_ingresado} ha sido eliminado.")
            break

def mostrar_usuario(lista:list, indice:int)->None:
    """Muestra los datos de un usuario registrado"""
    if lista[indice][10] == True:
        print(f"mail: {lista[indice][1]}\nnombre: {lista[indice][4]}\napellido: {lista[indice][5]}\nedad: {lista[indice][6]}\nnacionalidad: {lista[indice][7]}\ndni: {lista[indice][8]}\nfecha de registro: {lista[indice][9]}\n")

def mostrar_todos_los_usuarios(lista : list) -> None:
    """Muestra el listado completo de usuarios registrados."""
    print("|------------------ Listado de usuarios ------------------|")
    for i in range(len(lista)):
        mostrar_usuario(lista, i)

def promedio_edad(lista : list) -> float:
    """Calcula el promedio de edad de los usuarios registrados."""
    suma_edades = 0
    cantidad_usuarios = 0

    for i in range(len(lista)):
        if lista[i][10] == True:
            suma_edades += lista[i][6]
            cantidad_usuarios += 1

    if cantidad_usuarios > 0:
        promedio = suma_edades / cantidad_usuarios
    else:
        promedio = 0

    return promedio

def buscar_menor_mayor(lista : list, indice:int, mayor_menor:str) -> None:
    lista_usuario = []
    mayor = 0
    menor = 1000
    
    for i in range(len(lista)):
        if lista[i][10] == True:
            if mayor_menor == "mayor":
                if lista[i][indice] > mayor:
                    mayor = lista[i][indice]
                    lista_usuario = (f"El usuario de mayor edad es: {lista[i][4]} {lista[i][5]}")
            elif mayor_menor == "menor":
                if lista[i][indice] < menor:
                    menor = lista[i][indice]
                    lista_usuario = (f"El usuario de menor edad es: {lista[i][4]} {lista[i][5]}")
    print(lista_usuario)


def cantidad_total_usuarios(lista : list) -> int:
    """Calcula la cantidad total de usuarios registrados."""
    cantidad_usuarios = 0

    for i in range(len(lista)):
        if lista[i][10] == True:
            cantidad_usuarios += 1

    return cantidad_usuarios

def mostrar_cantidad_usuarios_mayores_de_edad(lista : list) -> None:
    """Muestra la cantidad de usuarios mayores de una edad determinada."""
    cantidad_usuarios_mayores = 0
    edad_minima = validar_numero(input(f"Ingrese la edad minima para filtrar los usuarios (debe ser un numero mayor a 0): "))
    while int(edad_minima) <= 0:
        edad_minima = validar_numero(input(f"La edad minima debe ser un numero mayor a 0. Reingrese la edad minima para filtrar los usuarios: "))
    
    for i in range(len(lista)):
        if lista[i][10] == True and lista[i][6] > edad_minima:
            cantidad_usuarios_mayores += 1

    print(f"Cantidad de usuarios mayores de {edad_minima} años: {cantidad_usuarios_mayores}")

def busqueda_de_usuario_por_nombre(lista : list) -> None:
    """Determina si existe un usuario con un nombre específico (búsqueda)."""
    usuarios_encontrados = []

    nombre = input("Ingrese el nombre del usuario que desea buscar: ")
    while nombre == "" or not validar_que_sea_letras(nombre):
        nombre = input("El nombre no puede estar vacio y debe contener solo letras. Ingrese el nombre del usuario que desea buscar: ")

    for i in range(len(lista)):
        if lista[i][10] == True and lista[i][4] == nombre:
            usuarios_encontrados.append(lista[i])

    if len(usuarios_encontrados) > 0:
        print(f"Usuarios encontrados con el nombre '{nombre}':")
        for usuario in usuarios_encontrados:
            print(f"id : {usuario[0]}\nmail: {usuario[1]}\nnombre: {usuario[4]}\napellido: {usuario[5]}\nedad: {usuario[6]}\nnacionalidad: {usuario[7]}\ndni: {usuario[8]}\nfecha de registro: {usuario[9]}\n")
    else:
        print(f"No se encontraron usuarios con el nombre '{nombre}'.")

def validar_tipo_dato(dato: str):
    """Valida que el tipo ingresado sea uno de los tipos de pokemon."""
    lista_tipos = ["mail", "contraseña", "rol", "nombre", "apellido", "edad", "nacionalidad", "dni", "fecha de registro", "activo"]
    for i in range(len(lista_tipos)):
        if dato == lista_tipos[i]:
            return False
    return True

def modificar_usuario(lista : list) -> None:
    """Modifica los datos de un usuario existente."""
    email_ingresado = input("Ingrese el email del usuario que desea modificar: ")
    while email_ingresado == "" or not validar_que_sea_gmail(email_ingresado) or not validar_dato_existente(email_ingresado, lista, 1) or email_ingresado == "" or len(email_ingresado) < 11:
        email_ingresado = input("El mail no puede estar vacio y debe estar registrado. Ingrese el email del usuario que desea modificar: ")
    
    for i in range(len(lista)):
        if lista[i][1] == email_ingresado:
            print(f"Modifique uno de los siguientes datos: {lista[i][1]} - {lista[i][2]} - {lista[i][3]} - {lista[i][4]} - {lista[i][5]} - {lista[i][6]} - {lista[i][7]} - {lista[i][8]} - {lista[i][9]} - {lista[i][10]}")
            break
    dato_a_modificar = input("Ingrese el dato que desea modificar (nombre, apellido, edad o nacionalidad): ")
    while validar_tipo_dato(dato_a_modificar):
        dato_a_modificar = input("El dato ingresado no es valido. Ingrese el dato que desea modificar (nombre, apellido, edad o nacionalidad, todo excepto id): ")

    for i in range(len(lista)):
        if email_ingresado == lista[i][1]:
            if dato_a_modificar == "mail":
                nuevo_mail = input("Ingrese el nuevo mail: ")
                while validar_dato_existente(nuevo_mail, lista, 1) or not validar_que_sea_gmail(nuevo_mail) or nuevo_mail == "" or len(nuevo_mail) < 11:
                    nuevo_mail = input("El mail debe ser un mail valido y no puede estar vacio, y no puede estar en uso. Ingrese otro: ")
                lista[i][1] = nuevo_mail
            elif dato_a_modificar == "contraseña":
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                while len(nueva_contraseña) < 6 or len(nueva_contraseña) > 20:
                    nueva_contraseña = input("La contraseña debe tener entre 6 y 20 caracteres. Ingrese otra: ")
                lista[i][2] = nueva_contraseña
            elif dato_a_modificar == "rol":
                nuevo_rol = input("Ingrese el nuevo rol (admin o jugador): ")
                while nuevo_rol != "admin" and nuevo_rol != "jugador":
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
                nueva_edad = validar_numero(input("Ingrese la nueva edad (debe ser un numero mayor a 0): "))
                while int(nueva_edad) <= 0:
                    nueva_edad = validar_numero(input("La edad debe ser un numero mayor a 0. Reingrese la nueva edad: "))
                lista[i][6] = int(nueva_edad)
            elif dato_a_modificar == "nacionalidad":
                nueva_nacionalidad = input("Ingrese la nueva nacionalidad: ")
                while nueva_nacionalidad == "" or not validar_que_sea_letras(nueva_nacionalidad):
                    nueva_nacionalidad = input("La nacionalidad no puede estar vacia y debe contener solo letras. Ingrese la nueva nacionalidad: ")
                lista[i][7] = nueva_nacionalidad
            elif dato_a_modificar == "dni":
                nuevo_dni = validar_numero(input("Ingrese el nuevo DNI (debe ser un numero): "))
                while validar_dato_existente(nuevo_dni, lista, 8) or len(nuevo_dni) != 8:
                    nuevo_dni = validar_numero(input("Este DNI ya está en uso o no es válido. El DNI debe ser un numero de 8 digitos. Ingrese otro: "))
                lista[i][8] = int(nuevo_dni)
            elif dato_a_modificar == "fecha de registro":
                nueva_fecha = validar_numero(input("Ingrese la nueva fecha de registro (formato YYYY-MM-DD): "))
                while len(nueva_fecha) != 10 or nueva_fecha[4] != "-" or nueva_fecha[7] != "-":
                    nueva_fecha = validar_numero(input("El formato de la fecha no es válido. Ingrese la nueva fecha de registro (formato YYYY-MM-DD): "))
                lista[i][9] = nueva_fecha
            elif dato_a_modificar == "activo":
                nuevo_activo = input("Ingrese el nuevo estado de activo (True o False): ")
                while nuevo_activo != "True" and nuevo_activo != "False":
                    nuevo_activo = input("El estado de activo debe ser 'True' o 'False'. Ingrese el nuevo estado de activo: ")
                nuevo_activo = bool(nuevo_activo)
                lista[i][10] = nuevo_activo
            print(f"El usuario con email {email_ingresado} ha sido modificado.")
            break

def menu_jugador(usuario : list) -> None:
    """Muestra el menu de opciones para el jugador."""
    bandera_2 = True
    while bandera_2:
        mostrar_menu_jugador()
        opcion = input("Seleccione una opcion (del 1 al 5): ")
        match opcion:
            case "1":
                ver_datos_personales(usuario)
            case "2":
                print("Funcionalidad en construccion.")
            case "3":
                print("Funcionalidad en construccion.")
            case "4":
                print("Funcionalidad en construccion.")
            case "5":
                bandera_2 = False
            case _:
                print("Opcion no valida. Intente nuevamente.")

def menu_estadisticas() -> None:
    """Muestra el menu de opciones de la opcion Ver estadiscticas."""
    bandera_stat = True
    while bandera_stat:
        mostrar_menu_estadisticas()
        opcion = input("Seleccione una opcion (del 1 al 6): ")
        match opcion:
            case "1":
                print(promedio_edad(usuarios))
            case "2":
                buscar_menor_mayor(usuarios, 6, "mayor")
            case "3":
                buscar_menor_mayor(usuarios, 6, "menor")
            case "4":
                print(f"La cantidad total de usuarios registrados es: {cantidad_total_usuarios(usuarios)}")
            case "5":
                mostrar_cantidad_usuarios_mayores_de_edad(usuarios)
            case "6":
                busqueda_de_usuario_por_nombre(usuarios)
            case "7":
                mostrar_todos_los_usuarios(usuarios)
            case "8":
                bandera_stat = False
            case _:
                print("Opcion no valida. Intente nuevamente.")

def menu_admin() -> None:
    """Muestra el menu de opciones para el administrador."""
    bandera_3 = True
    while bandera_3:
        mostrar_menu_admin()
        opcion = input("Seleccione una opcion (del 1 al 4): ")
        match opcion:
            case "1":
                menu_estadisticas()
            case "2":
                modificar_usuario(usuarios)
            case "3":
                eliminar_usuario(usuarios)
            case "4":
                bandera_3 = False
            case _:
                print("Opcion no valida. Intente nuevamente.")

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
                data_usuario = iniciar_sesion(usuarios)
                if data_usuario[3] == "jugador":
                    menu_jugador(data_usuario)
                elif data_usuario[3] == "admin":
                    menu_admin()
                else:
                    print("No se pudo iniciar sesion. El email o la contraseña son incorrectos.")
            case "3":
                bandera = False
            case _:
                print("Opcion no valida. Intente nuevamente.")