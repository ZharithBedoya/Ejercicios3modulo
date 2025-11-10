import csv
import os
import tempfile
import pytest
from Eje12_analizador_de_datos import analizar_csv

@pytest.fixture
def archivo_csv_temporal():
    contenido = [
        ["nombre", "edad", "calificacion"],
        ["Ana", "20", "4.5"],
        ["Juan", "22", "3.7"],
        ["Maria", "21", "5.0"],
        ["Luis", "19", "abc"],  # Valor no numérico
    ]

    with tempfile.NamedTemporaryFile(delete=False, mode="w", newline="", encoding="utf-8") as tmp:
        escritor = csv.writer(tmp)
        escritor.writerows(contenido)
        ruta = tmp.name

    yield ruta
    os.remove(ruta)

def test_analizar_csv_promedio_max_min(archivo_csv_temporal):
    resultado = analizar_csv(archivo_csv_temporal, "calificacion")
    assert pytest.approx(resultado["promedio"], 0.01) == (4.5 + 3.7 + 5.0) / 3
    assert resultado["maximo"] == 5.0
    assert resultado["minimo"] == 3.7

def test_analizar_csv_columna_no_existente(archivo_csv_temporal):
    with pytest.raises(ValueError):
        analizar_csv(archivo_csv_temporal, "inexistente")

def test_analizar_csv_columna_no_numerica(archivo_csv_temporal):
    with pytest.raises(ValueError):
        analizar_csv(archivo_csv_temporal, "nombre")
