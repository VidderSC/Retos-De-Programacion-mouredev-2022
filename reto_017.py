"""
Reto #17 - LA CARRERA DE OBSTÁCULOS
Crea una función que evalúe si un/a atleta ha superado correctamente
una carrera de obstáculos.
  - La función recibirá dos parámetros:
      - Un array que sólo puede contener String con las palabras "run" o "jump"
      - Un String que represente la pista y sólo puede 
        contener "_" (suelo) o "|" (valla)
  - La función imprimirá cómo ha finalizado la carrera:
      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será
        correcto y no variará el símbolo de esa parte de la pista.
      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
      - Si hace "run" en "|" (valla), se variará la pista por "/".
 - La función retornará un Boolean que indique si ha superado la carrera.
   Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""

# Creamos la lista (array) que contiene las acciones del atleta
ATLETA = ["run", "run", "run", 
          "jump", "run", "jump", 
          "run", "run", "jump", 
          "run", "run", "run", 
          "jump", "run", "jump",
          "run", "run", "run",]

# Creamos otra lista para comprobar las diferencias
ATLETA2 = ["run", "jump", "run", 
           "jump", "run", "jump", 
           "run", "run", "run", 
           "run", "run", "run", 
           "jump", "run", "run",
           "run", "jump", "run"]

# creamos el string con la pista de obstáculos
PISTA = "___|_|__|___|_|___"


def main():
    print("Estado de la pista antes de iniciar la carrera: ")
    print(PISTA)
    print()
    # imprimimos el resultado de la carrera
    print(carrera(ATLETA, PISTA))
    print()

    # imprimimos el otro atleta para comprobar la diferencia en el resultado
    print("Estado de la pista antes de iniciar la carrera: ")
    print(PISTA)
    print()
    # imprimimos el resultado de la nueva carrera
    print(carrera(ATLETA2, PISTA))


# Definimos la función Carrera tal y como nos pide el enunciado
def carrera(atleta: list, pista: str) -> bool:
    # Comprobamos que las longitudes coincidan, para que no de error.
    if len(atleta) != len(pista):
        print("El número de acciones no coincide con la longitud de la pista.")
        return False
    
    # Asignamos la longitud de pista a una variable e inicializamos el índice
    length = len(pista)
    index = 0

    # Creamos el string que contendrá la nueva pista
    new_pista = ""

    # Bucle para recorrer todas las acciones y compararlas con la pista, 
    # e caso de no coincidir, se añade el simbolo requerido en el enunciado.
    while index < length:
        if atleta[index] == "run" and pista[index] == "|": 
            new_pista += "/"
        elif atleta[index] == "jump" and pista[index] == "_":
            new_pista += "x"
        else:
            new_pista += pista[index]
        index += 1

    print("Estado de la pista al finalizar la carrera:")
    print(new_pista)

    # Devolvemos verdadero si la nueva pista es igual a la pista original, 
    # en caso contrario devolvemos falso
    return new_pista == pista


# Comprobamos si tenemos que ejecutar el main o no.
if __name__ == "__main__":
    main()
