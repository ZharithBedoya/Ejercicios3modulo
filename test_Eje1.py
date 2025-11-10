import pytest
from Eje1_IMC import calcular_imc

def test_calcular_imc_normal():
    """Prueba el cálculo de IMC con valores normales."""
    resultado = calcular_imc(70, 1.75)
    assert resultado == pytest.approx(22.86, abs=0.01)

def test_calcular_imc_bajo_peso():
    """Prueba el cálculo de IMC con valores de bajo peso."""
    resultado = calcular_imc(50, 1.75)
    assert resultado == pytest.approx(16.33, abs=0.01)

def test_calcular_imc_sobrepeso():
    """Prueba el cálculo de IMC con valores de sobrepeso."""
    resultado = calcular_imc(80, 1.75)
    assert resultado == pytest.approx(26.12, abs=0.01)

def test_calcular_imc_obesidad():
    """Prueba el cálculo de IMC con valores de obesidad."""
    resultado = calcular_imc(100, 1.75)
    assert resultado == pytest.approx(32.65, abs=0.01)

def test_calcular_imc_altura_cero():
    """Prueba el cálculo de IMC con altura cero (debe lanzar ZeroDivisionError)."""
    with pytest.raises(ZeroDivisionError):
        calcular_imc(70, 0)

def test_calcular_imc_valores_negativos():
    """Prueba el cálculo de IMC con valores negativos."""
    resultado = calcular_imc(-70, 1.75)
    assert resultado == pytest.approx(-22.86, abs=0.01)
