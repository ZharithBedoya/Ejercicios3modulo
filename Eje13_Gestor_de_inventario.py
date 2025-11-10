import json
from typing import List, Dict, Any
from rich.console import Console
from rich.table import Table

ARCHIVO_INVENTARIO = "inventario.json"

def cargar_inventario(archivo: str = ARCHIVO_INVENTARIO) -> List[Dict[str, Any]]:
    """
    Carga el inventario desde el archivo JSON.
    """
    try:
        with open(archivo, "r", encoding="utf-8") as archivo_json:
            return json.load(archivo_json)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_inventario(inventario: List[Dict[str, Any]], archivo: str = ARCHIVO_INVENTARIO) -> None:
    """
    Guarda el inventario en el archivo JSON.
    """
    with open(archivo, "w", encoding="utf-8") as archivo_json:
        json.dump(inventario, archivo_json, indent=4)

def agregar_producto(inventario: List[Dict[str, Any]], nombre: str, cantidad: int, precio: float, archivo: str = ARCHIVO_INVENTARIO) -> None:
    """
    Agrega un producto al inventario.
    """
    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    guardar_inventario(inventario, archivo)

def vender_producto(inventario: List[Dict[str, Any]], nombre: str, cantidad: int, archivo: str = ARCHIVO_INVENTARIO) -> bool:
    """
    Vende una cantidad de un producto del inventario.
    """
    for producto in inventario:
        if producto["nombre"] == nombre:
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                guardar_inventario(inventario, archivo)
                return True
            return False
    return False

def mostrar_inventario(inventario: List[Dict[str, Any]]) -> None:
    """
    Muestra el inventario en una tabla usando rich.
    """
    console = Console()
    tabla = Table(title="Inventario")

    tabla.add_column("Nombre", justify="left")
    tabla.add_column("Cantidad", justify="right")
    tabla.add_column("Precio", justify="right")

    for producto in inventario:
        tabla.add_row(
            producto["nombre"],
            str(producto["cantidad"]),
            f"${producto['precio']:.2f}"
        )

    console.print(tabla)

def main() -> None:
    """
    Función principal que muestra el menú y gestiona la interacción con el usuario.
    """
    inventario = cargar_inventario()
    console = Console()

    while True:
        console.print("\n[bold cyan]Gestor de Inventario[/]\n")
        console.print("[1] Mostrar inventario")
        console.print("[2] Agregar producto")
        console.print("[3] Vender producto")
        console.print("[4] Salir\n")

        opcion = console.input("Selecciona una opción: ").strip()

        if opcion == "1":
            mostrar_inventario(inventario)

        elif opcion == "2":
            nombre = console.input("Nombre del producto: ").strip()
            cantidad = int(console.input("Cantidad: "))
            precio = float(console.input("Precio: "))
            agregar_producto(inventario, nombre, cantidad, precio)
