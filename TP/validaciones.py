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

def validar_mayor_a(dato:int, desde:int) -> bool:
    numero_valido = False
    if validar_numero(dato):
        if int(dato) > desde:
            numero_valido = True

    return numero_valido

def validar_rango(dato:int, desde:int, hasta:int) -> bool:
    numero_valido = False
    if validar_numero(str(dato)):
        if dato > desde and dato < hasta:
            numero_valido = True

    return numero_valido

def validar_tipo_dato(dato:str, opciones:list) -> bool:
    """Valida que el tipo ingresado sea uno de los tipos de pokemon.""" #Es MUY IMPORTANTE los pokemones
    opcion_valida = False
    for i in range(len(opciones)):
        if dato == opciones[i]:
            opcion_valida = True
    return opcion_valida