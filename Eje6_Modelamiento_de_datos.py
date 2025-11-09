from typing import List, Dict
from rich.console import Console
from rich.table import Table

def aplicar_descuento(productos: List[Dict[str, float]]) -> List[float]:
    """
    Aplica un descuento del 10% a los precios de los productos.

    Args:
        productos (List[Dict[str, float]]): Lista de diccionarios con productos,
            cada uno con las claves "nombre" y "precio".

    Returns:
        List[float]: Lista con los precios con el descuento aplicado.
    """
    return list(map(lambda p: p["precio"] * 0.9, productos))

def mostrar_precios_descuento(precios: List[float]) -> None:
    """
    Muestra una tabla con los precios con descuento usando rich.

    Args:
        precios (List[float]): Lista de precios con descuento.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title="Precios con 10% de Descuento")

    tabla.add_column("Índice", justify="right")
    tabla.add_column("Precio con descuento", justify="right")

    for idx, precio in enumerate(precios, start=1):
        tabla.add_row(str(idx), f"${precio:.2f}")

    console.print(tabla)

if __name__ == "__main__":
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 75000},
        {"nombre": "Zapatos", "precio": 120000},
    ]

    precios_con_descuento = aplicar_descuento(productos)
    mostrar_precios_descuento(precios_con_descuento)
