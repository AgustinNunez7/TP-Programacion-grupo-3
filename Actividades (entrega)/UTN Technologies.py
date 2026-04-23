contador_empleados = 0
contador_no_ia = 0

mayor_IA = 0
mayor_RV = 0
mayor_IOT = 0

for i in range(10):
    nombre = input("Nombre: ")
    
    edad = int(input("Edad(mayor a 18): "))
    while edad > 18:
        edad = int(input("Error. Edad(mayor a 18): "))
    
    genero = input("Genero(Masculino, Femenino, Otro): ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        input("Error. Genero(Masculino, Femenino, Otro): ")
    
    voto = input("Voto(IA,RV/RA,IOT): ")
    while voto != "IA" and voto != "RV/RA" and voto != "IOT":
        input("Error. Voto(IA,RV/RA,IOT): ")

    if genero == "Masculino" and (voto == "IA" or voto == "IOT") and (edad >= 25 and edad <= 50):
        contador_empleados += 1

    if voto != "IA" and genero != "Femenino" and (edad > 33 and edad < 40):
        contador_no_ia += 1

    if genero == "Masculino":
        if voto == "IA":
            if edad > mayor_IA:
                mayor_IA = edad
                nombre_IA = nombre
        elif voto == "RV/RA":
            if edad > mayor_RV:
                mayor_RV = edad
                nombre_RV = nombre
        else:
            if edad > mayor_IOT:
                mayor_IOT = edad
                nombre_IOT = nombre
    
porcentaje = contador_no_ia * 10 / 100

if mayor_IA == 0:
    mensaje_mayor_ia = "Nadie voto por IA"
else:
    mensaje_mayor_ia = f"{nombre_IA} de {mayor_IA} años, voto por IA"

if mayor_RV == 0:
    mensaje_mayor_rv = "Nadie voto por RV"
else:
    mensaje_mayor_rv = f"{nombre_RV} de {mayor_RV} años, voto por RV"

if mayor_IOT == 0:
    mensaje_mayor_iot = "Nadie voto por IOT"
else:
    mensaje_mayor_iot = f"{nombre_IOT} de {mayor_IOT} años, voto por IOT"


print(
f'''
1. Cantidad de empleados de género masculino que votaron por IOT o IA,
cuya edad esté entre 25 y 50 años inclusive: {contador_empleados}
2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
género no sea Femenino o su edad se encuentre entre los 33 y 40: {porcentaje}%
3. 
{mensaje_mayor_ia}
{mensaje_mayor_rv}
{mensaje_mayor_iot}
'''
)
        