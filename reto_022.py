"""
Reto #22 - CONJUNTOS
Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes.
- Si el booleano es falso buscará y retornará los elementos no comunes.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

array_1: list = ["a", 1, "b", 2, "c", 3]
array_2: list = ["b", 3, "c", 1, "e", 2, "i", "o", "u"]


def elementos_comunes(array1: list, array2: list, es_verdadero: bool) -> list:
    # Si es verdadero, devolvemos los elementos comunes a ambos arrays.
    if es_verdadero:
        return [elemento for elemento in array1 if elemento in array2]

    # Si es falso, se hará lo siguiente:

    # Por cada elemento en el array1 que no se encuentra en el array2,
    # lo añadimos a la lista1.
    array_list1: list = [
        elemento for elemento in array1 if elemento not in array2]

    # Por cada elemento en el array2 que no se encuentra en el array1,
    # lo añadimos a la lista2.
    array_list2: list = [
        elemento for elemento in array2 if elemento not in array1]

    # Sumamos la lista1 y la lista2 y la devolvemos.
    return array_list1 + array_list2


print(elementos_comunes(array_1, array_2, True))
print(elementos_comunes(array_1, array_2, False))
