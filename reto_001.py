"""
Reto #1 - ¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne 
verdadero o falso (Boolean) según sean o no anagramas.

Un Anagrama consiste en formar una palabra reordenando TODAS las 
letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
"""


def is_anagram(word1, word2):
    # Comprobamos si es la misma palabra
    if word1 == word2:
        return False

    # Comprobamos si tienen la misma longitud
    if len(word1) != len(word2):
        return False

    # pasamos las palabras a minúsculas
    word1 = word1.lower()
    word2 = word2.lower()

    # Por cada letra en la palabra1, comprobamos si está en la palabra2
    for letter in word1:
        if letter not in word2:
            return False

    # Por cada letra en la palabra2, comprobamos si está en la palabra1 para evitar duplicados
    for letter in word2:
        if letter not in word1:
            return False

    # Si llegamos hasta aquí, quiere decir que son Anagramas
    return True


print(is_anagram("Magia", "Amiga"))  # True
print(is_anagram("word101", "word10"))  # False
print(is_anagram("word10", "word01"))  # True
