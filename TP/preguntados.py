import json
from random import randint
from datetime import datetime
from persistencia import cargar_datos, guardar_datos

def jugar_preguntados(usuario_id: int = 0, usuario_nombre: str = "Invitado", usuario_email: str = ""):
    """Juego de preguntas con selección aleatoria"""
    preguntas = cargar_datos("TP/preguntas.json")
    puntaje = 0
    preguntas_jugadas = []
    
    print("\n=============== PREGUNTADOS ===============")
    print("Ingrese la letra (A, B, C, D) o 'S' para salir.\n")
    
    while len(preguntas_jugadas) < len(preguntas):
        # Seleccionar una pregunta aleatoria que no se haya jugado
        indice = randint(0, len(preguntas) - 1)
        
        # Verificar si ya fue jugada
        for i in range(len(preguntas_jugadas)):
            if preguntas_jugadas[i] == indice:
                break
        else:
            preguntas_jugadas.append(indice)
            pregunta = preguntas[indice]
            
            # Mostrar la pregunta
            print("\n" + pregunta["pregunta"])
            
            # Mostrar opciones con letras
            letras = ["A", "B", "C", "D"]
            for i in range(len(pregunta["opciones"])):
                opcion = pregunta["opciones"][i]
                print(f"{letras[i]}) {opcion}")
            
            # Obtener respuesta del usuario
            respuesta = input("\nRespuesta: ")
            
            if respuesta == "S" or respuesta == "s":
                print("\nJuego abandonado.")
                break
            
            # Validar y convertir a índice
            indice_respuesta = -1
            if respuesta == "A" or respuesta == "a":
                indice_respuesta = 0
            elif respuesta == "B" or respuesta == "b":
                indice_respuesta = 1
            elif respuesta == "C" or respuesta == "c":
                indice_respuesta = 2
            elif respuesta == "D" or respuesta == "d":
                indice_respuesta = 3
            
            if indice_respuesta != -1:
                respuesta_correcta = pregunta["respuesta"]
                
                # Verificar si es correcta
                if indice_respuesta == respuesta_correcta:
                    print("¡Correcto!")
                    puntaje += pregunta["puntaje"]
                else:
                    respuesta_texto = pregunta["opciones"][respuesta_correcta]
                    print(f"Incorrecto. La respuesta correcta era {letras[respuesta_correcta]}) {respuesta_texto}")
            else:
                print("Opción inválida. Intente de nuevo.")
                preguntas_jugadas.pop()
    
    print(f"\n=== PUNTAJE FINAL: {puntaje} ===\n")
    
    # Guardar puntaje si el usuario está logueado
    if usuario_id != 0:
        guardar_puntaje_usuario(usuario_id, usuario_nombre, usuario_email, puntaje)
    
    return puntaje

def guardar_puntaje_usuario(usuario_id: int, usuario_nombre: str, usuario_email: str, puntaje: int, juego: str = "preguntados") -> None:
    """Guarda el puntaje del usuario si es mayor al registrado"""
    puntajes = cargar_datos("TP/puntajes.json")
    puntaje_existente = -1
    indice_puntaje = -1
    
    # Buscar si ya existe puntaje para este usuario en este juego
    for i in range(len(puntajes)):
        if puntajes[i]["usuario_id"] == usuario_id and puntajes[i]["juego"] == juego:
            puntaje_existente = puntajes[i]["puntaje"]
            indice_puntaje = i
            break
    
    # Guardar solo si es mayor al anterior o si no existe
    if puntaje_existente == -1 or puntaje > puntaje_existente:
        nuevo_puntaje = {
            "usuario_id": usuario_id,
            "nombre": usuario_nombre,
            "email": usuario_email,
            "juego": juego,
            "puntaje": puntaje,
        }
        
        if indice_puntaje != -1:
            puntajes[indice_puntaje] = nuevo_puntaje
        else:
            puntajes.append(nuevo_puntaje)
        
        guardar_datos("TP/puntajes.json", puntajes)