from typing import List, Tuple
from rich.console import Console
from rich.table import Table

def filtrar_estudiantes_aprobados(estudiantes: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    """
    Filtra la lista de estudiantes dejando solo aquellos con nota >= 3.0.

    Args:
        estudiantes (List[Tuple[str, float]]): Lista de tuplas con nombre y nota del estudiante.

    Returns:
        List[Tuple[str, float]]: Lista filtrada con estudiantes aprobados.
    """
    return list(filter(lambda estudiante: estudiante[1] >= 3.0, estudiantes))

def mostrar_estudiantes(estudiantes: List[Tuple[str, float]]) -> None:
    """
    Muestra una tabla con la lista de estudiantes y sus notas usando rich.

    Args:
        estudiantes (List[Tuple[str, float]]): Lista de estudiantes a mostrar.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title="Estudiantes Aprobados")

    tabla.add_column("Nombre", justify="left")
    tabla.add_column("Nota", justify="right")

    for nombre, nota in estudiantes:
        tabla.add_row(nombre, f"{nota:.2f}")

    console.print(tabla)

if __name__ == "__main__":
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9), ("Luis", 2.9)]

    aprobados = filtrar_estudiantes_aprobados(estudiantes)
    mostrar_estudiantes(aprobados)
