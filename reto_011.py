"""
Reto #11 - ELIMINANDO CARACTERES
Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima 
otras dos cadenas como salida (out1, out2).
 - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
"""

str1 = input("Escribe algo para 'str1': ")
str2 = input("Escribe algo para 'str2': ")

out1 = ""
out2 = ""

for c in str1:
    if c not in str2:
        out1 += c

for c in str2:
    if c not in str1:
        out2 += c

# Lo mismo pero con List Comprehensions (se devuelve una lista y no un String)
out1b = [c for c in str1 if c not in str2]
out2b = [c for c in str2 if c not in str1]

print()
print("Carácteres presentes en 'str1' pero NO en 'str2':")
print(out1)
print(out1b)

print()
print("Carácteres presentes en 'str2' pero NO en 'str1':")
print(out2)
print(out2b)