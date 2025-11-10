import os
import tempfile
import pytest
from Eje11_gestor_de_tareas import agregar_tarea, ver_tareas

@pytest.fixture
def archivo_temporal():
    with tempfile.NamedTemporaryFile(delete=False, mode="w+", encoding="utf-8") as tmp:
        yield tmp.name
    os.remove(tmp.name)

def test_agregar_y_ver_tareas(archivo_temporal, monkeypatch):
    # Parchear la ruta del archivo para usar archivo temporal
    monkeypatch.setattr("Eje11_gestor_de_tareas.ARCHIVO_TAREAS", archivo_temporal)

    agregar_tarea("Tarea 1")
    agregar_tarea("Tarea 2")

    tareas = ver_tareas()
    assert tareas == ["Tarea 1", "Tarea 2"]

def test_ver_tareas_archivo_no_existe(monkeypatch):
    # Archivo temporal que no se crea
    path_no_existente = "archivo_inexistente.txt"
    monkeypatch.setattr("Eje11_gestor_de_tareas.ARCHIVO_TAREAS", path_no_existente)

    tareas = ver_tareas()
    assert tareas == []
