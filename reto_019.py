"""
Reto #19 - CONVERSOR TIEMPO
Crea una función que reciba días, horas, minutos y segundos (como enteros) y 
retorne su resultado en milisegundos.
"""
from time import ctime


def main():
    print(f"{tiempo_milisegundos(days=1, hours=1, minutes=1,seconds=1)}ms")


def tiempo_milisegundos(days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> int:
    return (days*24*60*60*1000)+(hours*60*60*1000)+(minutes*60*1000)+(seconds*1000)


if __name__ == "__main__":
    main()
