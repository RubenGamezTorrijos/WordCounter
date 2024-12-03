###########################################
# Autor: Rubén Gámez Torrijos             #
# Analizador de texto interactivo         #
###########################################

import string
import json
import matplotlib.pyplot as plt
from collections import Counter
from rich.console import Console
from rich.table import Table

# Archivo JSON para almacenar palabras ingresadas
archivo_json = "palabras.json"

# Inicializar consola de Rich
console = Console()

# Cargar palabras desde el archivo JSON si existe
try:
    with open(archivo_json, "r") as archivo:
        palabras_totales = json.load(archivo)
except FileNotFoundError:
    palabras_totales = []

console.print("[bold green]===[ Analizador Interactivo de Palabras ]===[/bold green]")
console.print("Introduce palabras una a una para analizar estadísticas.")
console.print("Escribe '[bold red]salir[/bold red]' para terminar el programa.\n")

while True:
    entrada = input("Introduce una palabra: ").strip().lower()

    if entrada == "salir":
        console.print("[bold red]Saliendo del programa...[/bold red]")
        break

    # Ignorar entradas vacías
    if not entrada:
        console.print("[bold yellow]Por favor, ingresa una palabra válida.[/bold yellow]")
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
    console.print(f"\n[bold cyan]Total de palabras guardadas:[/bold cyan] {total_palabras}")
    console.print(f"[bold cyan]La palabra más frecuente:[/bold cyan] '{palabra_mas_frecuente[0]}' con {palabra_mas_frecuente[1]} apariciones.")

    # Crear una tabla bonita con Rich
    table = Table(title="Distribución de Palabras", title_style="bold magenta")
    table.add_column("Palabra", style="cyan", justify="center")
    table.add_column("Cantidad", style="green", justify="center")

    for palabra, cantidad in contador_palabras.items():
        table.add_row(palabra, str(cantidad))

    console.print(table)

    # Crear gráfico de pastel
    etiquetas = list(contador_palabras.keys())
    valores = list(contador_palabras.values())
    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=140)
    plt.title("Distribución de Palabras")
    plt.show()

