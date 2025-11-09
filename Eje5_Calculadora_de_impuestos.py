from rich.console import Console
from rich.table import Table

# Variable global para la tasa de IVA
TASA_IVA: float = 0.19

def calcular_iva(precio_base: float) -> float:
    """
    Calcula el IVA para un precio dado usando la tasa global TASA_IVA.

    Args:
        precio_base (float): Precio base sobre el cual calcular el IVA.

    Returns:
        float: Valor del IVA calculado.
    """
    return precio_base * TASA_IVA

def actualizar_tasa_iva(nueva_tasa: float) -> None:
    """
    Actualiza la tasa global de IVA con un nuevo valor.

    Args:
        nueva_tasa (float): Nueva tasa de IVA que debe estar entre 0 y 1.

    Raises:
        ValueError: Si la nueva tasa no está entre 0 y 1.

    Returns:
        None
    """
    global TASA_IVA
    if not 0 <= nueva_tasa <= 1:
        raise ValueError("La tasa de IVA debe estar entre 0 y 1.")
    TASA_IVA = nueva_tasa

def mostrar_tabla_precios(precios: list[float]) -> None:
    """
    Muestra una tabla con los precios base y sus respectivos valores de IVA.

    Args:
        precios (list[float]): Lista de precios base.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title="Cálculo de IVA")

    tabla.add_column("Precio Base", justify="right")
    tabla.add_column("IVA", justify="right")

    for precio in precios:
        iva = calcular_iva(precio)
        tabla.add_row(f"${precio:.2f}", f"${iva:.2f}")

    console.print(tabla)

if __name__ == "__main__":
    precios = [100.00, 250.50, 89.99]

    console = Console()
    console.print("[bold underline]Antes de actualizar la tasa de IVA:[/]\n")
    mostrar_tabla_precios(precios)

    actualizar_tasa_iva(0.21)
    console.print("\n[bold underline]Después de actualizar la tasa de IVA a 21%:[/]\n")
    mostrar_tabla_precios(precios)
