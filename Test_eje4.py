import pytest
from Eje4_validacion_de_datos import aplicar_validador, es_email_valido, es_mayor_a_10


def test_aplicar_validador_emails():
    emails = ["user@test.com", "bademail", "foo@bar."]
    resultado = aplicar_validador(emails, es_email_valido)
    assert resultado == ["user@test.com"]


def test_aplicar_validador_numeros():
    numeros = [9, 10, 11, 15]
    resultado = aplicar_validador(numeros, es_mayor_a_10)
    assert resultado == [11, 15]


def test_es_email_valido_valido():
    assert es_email_valido("persona@dominio.com")
    assert not es_email_valido("persona@dominio")
    assert not es_email_valido("persona.com")
    assert not es_email_valido("")


def test_es_mayor_a_10():
    assert es_mayor_a_10(11)
    assert not es_mayor_a_10(10)
    assert not es_mayor_a_10(5)
