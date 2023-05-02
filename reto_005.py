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

# We get the image from the provided URL and convert it to an Image
with requests.get(url) as response:
    img = Image.open(BytesIO(response.content))

# We get the width and height from the retrived image
width, height = img.size
print("Width:", width)
print("Height:", height)


# Function to calculate the aspect ratio and reduce it to its minimum expression
def aspect_ratio(width, height):
    # Find the smaller of the two
    smaller = min(width, height)
    # Check all possible divisors (we can stop at "smaller // 2 + 1, since any
    # larger than this would result in a smaller quotient.
    for i in range(2, smaller // 2 + 1):
        if width % i == 0 and height % i == 0:
            # If we find a common divisor, calculate the simplified ratio
            gcd = math.gcd(width, height)
            dividend, divisor = width // gcd, height // gcd
            return f"{dividend}:{divisor}"
    # If no common divisor is found, return the original ratio
    gcd = math.gcd(width, height)
    dividend = width // gcd
    divisor = height // gcd
    return f"{dividend}:{divisor}"


print(f"The aspect ratio is {aspect_ratio(width, height)}")