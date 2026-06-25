from validaciones import *
from informacion import *
from gestion_listas import *
from preguntados import jugar_preguntados
from persistencia import cargar_datos

def mostrar_menu_opciones(mensaje:str, opciones:list) -> None:
    menu = ""
    menu += f"\n|------------------ {mensaje} ------------------|\n"
    for i in range(len(opciones)):
        menu +=  f"{i+1}) {opciones[i]}\n"

    print(menu)

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
    print(f"{'Posicion':<10} {'Nombre':<20} {'Puntaje':<10}")
    print("-" * 60)
    
    cantidad = len(puntajes)
    if cantidad > 10:
        cantidad = 10
    
    for i in range(cantidad):
        posicion = i + 1
        nombre = puntajes[i]["nombre"]
        puntaje = puntajes[i]["puntaje"]
        print(f"{posicion:<10} {nombre:<20} {puntaje:<10}")
    
    print("-" * 60 + "\n")

def menu_jugador(usuario:int, usuarios:list) -> None:
    """Muestra el menu de opciones para el jugador."""
    bandera_2 = True
    while bandera_2:
        opciones = ["Ver datos personales", "Jugar juego 1", "Jugar juego 2", "Ver puntaje", "Cerrar sesion"]
        mostrar_menu_opciones("Menu de opciones", opciones)
        opcion = input("Seleccione una opcion (del 1 al 5): ")
        match opcion:
            case "1":
                print("|------------------ Datos personales ------------------|")
                mostrar_usuario(usuarios, usuario)
            case "2":
                usuario_id = usuarios[usuario][0]
                usuario_nombre = usuarios[usuario][4]
                usuario_email = usuarios[usuario][1]
                jugar_preguntados(usuario_id, usuario_nombre, usuario_email)
            case "3":
                print("Funcionalidad en construccion.")
            case "4":
                ver_top_10_puntajes()
            case "5":
                bandera_2 = False
            case _:
                print("Opcion no valida. Intente nuevamente.")

def menu_estadisticas(usuarios:list) -> None:
    """Muestra el menu de opciones de la opcion Ver estadiscticas."""
    bandera_stat = True
    while bandera_stat:
        opciones = ["Ver promedio de edad de los usuarios", "Ver el usuario de mayor edad", "Ver el usuario mas joven",
                     "Ver cantidad de usuarios registrados", "Ver usuarios mayores a una edad ingresada", 
                     "Determinar si existe un usuario con un nombre específico", "Mostrar todos los usuarios", "Volver al menu anterior"]
        mostrar_menu_opciones("Estadisticas", opciones)
        opcion = input("Seleccione una opcion (del 1 al 8): ")
        match opcion:
            case "1":
                print(promedio_lista(usuarios, 6))
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

def menu_admin(usuarios:list) -> None:
    """Muestra el menu de opciones para el administrador."""
    bandera_3 = True
    while bandera_3:
        opciones = ["Ver estadisticas", "Modificar usuario", "Eliminar usuario", "Cerrar sesion"]
        mostrar_menu_opciones("Menu de opciones", opciones)
        opcion = input("Seleccione una opcion (del 1 al 4): ")
        match opcion:
            case "1":
                menu_estadisticas(usuarios)
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
    usuarios = cargar_datos("TP/usuarios.json")
    
    bandera = True
    while bandera:
        opciones = ["Registrarse como nuevo usuario", "Iniciar sesion", "Salir del sistema"]
        mostrar_menu_opciones("Menu de opciones", opciones)
        opcion = input("Seleccione una opcion (del 1 al 3): ")
        match opcion:
            case "1":
                registrar_usuario(usuarios)
            case "2":
                data_usuario = iniciar_sesion(usuarios)
                if data_usuario != -1:
                    if usuarios[data_usuario][3] == "jugador":
                        print(f"Bienvenido/a jugador {usuarios[data_usuario][4]} {usuarios[data_usuario][5]}!")
                        menu_jugador(data_usuario, usuarios)
                    elif usuarios[data_usuario][3] == "admin":
                        print(f"Bienvenido/a admin {usuarios[data_usuario][4]} {usuarios[data_usuario][5]}!")
                        menu_admin(usuarios)
                else:
                    print("No se pudo iniciar sesion. El email o la contraseña son incorrectos.")
            case "3":
                bandera = False
                print("Se salio del sistema")
            case _:
                print("Opcion no valida. Intente nuevamente.")
