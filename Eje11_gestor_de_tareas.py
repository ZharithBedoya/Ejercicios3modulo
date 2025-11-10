from typing import List
from rich.console import Console
from rich.table import Table

ARCHIVO_TAREAS = "tareas.txt"

def agregar_tarea(tarea: str) -> None:
    """
    Agrega una tarea al archivo tareas.txt.

    Args:
        tarea (str): Descripción de la tarea a añadir.

    Returns:
        None
    """
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(tarea.strip() + "\n")

def ver_tareas() -> List[str]:
    """
    Lee todas las tareas desde el archivo tareas.txt.

    Returns:
        List[str]: Lista de tareas.
    """
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            tareas = [linea.strip() for linea in archivo.readlines()]
        return tareas
    except FileNotFoundError:
        return []

def mostrar_tareas(tareas: List[str]) -> None:
    """
    Muestra la lista de tareas en tabla usando rich.

    Args:
        tareas (List[str]): Lista de tareas a mostrar.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title="Lista de Tareas")

    tabla.add_column("Índice", justify="right")
    tabla.add_column("Tarea", justify="left")

    if tareas:
        for idx, tarea in enumerate(tareas, start=1):
            tabla.add_row(str(idx), tarea)
    else:
        tabla.add_row("-", "No hay tareas guardadas.")

    console.print(tabla)

def main() -> None:
    """
    Función principal que muestra un menú y gestiona la interacción con el usuario.

    Returns:
        None
    """
    console = Console()

    while True:
        console.print("\n[bold cyan]Gestor de Tareas[/]\n")
        console.print("[1] Ver tareas")
        console.print("[2] Agregar tarea")
        console.print("[3] Salir\n")

        opcion = console.input("Selecciona una opción: ").strip()

        if opcion == "1":
            tareas = ver_tareas()
            mostrar_tareas(tareas)

        elif opcion == "2":
            tarea = console.input("Ingrese la nueva tarea: ").strip()
            if tarea:
                agregar_tarea(tarea)
                console.print("[green]Tarea agregada correctamente.[/]")
            else:
                console.print("[red]La tarea no puede estar vacía.[/]")

        elif opcion == "3":
            console.print("[bold yellow]¡Hasta luego![/]")
            break

        else:
            console.print("[red]Opción no válida. Intente de nuevo.[/]")

if __name__ == "__main__":
    main()
