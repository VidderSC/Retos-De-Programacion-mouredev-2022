"""
Reto #6 - INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
  - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

texto = "Hola mundo"

# Obtenemos la longitud del texto y creamos una variable para el inverso
lenght = len(texto)
reverse = ""

# Hacemos un loop inverso para recorrer todo el texto
while lenght > 0:
    # Empezamos por el final
    lenght -= 1
    # Añadimos el último caracter a la variable en cada iteración
    reverse += texto[lenght]

print(reverse)