continuar = "si"
alquileres = 0
descuento = 0
kilometros_total = 0
precio_bruto = 0
contador_tarjeta = 0
contador_auto = 0
contador_moto = 0
contador_camioneta = 0
auto_total = 0
moto_total = 0
camioneta_total = 0
mayor_dias = 0
mayor_importe = 0

while continuar == "si":

    nombre = input("Nombre: ")

    tipo_vehiculo = input("Tipo de vehiculo(auto, camioneta, moto): ")
    while tipo_vehiculo != "auto" and tipo_vehiculo != "camioneta" and tipo_vehiculo != "moto":
        tipo_vehiculo = input("Error. Tipo de vehiculo(auto, camioneta, moto): ")

    dias = int(input("Cantidad de dias de alquiler(entre 1 y 30): "))
    while dias < 1 or dias > 30:
        dias = int(input("Error. Cantidad de dias de alquiler(entre 1 y 30): "))

    precio_dia = int(input("Precio por dia(mayor a 0): "))
    while precio_dia <= 0:
        precio_dia = int(input("Error. Precio por dia(mayor a 0): "))

    kilometros = int(input("Kilometros recorridos(entre 0 y 5000): "))
    while kilometros < 0 or kilometros > 5000:
        kilometros = int(input("Error. Kilometros recorridos(entre 0 y 5000): "))

    forma_pago = input("Forma de pago(efectivo, tarjeta, transferencia): ")
    while forma_pago != "efectivo" and forma_pago != "tarjeta" and forma_pago != "transferecia":
        forma_pago = input("Error. Forma de pago(efectivo, tarjeta, transferencia): ")

    frecuente = input("Cliente frecuente(si,no): ")
    while frecuente != "si" and frecuente != "no":
        frecuente = input("Error. Cliente frecuente(si,no): ")
    
    alquileres += 1

    precio = precio_dia * dias
    kilometros_total += kilometros
    precio_bruto += precio

    if frecuente == "si":
        descuento += 15
    if tipo_vehiculo == "camioneta":
        descuento += -20
    resta = precio * descuento / 100
    precio = precio - resta

    match tipo_vehiculo:
        case "auto":
            contador_auto += 1
            auto_total += kilometros
        case "moto":
            contador_moto += 1
            moto_total += kilometros
        case _:
            contador_camioneta += 1
            camioneta_total += kilometros

    if forma_pago == "tarjeta":
        contador_tarjeta += 1

    if dias > mayor_dias:
        mayor_dias = dias
        mayor_nombre = nombre

    if precio > mayor_importe:
        mayor_importe = precio
        mayor_estafado = nombre


    continuar = input("continuar?(si,no): ")

if kilometros_total > 20000:
    descuento = -10
    resta = precio_bruto * descuento / 100
    precio_final = precio_bruto - resta

mayor_vehiculo = contador_auto
mensaje_vehiculo = "auto"
if contador_moto > mayor_vehiculo:
    mayor_vehiculo = contador_moto
    mensaje_vehiculo = "moto"
if contador_camioneta > mayor_vehiculo:
    mayor_vehiculo = contador_camioneta
    mensaje_vehiculo = "camioneta"

mayor_kilometro = auto_total
mensaje_kilometro = "auto"
if moto_total > mayor_kilometro:
    mayor_kilometro = moto_total
    mensaje_kilometro = "moto"
if camioneta_total > mayor_kilometro:
    mayor_kilometro = camioneta_total
    mensaje_kilometro = "camioneta"

promedio_km = kilometros_total / alquileres

print(
f'''
a. Precio bruto: {precio_bruto} Total final: {precio_final}
b. Tipo de vehiculo con mayor cantidad de alquileres: {mensaje_vehiculo}
c. Nombre de cliente que mas dias alquilo: {mayor_dias}
d. Promedio de kilometros recorridos: {promedio_km}
e. Vehiculo que acumulo mas kilometros: {mayor_kilometro}
f. Alquileres pagados con tarjeta: {contador_tarjeta}
g. {mayor_estafado} tuvo el alquiler de mas importe con {mayor_importe}
'''
)