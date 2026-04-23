continuar = "si"
contador_especifico = 0
contador_jugadores = 0
contador_experto = 0
contador_avanzado = 0
contador_elite = 0
contador_plano = 0
contador_liftado = 0
contador_cortado = 0 
edad_total = 0
menor_edad = 0
flag_menor = False


while continuar == "si":
    nombre = input("Nombre: ")
    
    edad = int(input("Edad: "))
    while edad <= 0:
        edad = int(input("Error. Edad: "))

    puntos = int(input("Cantidad de puntos: "))
    while puntos < 0 or puntos > 60:
        puntos = int(input("Error. Cantidad de puntos: "))

    partidos_ganados = int(input("Numero de partidos ganados: "))
    while partidos_ganados < 0 or partidos_ganados > 35:
        partidos_ganados = int(input("Error. Numero de partidos ganados: "))

    tipo_saque = input("Tipo de saque(plano, liftado, cortado): ")
    while tipo_saque != "plano" and tipo_saque != "liftado" and tipo_saque != "cortado":
        tipo_saque = input("Error. Tipo de saque(plano, liftado, cortado): ")

    categoria = input("Categoria(elite, experto, avanzado): ")
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("Error. Categoria(elite, experto, avanzado): ")

    contador_jugadores += 1

    if categoria == "elite":
        if tipo_saque == "plano" and (edad >= 19 and edad <= 25):
            contador_especifico += 1
        
        if tipo_saque == "plano":
            contador_plano += 1
        elif tipo_saque == "liftado":
            contador_liftado += 1
        else:
            contador_cortado += 1


    elif categoria == "experto":
        contador_experto += 1

    else:
        contador_avanzado += 1
        edad_total += edad

    if flag_menor == False:
        flag_menor = True
        menor_edad = edad
        menor_categoria = categoria
        menor_nombre = nombre
    elif edad < menor_edad and puntos > 50:
        menor_edad = edad
        menor_categoria = categoria
        menor_nombre = nombre

    continuar = input("Continuar?(si, no): ")

porcentaje_experto = contador_experto * contador_jugadores / 100
promedio_avanzado = edad_total / contador_avanzado

saque_superior = contador_plano
saque_mensaje = "plano"
if contador_liftado > saque_superior:
    saque_superior = contador_liftado
    saque_mensaje = "liftado"
if contador_cortado > saque_superior:
    saque_superior = contador_cortado
    saque_mensaje = "cortado"

print(
f'''
1. Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
inclusive: {contador_especifico}
2. {menor_nombre} de categoria {menor_categoria} es el menor con {menor_edad} años
3. Jugadores de categoria experto: {porcentaje_experto}%
4. Promedio de edad de categoria avanzado: {promedio_avanzado}
5. Saque mas usado entre los elite: {saque_mensaje}
'''
)



    
    
