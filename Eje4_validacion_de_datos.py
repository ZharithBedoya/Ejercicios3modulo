from typing import Callable, List
from rich.table import Table
from rich.console import Console


def aplicar_validador(datos: List, validador: Callable[[object], bool]) -> List:
    """
    Aplica un validador a los elementos de una lista y devuelve
    una nueva lista con los elementos que pasan la validación.

    Args:
        datos (list): Lista de datos a validar.
        validador (Callable[[object], bool]): Función que recibe un elemento
           y devuelve True si pasa la validación, False en caso contrario.

    Returns:
        list: Lista con los elementos que aprobaron la validación.
    """
    return [dato for dato in datos if validador(dato)]


def es_email_valido(email: str) -> bool:
    """
    Valida si un email tiene un formato básico válido.

    Args:
        email (str): Email a validar.

    Returns:
        bool: True si el email tiene '@' y un punto '.' después del '@', False en caso contrario.
    """
    if '@' in email:
        dominio = email.split('@')[1]
        return '.' in dominio and len(dominio.split('.')) > 1
    return False


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
