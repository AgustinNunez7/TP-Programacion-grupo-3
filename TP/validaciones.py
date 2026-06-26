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
    """Valida que el dato ingresado por el usuario sea un mail valido."""
    es_mail = False
    mail_excluido = "@"

    if validar_dato_existente("@", dato) and dato[0] != "@":
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
            es_letras = False
            break

    return es_letras

def validar_numero(dato : str) -> bool:
    """Valida que el dato ingresado sea un numero"""
    es_numero = True
    for i in range(len(dato)):
        validar = ord(dato[i])
        if validar <= 44 or validar >= 58 or validar == 46 or validar == 47:
            es_numero = False
            break
    
    return es_numero

def validar_mayor_a(dato, desde:int) -> bool:
    """Valida que dato sea un número mayor que 'desde'. Usa sólo funciones ya presentes."""
    numero_valido = False
    dato_str = str(dato)

    # Rechazar cadena vacía
    if dato_str == "":
        return False

    # Validar que la representación en cadena sea numérica y luego comparar
    if validar_numero(dato_str):
        if int(dato_str) > desde:
            numero_valido = True

    return numero_valido

def validar_rango(dato:int, desde:int, hasta:int) -> bool:
    """Valida que un número esté entre `desde` y `hasta` (exclusivo)."""
    numero_valido = False
    if validar_numero(str(dato)):
        if dato > desde and dato < hasta:
            numero_valido = True

    return numero_valido

def validar_tipo_dato(dato:str, opciones:list) -> bool:
    """Valida que el tipo de dato ingresado.""" 
    opcion_valida = False
    for i in range(len(opciones)):
        if dato == opciones[i]:
            opcion_valida = True
    
    return opcion_valida

def pedir_email(lista:list, indice:int, mensaje:str)-> str:
    email_ingresado = input(mensaje)
    while validar_dato_existente(email_ingresado, lista, indice) or not validar_que_sea_gmail(email_ingresado) or email_ingresado == "":
        email_ingresado = input(f"El mail debe ser un mail valido, no puede estar vacio y no puede estar en uso.\n{mensaje}")
    
    return email_ingresado

def pedir_mail_existente(lista:list, indice:int, mensaje:str)->str:
    email_ingresado = input(mensaje)
    while not validar_dato_existente(email_ingresado, lista, indice) or not validar_que_sea_gmail(email_ingresado) or email_ingresado == "":
        email_ingresado = input(f"El mail debe ser un mail valido, no puede estar vacio y debe estar registrado. \n{mensaje}: ")
    
    return email_ingresado

def pedir_longitud_definida(min:int, max:int, mensaje:str)->str:
    dato_ingresado = input(mensaje)
    while not validar_rango(len(dato_ingresado), min, max):
        dato_ingresado = input(f"Debe tener entre {min} y {max} caracteres. {mensaje}: ")
    
    return dato_ingresado

def pedir_solo_letras(mensaje:str)->str:
    dato_ingresado = input(mensaje)
    while dato_ingresado == "" or not validar_que_sea_letras(dato_ingresado):
        dato_ingresado = input(f"No puede estar vacio y debe contener solo letras. Ingrese su {mensaje}: ")
    return dato_ingresado

def pedir_mayor_a(min:int, mensaje:str)->int:
    numero_ingresado = input(f"{mensaje} (debe ser un numero mayor a {min}): ")
    # Comprobar cadena vacía antes de validar para evitar int('')
    while numero_ingresado == "" or not validar_mayor_a(numero_ingresado, min):
        numero_ingresado = input(f"Debe ser un numero mayor a {min}. {mensaje}: ")

    return int(numero_ingresado)

def pedir_dni_existente(lista:list, indice:int, mensaje:str)->int:
    dni_ingresado = input(mensaje)
    while not validar_dato_existente(dni_ingresado, lista, indice) or len(dni_ingresado) != 8 or not validar_numero(dni_ingresado):
        dni_ingresado = input(f"Este DNI no esta registrado. El DNI debe ser un numero de 8 digitos y debe estar registrado. {mensaje} ")
    
    return int(dni_ingresado)

def pedir_dni(lista:list, indice:int, mensaje:str)->int:
    dni_ingresado = input(mensaje)
    while validar_dato_existente(dni_ingresado, lista, indice) or len(dni_ingresado) != 8 or not validar_numero(dni_ingresado):
        dni_ingresado = input(f"Este DNI ya está en uso o no es válido. El DNI debe ser un numero de 8 digitos. \n{mensaje} ")
    
    return int(dni_ingresado)

def pedir_fecha(mensaje:str)->str:    
    fecha_ingresada = input(mensaje)
    while len(fecha_ingresada) != 10 or fecha_ingresada[4] != "-" or fecha_ingresada[7] != "-" or not validar_numero(fecha_ingresada):
        fecha_ingresada = input(f"El formato de la fecha no es válido. {mensaje}: ")
    
    return fecha_ingresada

def pedir_opciones(opciones:list, mensaje:str)->str:
    opciones_mensaje = ""
    for i in range(len(opciones)):
        opciones_mensaje += opciones[i]
        if i + 1 != len(opciones):
            opciones_mensaje += ","

    dato_ingresado = input(f"{mensaje} \n({opciones_mensaje}): ")
    while not validar_tipo_dato(dato_ingresado, opciones):
        dato_ingresado = input(f"{mensaje} \n({opciones_mensaje})")
    
    return dato_ingresado

