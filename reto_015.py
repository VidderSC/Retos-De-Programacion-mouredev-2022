"""
Reto #15 - ¿CUÁNTOS DÍAS?
Crea una función que calcule y retorne cuántos días hay entre dos cadenas de 
texto que representen fechas.
 - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 - La función recibirá dos String y retornará un Int.
 - La diferencia en días será absoluta (no importa el orden de las fechas).
 - Si una de las dos cadenas de texto no representa una fecha correcta se 
   lanzará una excepción.
"""
from datetime import datetime


def calculo_dias_diferencia_entre_fechas(fecha1, fecha2):
    """
    Calcula la diferencia en días entre dos fechas.

    Parámetros:
    fecha1 (str): La primera fecha en formato "dd/MM/aaaa".
    fecha2 (str): La segunda fecha en formato "dd/MM/aaaa".

    Retorna:
    int: La diferencia absoluta en días entre las dos fechas.

    Ejemplo:
    >>> calculo_dias_diferencia_entre_fechas("01/01/2023", "05/01/2023")
    4
    """
    formato_fecha = "%d/%m/%Y"

    try:
        # Convertir las fechas ingresadas en objetos de tipo datetime
        fecha1 = datetime.strptime(fecha1, formato_fecha)
        fecha2 = datetime.strptime(fecha2, formato_fecha)
    except ValueError as e:
        # Capturar el error en caso de que el formato de fecha no sea correcto
        print(f"Error: {e}.")
        print("Debes introducir una fecha correcta en el formato (dd/MM/aaaa).")
        print()
        return None

    # Calcular la diferencia en días
    diferencia = abs((fecha1 - fecha2).days)
    return diferencia


# Inicializamos las fechas
fecha1 = "11/05/2023"
fecha2 = "18/05/2023"

# Calculamos la diferencia en días llamando a la función
dif = calculo_dias_diferencia_entre_fechas(fecha1, fecha2)

if dif is not None:
    print(f"La diferencia en días es de: {dif}")
