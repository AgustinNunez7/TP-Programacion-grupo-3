from validaciones import *
from informacion import mostrar_todos_los_usuarios
from usuarios import usuarios
from persistencia import guardar_datos

def registrar_usuario(lista : list) -> None:
    """Registra un nuevo usuario en el sistema."""
    usuario_nuevo = []

    id = len(lista) + 1
    usuario_nuevo.append(id)

    email_ingresado = pedir_email(lista, 1, "Ingrese un mail (no registrado antes): ")    
    usuario_nuevo.append(email_ingresado)

    contraseña_ingresada = pedir_longitud_definida(3, 20, "Ingrese su contraseña: ")
    usuario_nuevo.append(contraseña_ingresada)

    rol = "jugador"
    usuario_nuevo.append(rol)

    nombre_ingresado = pedir_solo_letras("Ingrese su nombre: ")   
    usuario_nuevo.append(nombre_ingresado)

    apellido_ingresado = pedir_solo_letras("Ingrese su apellido: ")    
    usuario_nuevo.append(apellido_ingresado)

    edad_ingresada = pedir_mayor_a(0, "Ingrese su edad") 
    usuario_nuevo.append(edad_ingresada)

    nacionalidad_ingresada = pedir_solo_letras("Ingrese su nacionalidad: ")    
    usuario_nuevo.append(nacionalidad_ingresada)

    dni_ingresado = pedir_dni(lista, 8, "Ingrese su dni: ")    
    usuario_nuevo.append(dni_ingresado)

    fecha_ingresada = pedir_fecha("Ingrese su fecha de registro (formato YYYY-MM-DD): ")    
    usuario_nuevo.append(fecha_ingresada)

    usuario_nuevo.append(True)

    lista.append(usuario_nuevo)
    guardar_datos("TP/usuarios.json", lista)

def eliminar_usuario(lista : list) -> None:
    """Elimina un usuario del sistema."""
    dni_ingresado = pedir_dni_existente(lista, 8, "Ingrese el dni del usuario que desea eliminar: ")

    for i in range(len(lista)):
        if lista[i][8] == dni_ingresado:
            print(f"El usuario con el dni {dni_ingresado} ha sido eliminado.")
            lista[i][10] = False
            guardar_datos("TP/usuarios.json", lista)
            break

def iniciar_sesion(lista : list) -> list:
    """Inicia sesion en el sistema."""
    guardar_indice_usuario = -1
    email_ingresado = input("Ingrese su email: ")
    while email_ingresado == "" or not validar_que_sea_gmail(email_ingresado):
        email_ingresado = input("El mail no puede estar vacio y debe ser valido. Ingrese su email: ")

    contraseña_ingresada = pedir_longitud_definida(1, 20, "Ingrese su contraseña: ")

    for i in range(len(lista)):
        if lista[i][1] == email_ingresado and lista[i][2] == contraseña_ingresada:
            guardar_indice_usuario = i
            break
    
    return guardar_indice_usuario

def modificar_usuario(lista : list) -> None:
    """Modifica los datos de un usuario existente."""
    mostrar_todos_los_usuarios(lista)
    dni_ingresado = pedir_dni_existente(lista, 8, "Ingrese el dni del usuario que desea modificar: ")

    for i in range(len(lista)):
        if lista[i][8] == dni_ingresado:
            print(f"Modifique uno de los siguientes datos: {lista[i][1]} - {lista[i][2]} - {lista[i][3]} - {lista[i][4]} - {lista[i][5]} - {lista[i][6]} - {lista[i][7]} - {lista[i][8]} - {lista[i][9]} - {lista[i][10]}")
            break
    
    opciones = ["mail", "contraseña", "rol", "nombre", "apellido", "edad", "nacionalidad", "dni", "fecha de registro", "activo"]
    dato_a_modificar = pedir_opciones(opciones, "Ingrese el dato que desea modificar")

    for i in range(len(lista)):
        if dni_ingresado == lista[i][8]:
            if dato_a_modificar == "mail":
                nuevo_mail = pedir_email(lista, 1, "Ingrese el nuevo mail: ")                
                lista[i][1] = nuevo_mail

            elif dato_a_modificar == "contraseña":
                nueva_contraseña = pedir_longitud_definida(6,20, "Ingrese la nueva contraseña: ")                
                lista[i][2] = nueva_contraseña

            elif dato_a_modificar == "rol":
                nuevo_rol = pedir_opciones(["admin","jugador"], "Ingrese el nuevo rol")
                lista[i][3] = nuevo_rol

            elif dato_a_modificar == "nombre":
                nuevo_nombre = pedir_solo_letras("Ingrese el nuevo nombre: ")                
                lista[i][4] = nuevo_nombre

            elif dato_a_modificar == "apellido":
                nuevo_apellido = pedir_solo_letras("Ingrese el nuevo apellido: ")
                lista[i][5] = nuevo_apellido

            elif dato_a_modificar == "edad":
                nueva_edad = pedir_mayor_a(0, "Ingrese la nueva edad") 
                lista[i][6] = int(nueva_edad)

            elif dato_a_modificar == "nacionalidad":
                nueva_nacionalidad = pedir_solo_letras("Ingrese la nueva nacionalidad: ") 
                lista[i][7] = nueva_nacionalidad

            elif dato_a_modificar == "dni":
                nuevo_dni = pedir_dni(lista, 8, "Ingrese el nuevo dni") 
                lista[i][8] = int(nuevo_dni)
            
            elif dato_a_modificar == "fecha de registro":
                nueva_fecha = pedir_fecha("Ingrese la nueva fecha de registro (formato YYYY-MM-DD): ")
                lista[i][9] = nueva_fecha
            
            elif dato_a_modificar == "activo":
                nuevo_activo = pedir_opciones(["True","False"], "Ingrese el nuevo activo")
                nuevo_activo = bool(nuevo_activo)
                lista[i][10] = nuevo_activo
            
            print(f"El usuario {lista[i][4]} {lista[i][5]} ha sido modificado.")
            guardar_datos("TP/usuarios.json", lista)
            break

def pasar_dict(lista:list, keys:list):
    """Convierte una lista y una lista de claves `keys` en un diccionario.

    Asocia cada clave de `keys` con el elemento correspondiente en `lista`.
    """
    nuevo_dict = {}
    for i in range(len(lista)):
        nuevo_dict[keys[i]] = lista[i]

    return nuevo_dict

def pasar_list_dict(lista:list, keys:list):
    """Convierte una lista de listas en una lista de diccionarios usando `keys`.

    Para cada sublista en `lista` llama a `pasar_dict` y agrega el diccionario resultante.
    """
    nueva_list = []
    for i in range(len(lista)):
        nuevo_dict = pasar_dict(lista[i],keys)
        nueva_list.append(nuevo_dict)

    return nueva_list