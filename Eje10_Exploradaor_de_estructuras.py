from typing import Any
from rich.console import Console
from rich.table import Table

def explorar_estructura(elemento: Any, profundidad: int = 1) -> None:
    """
    Explora recursivamente cualquier estructura de datos anidada e imprime
    los valores no iterables junto a su profundidad.

    Args:
        elemento (Any): Elemento o estructura de datos a explorar.
        profundidad (int): Nivel de profundidad actual (por defecto 1).

    Returns:
        None
    """
    console = Console()

    # Caso lista o tupla: recorrer elementos
    if isinstance(elemento, (list, tuple)):
        for item in elemento:
            explorar_estructura(item, profundidad + 1)

    # Caso diccionario: recorrer valores
    elif isinstance(elemento, dict):
        for valor in elemento.values():
            explorar_estructura(valor, profundidad + 1)

    # Caso base: no iterable (string, número, etc.)
    else:
        console.print(f"[bold cyan]Valor:[/] {elemento}, [bold green]Profundidad:[/] {profundidad}")

if __name__ == "__main__":
    estructura = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]
    explorar_estructura(estructura)
