"""
Reto #16 - EN MAYÚSCULA
Crea una función que reciba un String de cualquier tipo y se encargue de poner
en mayúscula la primera letra de cada palabra.
 - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

# Creo un diccionario de correspondencia de minúsculas a mayúsculas.
dict_min_may = {
    "a": "A", "b": "B", "c": "C",
    "d": "D", "e": "E", "f": "F",
    "g": "G", "h": "H", "i": "I",
    "j": "J", "k": "K", "l": "L", 
    "m": "M", "n": "N", "ñ": "Ñ",
    "o": "O", "p": "P", "q": "Q",
    "r": "R", "s": "S", "t": "T",
    "u": "U", "v": "V", "w": "W",
    "x": "X", "y": "Y", "z": "Z",
    "á": "Á", "é": "É", "í": "Í",
    "ó": "Ó", "ú": "Ú",
}


def main():
    # Pedimos al usuario un texto
    text = input("Introduce un texto: ")

    print("El texto con la primera letra de cada palabra que has pasado es:")
    print(to_title(text))


# Creamos la función para pasar la primera letra de cada palabra a mayúsculas
# todo esto sin usar la funciones que vienen por defecto en Python.
def to_title(text):
    # Obtenemos la longitud del texto para iterarlo
    length = len(text)

    # Creamos una variable para guardar el nuevo texto
    new_text =""

    # Comprobamos el primer carácter para convertirlo a mayúsculas.
    if text[0] in dict_min_may:
        new_text = dict_min_may[text[0]]
    else:
        # si no está en el diccionario, lo pasamos directamente
        new_text = text[0]

    # Recorremos el texto proporcionado desde la posición 1
    for index in range(1, length):
        # Si el carácter anterior al que leemos no está en el diccionario y 
        # el carácter actual sí, pasamos la mayúscula de este.
        if text[index-1] not in dict_min_may and text[index-1] not in dict_min_may.values() and text[index] in dict_min_may:
            new_text += dict_min_may[text[index]]
        # de lo contrario pasamos el mismo carácter.
        else:
            new_text += text[index]

    return new_text


if __name__ == "__main__":
    main()