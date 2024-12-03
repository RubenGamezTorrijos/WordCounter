###########################################
# Autor: Rubén Gámez Torrijos             #
# Analizador de texto interactivo         #
###########################################

import string
import json
import matplotlib.pyplot as plt
from collections import Counter

# Archivo JSON para almacenar palabras ingresadas
archivo_json = "palabras.json"

# Cargar palabras desde el archivo JSON si existe
try:
    with open(archivo_json, "r") as archivo:
        palabras_totales = json.load(archivo)
except FileNotFoundError:
    palabras_totales = []

print("=== Analizador Interactivo de Palabras ===")
print("Ingresa palabras una a una para analizar estadísticas.")
print("Escribe 'salir' para terminar.")

while True:
    entrada = input("Ingresa una palabra: ").strip().lower()

    if entrada == "salir":
        print("Saliendo del programa...")
        break

    # Ignorar entradas vacías
    if not entrada:
        print("Por favor, ingresa una palabra válida.")
        continue

    # Eliminar signos de puntuación
    entrada = entrada.translate(str.maketrans('', '', string.punctuation))
    
    # Agregar la palabra a la lista y guardar en JSON
    palabras_totales.append(entrada)
    with open(archivo_json, "w") as archivo:
        json.dump(palabras_totales, archivo, indent=4)

    # Calcular estadísticas
    contador_palabras = Counter(palabras_totales)
    total_palabras = sum(contador_palabras.values())
    palabra_mas_frecuente = contador_palabras.most_common(1)[0]

    # Mostrar estadísticas
    print(f"\nTotal de palabras ingresadas: {total_palabras}")
    print(f"La palabra más frecuente es '{palabra_mas_frecuente[0]}' con {palabra_mas_frecuente[1]} apariciones.")
    print("Distribución porcentual de palabras:")
    for palabra, cantidad in contador_palabras.items():
        porcentaje = (cantidad / total_palabras) * 100
        print(f"- {palabra}: {cantidad} ({porcentaje:.2f}%)")

    # Crear gráfico de pastel
    etiquetas = list(contador_palabras.keys())
    valores = list(contador_palabras.values())
    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=140)
    plt.title("Distribución de Palabras")
    plt.show()

