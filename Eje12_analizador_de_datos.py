"""
Ejercicio 12: Analizador de Datos CSV

Este módulo contiene una función para analizar datos numéricos de un archivo CSV,
calculando el promedio, máximo y mínimo de una columna específica.
Los resultados se muestran en una tabla usando la librería rich.
"""

import csv
from typing import Dict
from rich.table import Table
from rich.console import Console


def analizar_csv(nombre_archivo: str, columna: str) -> Dict[str, float]:
    """
    Analiza una columna numérica de un archivo CSV y devuelve estadísticas básicas.

    Args:
        nombre_archivo (str): Ruta o nombre del archivo CSV.
        columna (str): Nombre de la columna numérica a analizar.

    Returns:
        dict[str, float]: Diccionario con las claves 'promedio', 'maximo' y 'minimo'.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si la columna no es numérica o no existe.
    """
    try:
        with open(nombre_archivo, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            valores = []

            for fila in lector:
                try:
                    valor = float(fila[columna])
                    valores.append(valor)
                except (ValueError, KeyError):
                    continue

            if not valores:
                raise ValueError(f"No se encontraron valores numéricos en la columna '{columna}'.")

            promedio = sum(valores) / len(valores)
            maximo = max(valores)
            minimo = min(valores)

            return {"promedio": promedio, "maximo": maximo, "minimo": minimo}

    except FileNotFoundError as e:
        raise FileNotFoundError(f"El archivo '{nombre_archivo}' no fue encontrado.") from e


def mostrar_tabla(resultados: Dict[str, float]) -> None:
    """
    Muestra los resultados del análisis en una tabla con formato usando rich.

    Args:
        resultados (dict[str, float]): Diccionario con las estadísticas.
    """
    tabla = Table(title="📊 Resultados del Análisis CSV")
    tabla.add_column("Estadística", style="bold cyan")
    tabla.add_column("Valor", justify="right", style="bold yellow")

    for clave, valor in resultados.items():
        tabla.add_row(clave.capitalize(), f"{valor:.2f}")

    console = Console()
    console.print(tabla)


if __name__ == "__main__":
    archivo = "estudiantes.csv"
    columna = "calificación"

    try:
        resultados = analizar_csv(archivo, columna)
        mostrar_tabla(resultados)
    except Exception as error:
        print(f"❌ Error: {error}")
