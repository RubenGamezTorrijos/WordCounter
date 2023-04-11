###########################################
# Autor: Rubén Gámez Torrijos             #
# Analizador de texto, palabras, y letras #
###########################################


import string

texto = input("Ingresa el texto a analizar: ")

# Elimina signos de puntuación del texto
texto = texto.translate(str.maketrans('', '', string.punctuation))

palabras = texto.split()
cantidad_palabras = len(palabras)

cantidad_caracteres = len(texto)

frecuencia_letras = {}
for letra in texto:
    if letra in frecuencia_letras:
        frecuencia_letras[letra] += 1
    else:
        frecuencia_letras[letra] = 1

frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print("Cantidad de palabras:", cantidad_palabras)
print("Cantidad de caracteres:", cantidad_caracteres)
print("Frecuencia de letras:")
for letra, frecuencia in frecuencia_letras.items():
    print(letra, "-", frecuencia)
print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(palabra, "-", frecuencia)
