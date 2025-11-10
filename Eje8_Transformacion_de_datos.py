from typing import List, Dict
from rich.console import Console
from rich.table import Table

def obtener_palabras_mayusculas_largas(texto: str, longitud_minima: int = 6) -> List[str]:
    """
    Extrae una lista de palabras que estén en mayúsculas y tengan más de un número
    mínimo de letras del texto dado.

    Args:
        texto (str): Texto de entrada.
        longitud_minima (int): Longitud mínima de las palabras. Por defecto es 6.

    Returns:
        List[str]: Lista de palabras en mayúsculas que cumplen la longitud mínima.
    """
    palabras = texto.split()
    return [palabra for palabra in palabras if palabra.isupper() and len(palabra) >= longitud_minima]

def contar_longitud_palabras(palabras: List[str]) -> Dict[str, int]:
    """
    Genera un diccionario que asigna a cada palabra su longitud.

    Args:
        palabras (List[str]): Lista de palabras.

    Returns:
        Dict[str, int]: Diccionario con palabra como clave y su longitud como valor.
    """
    return {palabra: len(palabra) for palabra in palabras}

def mostrar_resultados(palabras: List[str], conteo: Dict[str, int]) -> None:
    """
    Muestra en tablas formateadas los resultados usando rich.

    Args:
        palabras (List[str]): Lista de palabras filtradas.
        conteo (Dict[str, int]): Diccionario con la longitud de cada palabra.

    Returns:
        None
    """
    console = Console()

    tabla_palabras = Table(title="Palabras en mayúsculas con más de 5 letras")
    tabla_palabras.add_column("Índice", justify="right")
    tabla_palabras.add_column("Palabra", justify="left")
    for idx, palabra in enumerate(palabras, start=1):
        tabla_palabras.add_row(str(idx), palabra)

    tabla_conteo = Table(title="Longitud de cada palabra")
    tabla_conteo.add_column("Palabra", justify="left")
    tabla_conteo.add_column("Longitud", justify="right")
    for palabra, longitud in conteo.items():
        tabla_conteo.add_row(palabra, str(longitud))

    console.print(tabla_palabras)
    console.print(tabla_conteo)

if __name__ == "__main__":
    texto = (
        "ESTE es un EJEMPLO DE TEXTO DONDE algunas PALABRAS están EN MAYÚSCULAS "
        "y otras no. LAS PALABRAS LARGAS EN MAYÚSCULAS DEBERÍAN SER FILTRADAS."
    )
    palabras_filtradas = obtener_palabras_mayusculas_largas(texto)
    conteo_palabras = contar_longitud_palabras(palabras_filtradas)
    mostrar_resultados(palabras_filtradas, conteo_palabras)
