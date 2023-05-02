"""
Reto #5 - ASPECT RATIO DE UNA IMAGEN
Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
"""


from PIL import Image
import requests
from io import BytesIO

url = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'

# We get the image from the provided URL and convert it to an Image
with requests.get(url) as response:
    img = Image.open(BytesIO(response.content))

# We get the width and height from the retrived image
width, height = img.size
print("Width:", width)
print("Height:", height)


# Function to calculate the aspect ratio and reduce it to its minimum expression
def aspect_ratio(width, height):
    smaller = width
    if width > height:
        smaller = height

    dividend = 0
    divisor = 0

    for i in range(2, smaller):
        if width % i == 0 and height % i == 0:
            dividend = int(width / i)
            divisor = int(height / i)

    return f"{dividend}:{divisor}"


print(f"The aspect ratio is {aspect_ratio(width, height)}")