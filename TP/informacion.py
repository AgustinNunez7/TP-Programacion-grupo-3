from validaciones import validar_numero, validar_que_sea_letras, validar_mayor_a
from persistencia import cargar_datos

def mostrar_usuario(lista:list, indice:int)->None:
    """Muestra los datos de un usuario registrado"""
    if lista[indice][10] == True:
        print(f"mail: {lista[indice][1]}\nnombre: {lista[indice][4]}\napellido: {lista[indice][5]}\nedad: {lista[indice][6]}\nnacionalidad: {lista[indice][7]}\ndni: {lista[indice][8]}\nfecha de registro: {lista[indice][9]}\n")

def mostrar_todos_los_usuarios(lista : list) -> None:
    """Muestra el listado completo de usuarios registrados."""
    print("|------------------ Listado de usuarios ------------------|")
    for i in range(len(lista)):
        mostrar_usuario(lista, i)

def promedio_lista(lista:list, indice:int) -> float:
    """Calcula el promedio de edad de los usuarios registrados."""
    suma = 0
    cantidad = 0

    for i in range(len(lista)):
        if lista[i][10] == True:
            suma += lista[i][indice]
            cantidad += 1

    if cantidad > 0:
        promedio = suma / cantidad
    else:
        promedio = 0

    return promedio

def buscar_menor_mayor(lista : list, indice:int, mayor_menor:str) -> None:
    extremo = lista[0][indice] 
    
    for i in range(len(lista)):
        if lista[i][10] == True:
            if mayor_menor == "mayor":
                if lista[i][indice] > extremo:
                    extremo = lista[i][indice]
                    lista_usuario = f"El usuario de mayor edad es: {lista[i][4]} {lista[i][5]} con {extremo} años"
            elif mayor_menor == "menor":
                if lista[i][indice] < extremo:
                    extremo = lista[i][indice]
                    lista_usuario = f"El usuario de menor edad es: {lista[i][4]} {lista[i][5]} con {extremo} años"
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

    edad_minima = input(f"Ingrese la edad minima para filtrar los usuarios (debe ser un numero mayor a 0): ")
    while not validar_mayor_a(edad_minima, 0) or not validar_numero(edad_minima):
        edad_minima = input(f"La edad minima debe ser un numero mayor a 0. Reingrese la edad minima para filtrar los usuarios: ")
    edad_minima = int(edad_minima)

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
            usuarios_encontrados.append(i)

    if len(usuarios_encontrados) > 0:
        print(f"Usuarios encontrados con el nombre '{nombre}':")
        for usuario in usuarios_encontrados:
            mostrar_usuario(lista, usuario)
    else:
        print(f"No se encontraron usuarios con el nombre '{nombre}'.")

def ver_top_10_puntajes() -> None:
    """Muestra los 10 mayores puntajes ordenados de mayor a menor usando burbujeo."""
    puntajes = cargar_datos("TP/puntajes.json")
    
    if len(puntajes) == 0:
        print("\n|------------------ Ver Puntajes ------------------|")
        print("No hay puntajes registrados aun.\n")
        return
    
    # Ordenar por burbujeo (de mayor a menor)
    for i in range(len(puntajes)):
        for j in range(len(puntajes) - 1 - i):
            if puntajes[j]["puntaje"] < puntajes[j + 1]["puntaje"]:
                # Intercambiar
                temp = puntajes[j]
                puntajes[j] = puntajes[j + 1]
                puntajes[j + 1] = temp
    
    # Mostrar top 10
    print("\n|------------------ Top 10 Puntajes ------------------|")
    print(f"{'Posicion':<15} {'Nombre':<20} {'Puntaje':<10}")
    print("-" * 60)
    
    cantidad = len(puntajes)
    if cantidad > 10:
        cantidad = 10
    
    for i in range(cantidad):
        posicion = i + 1
        nombre = puntajes[i]["nombre"]
        puntaje = puntajes[i]["puntaje"]
        print(f"{posicion:<15} {nombre:<20} {puntaje:<10}")
    
    print("-" * 60 + "\n")