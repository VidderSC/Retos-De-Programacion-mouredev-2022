"""
Reto #21 - CALCULADORA .TXT
Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
- El .txt se corresponde con las entradas de una calculadora.
- Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
- Soporta números enteros y decimales.
- Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
- El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
- Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
"""

lineas: list = list()
a: float = -1
operador: str = ""

try:
    with open("challenge21.txt") as file:
        lineas = file.read().split("\n")
except FileNotFoundError as e:
    print(f"Ha dado el siguiente error al intentar abrir el fichero: {e}")

length: int = len(lineas)
index: int = 1

if lineas[0] in ("+", "-", "*", "/"):
    raise TypeError("El primer valor debe ser numérico.")
elif lineas[0].isnumeric():
    a = float(lineas[0])
else:
    raise TypeError("El valor debe ser numérico.")

while index < length:
    if lineas[index] in ("+", "-", "*", "/"):
        operador = lineas[index]
        index += 1
        continue
    elif lineas[index].isnumeric():
        b = float(lineas[index])
        index += 1
    else:
        raise TypeError("El valor debe ser numérico.")

    if a >= 0 and b >= 0 and operador != "":
        match operador:
            case "+":
                a = a + b
                operador = ""
            case "-":
                a = a - b
                operador = ""
            case "*":
                a = a * b
                operador = ""
            case "/":
                a = a / b
                operador = ""

print(f"El resultado de las operaciones es: {a}")
