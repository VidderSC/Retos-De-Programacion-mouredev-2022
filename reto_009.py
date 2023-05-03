"""
Reto #9 - CÓDIGO MORSE
Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 - En morse se soporta raya "-", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
"""


# Generamos un diccionario con el alfabeto de texto a Morse
text_to_morse_dict = {
    "A":"·-",    "N":"-·",    "0":"-----",
    "B":"-···",  "Ñ":"--·--", "1":"·----",
    "C":"-·-·",  "O":"---",   "2":"··---",
    "CH":"----", "P":"·--·",  "3":"···--",
    "D":"-··",   "Q":"--·-",  "4":"····-",
    "E":"·",     "R":"·-·",   "5":"·····",
    "F":"··-·",  "S":"···",   "6":"-····",
    "G":"--·",   "T":"-",     "7":"--···",
    "H":"····",  "U":"··-",   "8":"---··",
    "I":"··",    "V":"···-",  "9":"----·",
    "J":"·---",  "W":"·--",   ".":"·-·-·-",
    "K":"-·-",   "X":"-··-",  ",":"--··--",
    "L":"·-··",  "Y":"-·--",  "?":"··--··",
    "M":"--",    "Z":"--··",  '"':"·-··-·",
    "/":"-··-·"}

# Generamos el diccionario opuesto al anterior, de Morse a Texto
morse_to_text_dict = {value: key for key, value in text_to_morse_dict.items()}


# Función para convertir el texto natural a Morse
def convert_to_morse(message):
    # Convertimos todas las letras a mayúsculas
    message = message.upper()

    # Obtenemos la longitud del mensaje
    length = len(message)

    # Inicializamos la variable con la traducción y el contador
    translated = ""
    i = 0

    # Mientras que "i" sea menor que la longitud del mensaje
    while i < length:
        # Verificamos en caso que sea "CH"
        if message[i] == "C" and message[i+1] == "H":
            translated += text_to_morse_dict["CH"]
            # Sumamos 1 al contador para saltarnos la "H"
            i += 1
            translated += " "
        # En caso que sea un espacio
        elif message[i] == " ":
            translated += "  "
        # En cualquier otro caso
        else:
            # Añadimos el valor de la letra correspondiente en el diccionario
            translated += text_to_morse_dict[message[i]]
            # Si el valor de "i" es distinto de la longitud - 1
            if i != length - 1:
                if message[i+1] != " ":
                    translated += " "
        # Sumamos 1 para incrementar el contador.
        i += 1
    # Imprimimos por consola el resultado.
    print(translated)


# Función para convertir de Morse a texto natural
def convert_from_morse(message):
    # Inicializamos la variable con la traducción
    translated = ""
    # Creamos una lista con los símbolos en Morse
    message_list = message.split(" ")
    
    # Recorremos por cada símbolo en la lista
    for symbol in message_list:
        # Si el simbolo está vacío, añadimos un espacio
        if symbol == "":
            translated += " "
        else:
            # Añadimos el valor del símbolo correspondiente en el diccionario
            translated += morse_to_text_dict[symbol]
    # Imprimimos por consola el resultado.
    print(translated)


# Solicitamos al usuario que introduzca un texto o código morse
print()
print("Introduce un mensaje (en texto o en código Morse):")
message = input()
print()
print("Traducción:")

# Comprobamos si es código Morse o texto natural.
if message[0] in {"·", "-"}:
    convert_from_morse(message)
else:
    convert_to_morse(message)
