continuar = "si"
planes = 0
planes18 = 0
descuento = 0
precio_bruto = 0
precio_total = 0
contador_mensual = 0
contador_trimestral = 0
contador_anual = 0
contador_mañana = 0
contador_tarde = 0
contador_anoche = 0
contador_efectivo = 0
contador_tarjeta = 0
contador_transferencia = 0
mayor_pago = 0

while continuar == "si":

    nombre = input("Nombre: ")

    tipo_plan = input("Tipo de plan(mensual, trimestral, anual): ")
    while tipo_plan != "mensual" and tipo_plan != "trimestral" and tipo_plan != "anual":
        tipo_plan = input("Error. Tipo de plan(mensual, trimestral, anual): ")

    edad = int(input("Edad(entre 12 y 80): "))
    while edad < 12 or edad > 80:
        edad = int(input("Error. Edad(entre 12 y 80): "))

    precio_plan = int(input("Precio del plan(mayor a 0): "))
    while precio_plan <= 0:
        precio_plan = int(input("Error. Precio del plan(mayor a 0): "))

    forma_pago = input("Forma de pago(efectivo, tarjeta, transferencia): ")
    while forma_pago != "efectivo" and forma_pago != "tarjeta" and forma_pago != "transferecia":
        forma_pago = input("Error. Forma de pago(efectivo, tarjeta, transferencia): ")

    turno = input("Turno(mañana, tarde, noche): ")
    while turno != "mañana" and turno != "tarde" and turno != "noche":
        turno = input("Error. Turno(mañana, tarde, noche): ")

    nuevo = input("Alumno nuevo(si,no): ")
    while nuevo != "si" and nuevo != "no":
        nuevo = input("Error. Alumno nuevo(si,no): ")

    planes += 1
    if edad < 18:
        planes18 += 1

    precio_bruto += precio_plan

    if nuevo == "si":
        descuento += 10
    if tipo_plan == "anual":
        descuento += -15
    resta = precio_plan * descuento / 100
    precio_plan = precio_plan - resta

    precio_total += precio_plan

    match tipo_plan:
        case "mensual":
            contador_mensual += 1
        case "trimestral":
            contador_trimestral += 1
        case _:
            contador_anual += 1

    match turno:
        case "mañana":
            contador_mañana += 1
        case "tarde":
            contador_tarde += 1
        case _:
            contador_anoche += 1

    match forma_pago:
        case "efectivo":
            contador_efectivo += 1
        case "tarjeta":
            contador_tarjeta += 1
        case _:
            contador_transferencia += 1

    if precio_plan > mayor_pago:
        mayor_pago = precio_plan
        mayor_nombre = nombre


    continuar = input("continuar?(si,no): ")

if planes > 50:
    descuento = 5
    resta = precio_total * descuento / 100
    precio_total = precio_total - resta

mayor_turno = contador_mañana
mensaje_turno = "mañana"
if contador_tarde > mayor_turno:
    mayor_turno = contador_tarde
    mensaje_turno = "tarde"
if contador_anoche > mayor_turno:
    mayor_turno = contador_anoche
    mensaje_turno = "anual"

mayor_pago = contador_efectivo
mensaje_pago = "efectivo"
if contador_tarjeta > mayor_pago:
    mayor_pago = contador_tarjeta
    mensaje_pago = "tarjeta"
if contador_transferencia > mayor_pago:
    mayor_pago = contador_transferencia
    mensaje_pago = "transferencia"

promedio_precio = precio_bruto / planes

print(
f'''
a. Total bruto: {precio_bruto}, Total final: {precio_total}
b. Cantidad de ventas de plan 
mensual: {contador_mensual} 
trimestral: {contador_trimestral} 
anual: {contador_anual}
c. Turno con mas clientes: {mensaje_turno}
d. {mayor_nombre} pago el plan mas caro
e. Promedio de precios de planes: {promedio_precio}
f. Forma de pago mas utilizada: {mensaje_pago}
g. Clientes menores de 18: {planes18}
'''
)