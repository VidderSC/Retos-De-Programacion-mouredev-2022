"""
Reto #14 - ¿ES UN NÚMERO DE ARMSTRONG?
Escribe una función que calcule si un número dado es un número de 
Amstrong (o también llamado narcisista).
  - Si no conoces qué es un número de Armstrong, debes buscar 
    información al respecto.
"""

"""
Un número es Armstrong si la suma de cada uno de sus dígitos elevados a 
la cantidad de dígitos que tiene el número es igual al número en sí mismo.

Por ejemplo, el número 153 es un número Armstrong, ya que tiene tres dígitos y 
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
"""


# Creamos la función para determinar si es un número Armstrong
def is_armstrong(num):
    # convertimos el número a un string
    num_str = str(num)
    # Obtenemos la cantidad de dígitos
    length = len(num_str)
    suma = 0
    # Recorremos el num_str y calculamos
    for n in num_str:
        suma += int(n)**length
    # Si la suma es igual al número, devuelve Verdadero
    return suma == num


print(is_armstrong(153))