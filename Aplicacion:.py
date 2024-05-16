import math

# Función para calcular la distancia entre dos ciudades en kilómetros
def calcular_distancia(ciudad_origen, ciudad_destino):
    # Simulando la distancia entre Santiago y Ovalle
    distancia_km = 378.5
    return distancia_km

# Función para calcular la duración del viaje en horas, minutos y segundos
def calcular_duracion(distancia_km, velocidad_promedio):
    tiempo_horas = distancia_km / velocidad_promedio
    tiempo_minutos = tiempo_horas * 60
    tiempo_segundos = tiempo_minutos * 60
    return tiempo_horas, tiempo_minutos, tiempo_segundos

# Función para calcular el combustible requerido para el viaje
def calcular_combustible(distancia_km, consumo_litros_por_km):
    combustible_litros = distancia_km * consumo_litros_por_km
    return combustible_litros

# Función para imprimir la narrativa del viaje
def imprimir_narrativa(ciudad_origen, ciudad_destino, distancia_km, duracion_horas, duracion_minutos, duracion_segundos, combustible_litros):
    print("\nNarrativa del viaje:")
    print(f"Viaje desde {ciudad_origen} hasta {ciudad_destino}:")
    print(f" - Distancia: {distancia_km:.2f} km")
    print(f" - Duración del viaje: {int(duracion_horas):02d} horas, {int(duracion_minutos):02d} minutos, {int(duracion_segundos):02d} segundos")
    print(f" - Combustible requerido: {combustible_litros:.2f} litros\n")

# Función principal del programa
def main():
    velocidad_promedio = 80  # Velocidad promedio en km/h
    consumo_litros_por_km = 0.08  # Consumo de combustible en litros por km

    while True:
        ciudad_origen = input("Ingrese la ciudad de origen (o 'q' para salir): ")
        if ciudad_origen.lower() == 'q':
            print("¡Hasta luego!")
            break
        
        ciudad_destino = input("Ingrese la ciudad de destino: ")

        distancia_km = calcular_distancia(ciudad_origen, ciudad_destino)
        duracion_horas, duracion_minutos, duracion_segundos = calcular_duracion(distancia_km, velocidad_promedio)
        combustible_litros = calcular_combustible(distancia_km, consumo_litros_por_km)

        imprimir_narrativa(ciudad_origen, ciudad_destino, distancia_km, duracion_horas, duracion_minutos, duracion_segundos, combustible_litros)

# Llamada a la función principal del programa
if __name__ == "__main__":
    main()