class Ruta:
    def __init__(self, nombre, distancia, tiempo, congestion):
        self.nombre = nombre
        self.distancia = distancia
        self.tiempo = tiempo
        self.congestion = congestion
    
    def indice_conveniencia(self):
        if self.congestion == "alto":
            return self.distancia * 2.0
        elif self.congestion == "medio":
            return self.distancia * 1.5
        else:
            return self.distancia * 1.0

ruta_principal = Ruta("Blanco Galindo", 5, 20, "alto")
ruta_alternativa = Ruta("Alternativa 1", 6, 18, "medio")

rutas_avenidas = {}

rutas_avenidas["Av. Blanco Galindo"] = [ruta_principal, ruta_alternativa]

rutas_avenidas["Av. America"] = [
    Ruta("America Central", 4, 15, "bajo"),
    Ruta("America Norte", 6, 20, "medio")
]

rutas_avenidas["Av. Ayacucho"] = [
    Ruta("Ayacucho Sur", 7, 25, "alto"),
    Ruta("Ayacucho Norte", 5, 22, "medio")
]

print("Ruta principal:")
print("Nombre:", ruta_principal.nombre)
print("Distancia:", ruta_principal.distancia, "km")
print("Tiempo estimado:", ruta_principal.tiempo, "min")
print("Congestion:", ruta_principal.congestion)
print("Indice conveniencia:", ruta_principal.indice_conveniencia())

print()

print("Ruta alternativa:")
print("Nombre:", ruta_alternativa.nombre)
print("Distancia:", ruta_alternativa.distancia, "km")
print("Tiempo estimado:", ruta_alternativa.tiempo, "min")
print("Congestion:", ruta_alternativa.congestion)
print("Indice conveniencia:", ruta_alternativa.indice_conveniencia())

print()

print("Todas las rutas por avenida:")
for avenida, lista_rutas in rutas_avenidas.items():
    print("Avenida:", avenida)
    for ruta in lista_rutas:
        print("  -", ruta.nombre, "| Indice:", ruta.indice_conveniencia())