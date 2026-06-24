from juego.preguntas import preguntas

def jugar_preguntados():
    puntaje = 0

    print("\n=== PREGUNTADOS ===")
    print("Ingrese 'S' para salir del juego.\n")

    for pregunta in preguntas:

        print("\n" + pregunta["pregunta"])

        for opcion in pregunta["opciones"]:
            print(opcion)

        respuesta = input("Respuesta: ").upper()

        if respuesta == "S":
            print("Juego abandonado.")
            break

        if respuesta == pregunta["correcta"]:
            print("¡Correcto!")
            puntaje += 10
        else:
            print(f"Incorrecto. La respuesta correcta era {pregunta['correcta']}")

    print(f"\nPuntaje final: {puntaje}")

    return puntaje

jugar_preguntados()