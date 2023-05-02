"""
Reto #5 - ASPECT RATIO DE UNA IMAGEN
Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
"""


from PIL import Image
import requests
from io import BytesIO
import math

url = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'

# Obtenemos la imagen de la url y la convertimos a una imagen que PIL entienda
with requests.get(url) as response:
    img = Image.open(BytesIO(response.content))

# Obtenemos el ancho y alto de la imagen
width, height = img.size
print("Width:", width)
print("Height:", height)


# Función que calcula el aspect ratio y lo reduce a la mínima expresión
def aspect_ratio(width, height):
    # Encontramos cual es el más pequeño de los dos
    smaller = min(width, height)
    # Comprobamos todos los posibles divisores (podemos parar en "smaller // 2 + 1",
    # porque algo más largo que eso resultaría en un cociente más pequeño.
    for i in range(2, smaller // 2 + 1):
        if width % i == 0 and height % i == 0:
            # Si encontramos un común divisor, calculamos el ratio simplificado
            gcd = math.gcd(width, height)
            dividend, divisor = width // gcd, height // gcd
            return f"{dividend}:{divisor}"
    # Si no encontramos un divisor común, devolvemos el ratio original
    gcd = math.gcd(width, height)
    dividend = width // gcd
    divisor = height // gcd
    return f"{dividend}:{divisor}"


print(f"The aspect ratio is {aspect_ratio(width, height)}")