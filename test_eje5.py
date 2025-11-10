import pytest
from Eje5_Calculadora_de_impuestos import calcular_impuesto, tasa_impuesto

def test_calcular_impuesto_caso_normal():
    """Prueba el cálculo de impuesto con valores normales."""
    resultado = calcular_impuesto(1000)
    esperado = 1000 * tasa_impuesto
    assert resultado == esperado

def test_calcular_impuesto_cero():
    """Prueba el cálculo de impuesto con valor cero."""
    resultado = calcular_impuesto(0)
    assert resultado == 0

def test_calcular_impuesto_negativo():
    """Prueba el cálculo de impuesto con valor negativo."""
    resultado = calcular_impuesto(-100)
    esperado = -100 * tasa_impuesto
    assert resultado == esperado

def test_calcular_impuesto_decimal():
    """Prueba el cálculo de impuesto con valor decimal."""
    resultado = calcular_impuesto(123.45)
    esperado = 123.45 * tasa_impuesto
    assert abs(resultado - esperado) < 1e-6  # Para evitar errores de redondeo

def test_tasa_impuesto_cambio():
    """Prueba que el cálculo cambia si la tasa de impuesto cambia."""
    global tasa_impuesto
    tasa_original = tasa_impuesto
    tasa_impuesto = 0.2
    resultado = calcular_impuesto(100)
    esperado = 100 * 0.2
    assert resultado == esperado
    tasa_impuesto = tasa_original  # Restaurar valor original
