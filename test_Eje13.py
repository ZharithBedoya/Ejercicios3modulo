import json
import tempfile
import os
import pytest
from Eje13_Gestor_de_inventario import (
    cargar_inventario,
    guardar_inventario,
    agregar_producto,
    vender_producto,
)

@pytest.fixture
def inventario_temporal():
    with tempfile.NamedTemporaryFile(delete=False, mode="w+", suffix=".json") as tmp:
        yield tmp.name
    os.remove(tmp.name)

def test_cargar_inventario_vacio(inventario_temporal):
    with open(inventario_temporal, "w", encoding="utf-8") as f:
        f.write("[]")
    assert cargar_inventario(inventario_temporal) == []

def test_guardar_inventario(inventario_temporal):
    inventario = [{"nombre": "Producto A", "cantidad": 10, "precio": 20.0}]
    guardar_inventario(inventario, inventario_temporal)
    with open(inventario_temporal, "r", encoding="utf-8") as f:
        assert json.load(f) == inventario

def test_agregar_producto(inventario_temporal):
    inventario = []
    agregar_producto(inventario, "Producto B", 5, 15.0, inventario_temporal)
    datos = cargar_inventario(inventario_temporal)
    assert datos == [{"nombre": "Producto B", "cantidad": 5, "precio": 15.0}]

def test_vender_producto(inventario_temporal):
    inventario = [{"nombre": "Producto C", "cantidad": 10, "precio": 25.0}]
    guardar_inventario(inventario, inventario_temporal)
    assert vender_producto(inventario, "Producto C", 3, inventario_temporal)
    assert inventario[0]["cantidad"] == 7
