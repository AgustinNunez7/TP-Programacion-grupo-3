ventas = 25
descuento = 0
unidades_total = 0
precio_total = 0
precio_unitario_total = 0

precio_mayor = 0

contador_efectivo = 0
contador_tarjeta = 0
contador_transferecia = 0 

for i in range(ventas):
    tipo_producto = input("Tipo de producto(alimento, limpieza, perfumeria): ")
    while tipo_producto != "alimento" and tipo_producto != "limpieza" and tipo_producto != "perfumeria":
        tipo_producto = input("Error. Tipo de producto(alimento, limpieza, perfumeria): ")

    pago = input("Forma de pago(efectivo, tarjeta, transferencia,): ")
    while pago != "alimento" and pago != "limpieza" and pago != "perfumeria":
        pago = input("Error. Forma de pago(efectivo, tarjeta, transferencia,): ")

    unidades = int(input("Cantidad de unidades(1-20): "))
    while unidades < 1 or unidades > 20:
        unidades = int(input("Error. Cantidad de unidades(1-20): "))

    precio_unitario = int(input("Precio unitario(mayor a 0): "))
    while precio_unitario < 0:
        precio_unitario = int(input("Error. Precio unitario(mayor a 0): "))

    unidades_total += unidades
    precio = unidades * precio_unitario
    precio_unitario_total += precio_unitario

    if pago == "tarjeta":
        contador_tarjeta += 1

        descuento = 5
        resta = precio * descuento / 100
        precio_total = precio - resta

        if precio > precio_mayor:
            precio_mayor = precio

    elif pago == "efectivo":
        contador_efectivo += 1

    else:
        contador_transferecia += 1
            
    precio_total += precio

promedio_unitario = precio_unitario / ventas
precio_bruto = precio_total

if unidades_total > 200:
    descuento = 10
elif unidades_total > 400:
    descuento = 20

if descuento != 0:
    resta = precio_total * descuento / 100
    precio_total = precio_total - resta

contador_mayor = contador_tarjeta
mensaje_pago_mayor = "Se pago mas con tarjeta"
if contador_efectivo > contador_mayor:
    mensaje_pago_mayor = "Se pago mas en efectivo"
if contador_transferecia > contador_mayor:
    mensaje_pago_mayor = "Se pago mas por transferencia"

print(
f'''
1.Precio BRUTO: {precio_bruto}
2.Importe total final: {precio_total}
3.Venta mas cara con tarjeta: {precio_mayor}
4.Promedio de precio unitario: {promedio_unitario}
5.{mensaje_pago_mayor}
'''
)