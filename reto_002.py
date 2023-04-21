"""
Reto #2 - LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión 
de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números en la que el 
siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""


# Creamos la funcion y acepta un parámetro opcional para indicar cuantos números
# de la sucesión se quieren imprimir, serán 50 por defecto si no se indica nada.
def fibonacci(lenght=50):
    # Iniciamos las variables
    num_a = 0
    num_b = 1

    # Bucle para recorrer los 50 primeros números empezando en 0.
    for i in range(0, lenght):
        # Imprimimos el primer valor
        print(num_a)
        # Creamos una variable para transicionar
        temp = num_a + num_b
        # Intercambiamos los valores para mantener siempre los dos anteriores.
        num_a = num_b
        num_b = temp


# Llamamos a la funcion sin pasar un parámetro.
fibonacci()
