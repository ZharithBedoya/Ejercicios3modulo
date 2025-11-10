import json
import tempfile
import os
import pytest
import Eje15_mini_sistema_biblioteca as biblioteca_mod

@pytest.fixture
def biblioteca_temporal(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False, mode="w+", suffix=".json") as tmp:
        # Parchea la ruta del archivo para que use este temporal
        monkeypatch.setattr(biblioteca_mod, "ARCHIVO_BIBLIOTECA", tmp.name)
        yield tmp.name
    os.remove(tmp.name)

def test_cargar_biblioteca_vacia(biblioteca_temporal):
    with open(biblioteca_temporal, "w") as f:
        f.write("[]")
    assert biblioteca_mod.cargar_biblioteca() == []

def test_guardar_biblioteca(biblioteca_temporal):
    biblioteca = [{"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": None}]
    biblioteca_mod.guardar_biblioteca(biblioteca)
    with open(biblioteca_temporal, "r") as f:
        contenido = json.load(f)
    assert contenido == biblioteca

def test_prestar_libro(biblioteca_temporal):
    biblioteca = [{"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": None}]
    biblioteca_mod.guardar_biblioteca(biblioteca)
    assert biblioteca_mod.prestar_libro(biblioteca, "001", "Ana")
    assert biblioteca[0]["prestado_a"] == "Ana"

def test_devolver_libro(biblioteca_temporal):
    biblioteca = [{"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": "Ana"}]
    biblioteca_mod.guardar_biblioteca(biblioteca)
    assert biblioteca_mod.devolver_libro(biblioteca, "001")
    assert biblioteca[0]["prestado_a"] is None

def test_buscar_libro():
    biblioteca = [
        {"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": None},
        {"libro_id": "002", "titulo": "El amor en los tiempos del cólera", "prestado_a": None},
    ]
    resultados = biblioteca_mod.buscar_libro(biblioteca, "años")
    assert len(resultados) == 1
    assert resultados[0]["titulo"] == "Cien Años de Soledad"

def test_ver_libros_prestados():
    biblioteca = [
        {"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": "Ana"},
        {"libro_id": "002", "titulo": "El amor en los tiempos del cólera", "prestado_a": None},
    ]
    prestados = biblioteca_mod.ver_libros_prestados(biblioteca)
    assert len(prestados) == 1
    assert prestados[0]["libro_id"] == "001"
