from functools import reduce
from typing import List
from rich.console import Console
from rich.table import Table

def suma_total(numeros: List[int]) -> int:
    """
    Calcula la suma total de una lista de números usando functools.reduce.

    Args:
        numeros (List[int]): Lista de números enteros.

    Returns:
        int: Suma de todos los números de la lista.
    """
    return reduce(lambda acc, x: acc + x, numeros, 0)

def concatenar_cadenas(cadenas: List[str]) -> str:
    """
    Concatena una lista de cadenas en una sola usando functools.reduce.

    Args:
        cadenas (List[str]): Lista de cadenas.

    Returns:
        str: Cadena resultante de la concatenación.
    """
    return reduce(lambda acc, s: acc + s, cadenas, "")

def mostrar_resultados(numeros: List[int], cadenas: List[str]) -> None:
    """
    Muestra resultados de la suma y concatenación en tablas usando rich.

    Args:
        numeros (List[int]): Lista de números.
        cadenas (List[str]): Lista de cadenas.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title="Resultados con reduce")

    tabla.add_column("Operación", justify="left")
    tabla.add_column("Resultado", justify="left")

    suma = suma_total(numeros)
    concatenacion = concatenar_cadenas(cadenas)

    tabla.add_row(f"Suma de {numeros}", str(suma))
    tabla.add_row(f"Concatenación de {cadenas}", concatenacion)

    console.print(tabla)

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    cadenas = ["Hola", " ", "SENA", "!"]

    mostrar_resultados(numeros, cadenas)
