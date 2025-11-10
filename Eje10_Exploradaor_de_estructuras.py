from typing import Any
from rich.console import Console

def explorar_estructura(elemento: Any, profundidad: int = 1, salida=None) -> None:
    """
    Explora recursivamente cualquier estructura de datos anidada e imprime
    los valores no iterables junto a su profundidad.
    """
    console = Console()
    if salida is None:
        salida = []

    if isinstance(elemento, (list, tuple)):
        for item in elemento:
            explorar_estructura(item, profundidad + 1, salida)

    elif isinstance(elemento, dict):
        for valor in elemento.values():
            explorar_estructura(valor, profundidad + 1, salida)

    else:
        texto_plano = f"Valor: {elemento}, Profundidad: {profundidad}"
        salida.append(texto_plano)
        console.print(f"[bold cyan]Valor:[/] {elemento}, [bold green]Profundidad:[/] {profundidad}")

    return salida
