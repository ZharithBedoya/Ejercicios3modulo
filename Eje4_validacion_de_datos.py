from typing import Callable, List
from rich.table import Table
from rich.console import Console


def aplicar_validador(lista: list, validador: callable) -> list:
    """
    Aplica un validador a cada elemento de una lista y devuelve solo los que pasan.

    Args:
        lista (list): Lista de elementos a validar.
        validador (callable): Función que valida cada elemento.

    Returns:
        list: Lista de elementos que pasan la validación.
    """
    return [item for item in lista if validador(item)]



import re

def es_email_valido(email: str) -> bool:
    """
    Verifica si un email tiene un formato válido.

    Args:
        email (str): Email a validar.

    Returns:
        bool: True si el email es válido, False en caso contrario.
    """
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.fullmatch(patron, email) is not None



def es_mayor_a_10(numero: int) -> bool:
    """
    Verifica si un número es mayor a 10.

    Args:
        numero (int): Número a evaluar.

    Returns:
        bool: True si el número es mayor a 10, False en caso contrario.
    """
    return numero > 10


def mostrar_resultados(titulo: str, datos: list) -> None:
    """
    Muestra una lista de datos en tabla con formato usando Rich.

    Args:
        titulo (str): Título de la tabla.
        datos (list): Lista de datos a mostrar.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title=titulo)
    tabla.add_column("Índice", justify="right")
    tabla.add_column("Valor", justify="left")

    for idx, valor in enumerate(datos, start=1):
        tabla.add_row(str(idx), str(valor))

    console.print(tabla)


if __name__ == "__main__":
    emails = ["ejemplo@mail.com", "invalidoemail", "usuario@dominio."]
    numeros = [5, 12, 8, 20, 10]

    emails_validos = aplicar_validador(emails, es_email_valido)
    numeros_mayores = aplicar_validador(numeros, es_mayor_a_10)

    mostrar_resultados("Emails Válidos", emails_validos)
    mostrar_resultados("Números Mayores a 10", numeros_mayores)
