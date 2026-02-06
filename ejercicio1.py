def analizar_flujo(datos, limite):
    hora_mas_transito = 0
    for i in range(len(datos)):
        if datos[i] > datos[hora_mas_transito]:
            hora_mas_transito = i
    
    suma = 0
    for valor in datos:
        suma = suma + valor
    promedio = suma / len(datos)
    
    horas_altas = []
    for i in range(len(datos)):
        if datos[i] > limite:
            horas_altas.append(i)
    
    return hora_mas_transito, promedio, horas_altas

flujo = [50, 120, 300, 450, 500, 480, 400, 350, 300, 200, 150, 100, 80, 60]
umbral = 300

resultado = analizar_flujo(flujo, umbral)

print("Hora con mas trafico:", resultado[0])
print("Hora real:", resultado[0] + 6, ":00")
print("Promedio de vehiculos:", round(resultado[1], 2))
print("Horas con trafico sobre", umbral, ":", resultado[2])