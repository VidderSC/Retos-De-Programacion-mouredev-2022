"""
Reto #20 - PARANDO EL TIEMPO
Crea una función que sume 2 números y retorne su resultado pasados
unos segundos.
- Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar
  en finalizar su ejecución.
- Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona,
  es decir, sin detener la ejecución del programa principal. Se podría ejecutar
  varias veces al mismo tiempo.
"""

import asyncio


async def main():
    # Creamos las tareas asincrónicas
    tarea1 = asyncio.create_task(sumar(2, 1, 2))
    tarea2 = asyncio.create_task(sumar(1, 0, 0))

    # Lista de tareas pendientes
    pendientes = [tarea1, tarea2]

    while pendientes:
        # Esperamos hasta que una tarea se complete.
        # La función 'wait' espera a que al menos una tarea de la lista
        # 'pendientes' se complete y devuelve dos conjuntos:
        # 'terminados' que contiene las tareas completadas y
        # 'pendientes' que contiene las tareas que aún no se han completado.
        terminados, pendientes = await \
            asyncio.wait(pendientes,
                         return_when=asyncio.FIRST_COMPLETED)

        # Procesamos las tareas completadas
        for terminado in terminados:
            # Esperamos el resultado de la tarea completada
            resultado = await terminado
            print(resultado)


async def sumar(num1: int, num2: int, delay: int):
    # Esperamos el tiempo especificado en 'delay' antes de continuar
    await asyncio.sleep(delay)
    # Devolvemos la suma de los números
    return num1 + num2


if __name__ == "__main__":
    # Ejecutar la función 'main' de forma asíncrona utilizando 'asyncio.run()'
    asyncio.run(main())
