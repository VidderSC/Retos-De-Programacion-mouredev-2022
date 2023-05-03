"""
Reto #8 - DECIMAL A BINARIO
Crea un programa se encargue de transformar un número decimal a binario,
sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

# Para convertir un número decimal a binario, tenemos que ir dividiendo
# el número entre 2 y escribir el resto (que es 0 o 1) cada vez.
# Seguimos haciendo esto hasta que lleguemos a 0.

number = int(input("Introduce un número entero: "))
binary = ""
binary_reversed = ""

while number != 0:
    binary_reversed += str(number % 2)
    number = number // 2

length = len(binary_reversed)

while length > 0:
    length -= 1
    binary += binary_reversed[length]

print(f"El valor en binario es: {binary}")