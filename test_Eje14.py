import json
import tempfile
import os
import pytest
from Eje14_generador_reportes import leer_csv, leer_json, generar_reporte

@pytest.fixture
def archivos_temporales():
    # Crear archivos temporales para pruebas
    with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".csv") as csv_file:
        csv_file.write("nombre\nAna\nJuan\n")
        csv_path = csv_file.name

    with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".json") as json_file:
        json.dump({"Ana": ["Matemáticas", "Física"], "Juan": ["Historia"]}, json_file)
        json_path = json_file.name

    yield csv_path, json_path

    os.remove(csv_path)
    os.remove(json_path)

def test_leer_csv(archivos_temporales):
    csv_path, _ = archivos_temporales
    resultado = leer_csv(csv_path)
    assert resultado == [{"nombre": "Ana"}, {"nombre": "Juan"}]

def test_leer_json(archivos_temporales):
    _, json_path = archivos_temporales
    resultado = leer_json(json_path)
    assert resultado == {"Ana": ["Matemáticas", "Física"], "Juan": ["Historia"]}

def test_generar_reporte():
    estudiantes = [{"nombre": "Ana"}, {"nombre": "Juan"}]
    cursos = {"Ana": ["Matemáticas", "Física"], "Juan": ["Historia"]}
    reporte = generar_reporte(estudiantes, cursos)
    esperado = "Ana: Matemáticas, Física\nJuan: Historia\n"
    assert reporte == esperado
