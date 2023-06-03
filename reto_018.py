"""
Reto #18 - TRES EN RAYA
Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y 
retorne lo siguiente:
- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es 
  correcta. O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta. Se podría representar 
con un vacío "", por ejemplo.
"""

matriz: list = [
    ["","O","X"],
    ["O","X",""],
    ["X","",""],
]

def main():
    print(analizar_tres_en_raya(matriz))


# Definimos una función que analice la matriz y determine el resultado.
def analizar_tres_en_raya(matrix: list) -> str:
    """
    Analiza una matriz 3x3 del juego "Tres en Raya" y determina el resultado.

    Args:
        matriz (list): Matriz 3x3 compuesta por "X", "O" y/o elemento vacío "".

    Returns:
        str: El resultado del juego. Puede ser "X" si han ganado las "X",
             "O" si han ganado las "O", "Empate" si ha habido un empate,
             "Nulo" si la proporción de "X" u "O" en la matriz no es correcta o
             si ambos jugadores han ganado.

    Examples:
        >>> matriz = [
        ...     ["O", "O", ""],
        ...     ["", "X", "O"],
        ...     ["X", "X", "X"],
        ... ]
        >>> resultado = analizar_tres_en_raya(matriz)
        >>> print(resultado)
        X         
    

    """

    # Verificamos las filas
    for line in matrix:
        if line[0] != "" and line[0] == line[1] == line[2]:
            return line[0]

    # Verificamos las columnas
    for index in range(3):
        if matrix[0][index] != "" and \
            matrix[0][index] == matrix[1][index] == matrix[2][index]:
            return matrix[0][index]

    # Verificamos las diagonales
    if matrix[0][0] != "" and matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return matrix[0][0]

    if matrix[2][0] != "" and matrix[2][0] == matrix[1][1] == matrix[0][2]:
        return matrix[2][0]

    # Verificamos si hay empate, para ello contamos y sumamos todos los casos
    # en que haya un elemento vacío "".
    elementos_no_vacios: int = sum(row.count("") for row in matriz)
    if elementos_no_vacios == 0:
        return "Empate"

    # En caso que no haya ocurrido nada de lo anterior, 
    # suponemos que el resultado es nulo.
    return "Nulo"


if __name__ == "__main__":
    main()
