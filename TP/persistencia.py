import json

def cargar_datos(ruta: str) -> list:
    """Carga datos desde un archivo JSON"""
    with open(ruta, "r") as archivo:
        datos = json.load(archivo)          
    return datos


def guardar_datos(ruta: str, datos: list) -> None:
    """Guarda datos en un archivo JSON"""
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent=4)
