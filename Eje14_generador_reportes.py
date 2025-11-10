import csv
import json
from typing import List, Dict
from rich.console import Console
from rich.table import Table

def leer_csv(nombre_archivo: str) -> List[Dict[str, str]]:
    """
    Lee un archivo CSV y devuelve una lista de diccionarios.

    Args:
        nombre_archivo (str): Nombre del archivo CSV.

    Returns:
        List[Dict[str, str]]: Lista de diccionarios con los datos del CSV.
    """
    with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

def leer_json(nombre_archivo: str) -> Dict[str, List[str]]:
    """
    Lee un archivo JSON y devuelve un diccionario.

    Args:
        nombre_archivo (str): Nombre del archivo JSON.

    Returns:
        Dict[str, List[str]]: Diccionario con los datos del JSON.
    """
    with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
        return json.load(archivo)

def generar_reporte(estudiantes: List[Dict[str, str]], cursos: Dict[str, List[str]]) -> str:
    """
    Combina los datos de estudiantes y cursos para generar un reporte.

    Args:
        estudiantes (List[Dict[str, str]]): Lista de estudiantes.
        cursos (Dict[str, List[str]]): Diccionario de cursos por estudiante.

    Returns:
        str: Reporte en formato de texto.
    """
    reporte = ""
    for estudiante in estudiantes:
        nombre = estudiante["nombre"]
        cursos_estudiante = cursos.get(nombre, [])
        reporte += f"{nombre}: {', '.join(cursos_estudiante)}\n"
    return reporte

def mostrar_reporte_en_consola(reporte: str) -> None:
    """
    Muestra el reporte en la consola usando rich.

    Args:
        reporte (str): Reporte a mostrar.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title="Reporte de Cursos por Estudiante")
    tabla.add_column("Estudiante y Cursos", justify="left")
    for linea in reporte.strip().split("\n"):
        tabla.add_row(linea)
    console.print(tabla)

def main() -> None:
    """
    Función principal que coordina la lectura, combinación y generación del reporte.

    Returns:
        None
    """
    estudiantes = leer_csv("estudiantes.csv")
    cursos = leer_json("cursos.json")
    reporte = generar_reporte(estudiantes, cursos)
    mostrar_reporte_en_consola(reporte)

    with open("reporte.txt", "w", encoding="utf-8") as archivo:
        archivo.write(reporte)

if __name__ == "__main__":
    main()
