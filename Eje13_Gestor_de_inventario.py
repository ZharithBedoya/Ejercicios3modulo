import json
from typing import List, Dict
from rich.console import Console
from rich.table import Table

ARCHIVO_INVENTARIO = "inventario.json"

def cargar_inventario() -> List[Dict[str, any]]:
    """
    Carga el inventario desde el archivo JSON.

    Returns:
        List[Dict[str, any]]: Lista de productos en el inventario.
    """
    try:
        with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_inventario(inventario: List[Dict[str, any]]) -> None:
    """
    Guarda el inventario en el archivo JSON.

    Args:
        inventario (List[Dict[str, any]]): Lista de productos a guardar.

    Returns:
        None
    """
    with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4)

def agregar_producto(inventario: List[Dict[str, any]], nombre: str, cantidad: int, precio: float) -> None:
    """
    Agrega un producto al inventario.

    Args:
        inventario (List[Dict[str, any]]): Lista de productos.
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad disponible.
        precio (float): Precio del producto.

    Returns:
        None
    """
    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    guardar_inventario(inventario)

def vender_producto(inventario: List[Dict[str, any]], nombre: str, cantidad: int) -> bool:
    """
    Vende una cantidad de un producto del inventario.

    Args:
        inventario (List[Dict[str, any]]): Lista de productos.
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad a vender.

    Returns:
        bool: True si la venta fue exitosa, False si no hay suficiente stock.
    """
    for producto in inventario:
        if producto["nombre"] == nombre:
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                guardar_inventario(inventario)
                return True
            return False
    return False

def mostrar_inventario(inventario: List[Dict[str, any]]) -> None:
    """
    Muestra el inventario en una tabla usando rich.

    Args:
        inventario (List[Dict[str, any]]): Lista de productos.

    Returns:
        None
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

    Returns:
        None
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
            console.print("[green]Producto agregado correctamente.[/]")

        elif opcion == "3":
            nombre = console.input("Nombre del producto: ").strip()
            cantidad = int(console.input("Cantidad a vender: "))
            if vender_producto(inventario, nombre, cantidad):
                console.print("[green]Venta realizada correctamente.[/]")
            else:
                console.print("[red]No hay suficiente stock o producto no encontrado.[/]")

        elif opcion == "4":
            console.print("[bold yellow]¡Hasta luego![/]")
            break

        else:
            console.print("[red]Opción no válida. Intente de nuevo.[/]")

if __name__ == "__main__":
    main()
