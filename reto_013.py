"""
Reto #13 - FACTORIAL RECURSIVO
Escribe una función que calcule y retorne el factorial de
un número dado de forma recursiva.
"""

"""
El factorial de un número es el resultado de multiplicar ese número por todos
los números enteros positivos que son menores que él.

Por ejemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""


# Creamos la funcion que calcula el factorial de un número
def factorial(num):
    i = num
    while i > 1:
        i -= 1
        num *= i
    return num


# Creamos un loop que se va a repetir infinitamente hasta que lo rompamos.
while True:
    # Pedimos el número a calcular y verificamos que sea un número válido.
    num = input("Introduce un número Entero para calcular su factorial: ")
    if num.isdecimal():
        num = int(num)
        if num > 0:
            # como es válido, rompemos el loop
            break
    # En cualquier otro caso, informamos de lo que necesitamos.
    print("Tiene que ser un número entero positivo mayor que 0.")

print(f"{num}! = {factorial(num)}")