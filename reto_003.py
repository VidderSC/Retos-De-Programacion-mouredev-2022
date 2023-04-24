"""
Reto #3 - ¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""


# Un número Primo es aquel que solamente se puede dividir por si mismo o por 1.
# El 1 no se considera como un número Primo.


# Función que determina si un número es Primo o no, devuelve True o False.
def is_prime(num):
    # Si el número es 2 o 3, devolvemos verdadero.
    if num == 2 or num == 3:
        return True
    # Si el número es divisible por 2 o por 3, o es el 1, devolvemos falso.
    if num % 2 == 0 or num % 3 == 0 or num == 1:
        return False
    # Al no cumplirse lo anterior, devolvemos verdadero
    return True


# Bucle para recorrer todos los números entre el 1 y el 100
for i in range(1, 101):
    # Si el numero es primo, lo imprimimos por consola
    if is_prime(i):
        print(i)
