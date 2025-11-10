import pytest
from Eje5_Calculadora_de_impuestos import calcular_iva, actualizar_tasa_iva, TASA_IVA

def test_calcular_iva():
    global TASA_IVA
    TASA_IVA = 0.19
    assert calcular_iva(100) == 19.0
    assert calcular_iva(0) == 0.0
    assert calcular_iva(50.5) == 50.5 * 0.19

def test_actualizar_tasa_iva_valida():
    actualizar_tasa_iva(0.25)
    assert abs(calcular_iva(100) - 25) < 1e-6

def test_actualizar_tasa_iva_invalida():
    with pytest.raises(ValueError):
        actualizar_tasa_iva(-0.1)
    with pytest.raises(ValueError):
        actualizar_tasa_iva(1.5)
