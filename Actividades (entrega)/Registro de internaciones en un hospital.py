continuar = "si"
pacientes = 0
pacientes10 = 0
descuento = 0
costo_bruto = 0
costo_total = 0
dias_total = 0
costo_dia_total = 0
contador_urgente = 0
contador_control = 0
contador_cirujia = 0
contador_efectivo = 0
contador_tarjeta = 0
contador_transferencia = 0
urgente_total = 0
control_total = 0
cirujia_total = 0
costo_mayor = 0

while continuar == "si":
    nombre = input("Nombre: ")

    edad = int(input("Edad(entre 0 y 100): "))
    while edad < 0 or edad > 100:
        edad = int(input("Error. Edad(entre 0 y 100): "))

    tipo_atencion = input("Tipo de atencion(urgencia, control, cirujia): ")
    while tipo_atencion != "urgencia" and tipo_atencion != "control" and tipo_atencion != "cirujia":
        tipo_atencion = input("Error. Tipo de atencion(urgencia, control, cirujia): ")

    dias = int(input("Cantidad de dias internado(entre 1 y 60): "))
    while dias < 1 or dias > 60:
        dias = int(input("Error. Cantidad de dias internado(entre 1 y 60): "))

    costo_dia = int(input("Costo por dia(mayor a 0): "))
    while costo_dia <= 0:
        costo_dia = int(input("Error. Costo por dia(mayor a 0): "))

    sexo = input("Sexo(M, F, NB): ")
    while sexo != "M" and sexo != "F" and sexo != "NB":
        sexo = int(input("Error. Sexo(M, F, NB): "))

    obra_social = input("Tiene obra social?(si,no): ")
    while obra_social != "si" and obra_social != "no":
        obra_social = input("Error. Tiene obra social?(si,no): ")

    forma_pago = input("Forma de pago(efectivo, tarjeta, transferencia): ")
    while forma_pago != "efectivo" and forma_pago != "tarjeta" and forma_pago != "transferecia":
        forma_pago = input("Error. Forma de pago(efectivo, tarjeta, transferencia): ")
    
    pacientes += 1
    if dias > 10:
        pacientes10 += 1

    costo = costo_dia * dias
    costo_bruto += costo
    dias_total += dias
    costo_dia_total += costo_dia

    if obra_social == "si":
        descuento = 20
        resta = costo * descuento / 100
        costo = costo - resta

    if costo > costo_mayor:
        costo_mayor = costo
        nombre_mayor = nombre

    costo_total += costo

    match tipo_atencion:
        case "urgencia":
            contador_urgente += 1
            urgente_total += dias
        case "control":
            contador_control += 1
            control_total += dias
        case _:
            contador_cirujia += 1
            cirujia_total += dias
    
    match forma_pago:
        case "efectivo":
            contador_efectivo += 1
        case "tarjeta":
            contador_tarjeta += 1
        case _:
            contador_transferencia += 1

    continuar = input("continuar?(si,no): ")

if dias_total > 500:
    descuento = 10
    resta = costo_total * descuento / 100
    costo_total = costo_total - resta

promedio_costo = costo_dia_total / pacientes

mayor_atencion = contador_urgente
mensaje_atencion = "urgencia"
if contador_control > mayor_atencion:
    mayor_atencion = contador_control
    mensaje_atencion = "control"
if contador_cirujia > mayor_atencion:
    mayor_atencion = contador_cirujia
    mensaje_atencion = "cirujia"

mayor_pago = contador_efectivo
mensaje_pago = "efectivo"
if contador_tarjeta > mayor_pago:
    mayor_pago = contador_tarjeta
    mensaje_pago = "tarjeta"
if contador_transferencia > mayor_pago:
    mayor_pago = contador_transferencia
    mensaje_pago = "transferencia"

print(
f'''
a. Total bruto por internaciones: {costo_bruto} Con descuentos aplicados: {costo_total}
b. Pacientes de urgencia: {contador_urgente} control: {contador_control} cirujia: {contador_cirujia}
c. Tipo de atención con mayor cantidad de días acumulados: {mensaje_atencion}
d. Paciente con mas costo de internacion: {nombre_mayor}
e. Promedio del costo por dia de todos los pacientes: {promedio_costo}
f. Forma de pago mas usada: {mensaje_pago}
g. Pacientes con mas de 10 dias de internacion: {pacientes10}
'''
)