""" 
Reto #12 - ¿ES UN PALÍNDROMO?
Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
 - Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
 - NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 - Ejemplo: Ana lleva al oso la avellana.
"""
import string

# Creamos un diccionario con las tildes
tildes_dict = {"á": "a", "é": "e", "í":"i", "ó":"o", "ú":"u"}
# Creamos la variable con los signos de puntuación y añadimos el espacio
signos_punct = string.punctuation + " "


# Definimos la función que va a devolver Verdadero o Falso
def is_palindromo(frase):
    # Pasamos la frase a minúsculas
    frase = frase.lower()
    # Quitamos los signos de puntuacion y los espacios
    frase_filtrada = "".join([c for c in frase if c not in signos_punct])
    frase_sin_acentos = ""
    # Quitamos los acentos en caso que los haya
    for c in frase_filtrada:
        if c in tildes_dict:
            frase_sin_acentos += tildes_dict[c]
        else:
            frase_sin_acentos += c
    # Si la frase es igual a su reverso devolvemos Verdadero
    if frase_sin_acentos == frase_sin_acentos[::-1]:
        return True
    # En cualquier otro caso, devolvemos Falso
    return False


print(is_palindromo("Ana lleva al oso la avellana"))