import json
from typing import List, Dict, Optional
from rich.console import Console
from rich.table import Table

ARCHIVO_BIBLIOTECA = "biblioteca.json"

def cargar_biblioteca() -> List[Dict[str, any]]:
    """
    Carga el estado de la biblioteca desde el archivo JSON.

    Returns:
        List[Dict[str, any]]: Lista de libros en la biblioteca.
    """
    try:
        with open(ARCHIVO_BIBLIOTECA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_biblioteca(biblioteca: List[Dict[str, any]]) -> None:
    """
    Guarda el estado de la biblioteca en el archivo JSON.

    Args:
        biblioteca (List[Dict[str, any]]): Lista de libros a guardar.

    Returns:
        None
    """
    with open(ARCHIVO_BIBLIOTECA, "w", encoding="utf-8") as archivo:
        json.dump(biblioteca, archivo, indent=4)

def prestar_libro(biblioteca: List[Dict[str, any]], libro_id: str, nombre_aprendiz: str) -> bool:
    """
    Marca un libro como prestado.

    Args:
        biblioteca (List[Dict[str, any]]): Lista de libros.
        libro_id (str): ID del libro a prestar.
        nombre_aprendiz (str): Nombre de la persona que lo toma prestado.

    Returns:
        bool: True si el préstamo fue exitoso, False si el libro no existe o ya está prestado.
    """
    for libro in biblioteca:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"] is None:
                libro["prestado_a"] = nombre_aprendiz
                guardar_biblioteca(biblioteca)
                return True
            return False
    return False

def devolver_libro(biblioteca: List[Dict[str, any]], libro_id: str) -> bool:
    """
    Marca un libro como disponible (prestado_a: null).

    Args:
        biblioteca (List[Dict[str, any]]): Lista de libros.
        libro_id (str): ID del libro a devolver.

    Returns:
        bool: True si la devolución fue exitosa, False si el libro no existe o no está prestado.
    """
    for libro in biblioteca:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"] is not None:
                libro["prestado_a"] = None
                guardar_biblioteca(biblioteca)
                return True
            return False
    return False

def buscar_libro(biblioteca: List[Dict[str, any]], query: str) -> List[Dict[str, any]]:
    """
    Busca libros por título.

    Args:
        biblioteca (List[Dict[str, any]]): Lista de libros.
        query (str): Término de búsqueda.

    Returns:
        List[Dict[str, any]]: Lista de libros que coinciden con la búsqueda.
    """
    return [libro for libro in biblioteca if query.lower() in libro["titulo"].lower()]

def ver_libros_prestados(biblioteca: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """
    Muestra todos los libros que no están disponibles.

    Args:
        biblioteca (List[Dict[str, any]]): Lista de libros.

    Returns:
        List[Dict[str, any]]: Lista de libros prestados.
    """
    return [libro for libro in biblioteca if libro["prestado_a"] is not None]

def mostrar_libros(libros: List[Dict[str, any]], titulo: str) -> None:
    """
    Muestra una lista de libros en tabla usando rich.

    Args:
        libros (List[Dict[str, any]]): Lista de libros a mostrar.
        titulo (str): Título de la tabla.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title=titulo)

    tabla.add_column("ID", justify="right")
    tabla.add_column("Título", justify="left")
    tabla.add_column("Prestado a", justify="left")

    for libro in libros:
        prestado = libro["prestado_a"] if libro["prestado_a"] else "Disponible"
        tabla.add_row(libro["libro_id"], libro["titulo"], prestado)

    console.print(tabla)

def main() -> None:
    """
    Función principal que muestra el menú y gestiona la interacción con el usuario.

    Returns:
        None
    """
    biblioteca = cargar_biblioteca()
    console = Console()

    while True:
        console.print("\n[bold cyan]Mini Sistema de Biblioteca[/]\n")
        console.print("[1] Ver libros prestados")
        console.print("[2] Buscar libro")
        console.print("[3] Prestar libro")
        console.print("[4] Devolver libro")
        console.print("[5] Salir\n")

        opcion = console.input("Selecciona una opción: ").strip()

        if opcion == "1":
            prestados = ver_libros_prestados(biblioteca)
            mostrar_libros(prestados, "Libros Prestados")

        elif opcion == "2":
            query = console.input("Buscar por título: ").strip()
            resultados = buscar_libro(biblioteca, query)
            mostrar_libros(resultados, f"Resultados para '{query}'")

        elif opcion == "3":
            libro_id = console.input("ID del libro: ").strip()
            nombre = console.input("Nombre del aprendiz: ").strip()
            if prestar_libro(biblioteca, libro_id, nombre):
                console.print("[green]Libro prestado correctamente.[/]")
            else:
                console.print("[red]No se pudo prestar el libro (no existe o ya está prestado).[/]")

        elif opcion == "4":
            libro_id = console.input("ID del libro: ").strip()
            if devolver_libro(biblioteca, libro_id):
                console.print("[green]Libro devuelto correctamente.[/]")
            else:
                console.print("[red]No se pudo devolver el libro (no existe o no está prestado).[/]")

        elif opcion == "5":
            console.print("[bold yellow]¡Hasta luego![/]")
            break

        else:
            console.print("[red]Opción no válida. Intente de nuevo.[/]")

if __name__ == "__main__":
    main()
