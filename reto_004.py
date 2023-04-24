"""
Reto #4 - ÁREA DE UN POLÍGONO
Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo.
"""


def area_poligon(tipo, base, altura=0):
    if tipo == "Triángulo":
        print(
            f"El área del {tipo} de base {base} y altura {altura} es {(base * altura) / 2}")
    elif tipo == "Rectángulo":
        print(
            f"El área del {tipo} de ancho {base} y alto {altura} es {(base * altura)}")
    elif tipo == "Cuadrado":
        print(f"El área del {tipo} de lado {base} es {(base ** 2)}")
    else:
        print("Tipo de polígono inválido. Solamente se acepta 'Triángulo', 'Cuadrado' o 'Rectángulo'")


area_poligon("Rectángulo", 3, 4)
area_poligon("Triángulo", 3, 4)
area_poligon("Cuadrado", 3)
area_poligon("Rombo", 3, 4)
