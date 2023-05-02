"""
Reto #7 - CONTANDO PALABRAS
Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
  - Los signos de puntuación no forman parte de la palabra.
  - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
  - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""

import string

text = "Hola, mi nombre es vidders. Mi nombre completo es Vidders SC (VidderSC)."

# Convertimos todas las palabras del texto a minúsculas
text = text.lower()
# Asignamos los signos de puntuación a la variable
punctuation = string.punctuation

# Creamos una variable para copiar el texto sin los signos de puntuación
text_no_punctuation = ""

for letter in text:
    # Comprobamos que la letra no sea un signo de puntuación y la añadimos al texto
    if letter not in punctuation:
        text_no_punctuation += letter

# La siguiente línea, hace exactamente lo mismo que el bucle for anterior pero optimizado.
# text_no_punctuation2 = text.translate(str.maketrans("", "", punctuation))

# Dividimos el texto y lo pasamos a una lista
text_lst = text_no_punctuation.split(" ")

# Creamos un diccionario para hacer el recuento
text_dict = {}

# Por cada palabra en la lista, la añadimos al diccionario con 
# el valor 1 y si ya existe, le sumamos 1.
for word in text_lst:
    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1

# Este bucle for hace exactamente lo mismo que el for anterior pero optimizado.
# for word in text_lst:
#     text_dict[word] = text_dict.get(word, 0) + 1

print(text_dict)
