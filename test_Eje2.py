import pytest
from Generador_de_perfiles_de_usuario import crear_perfil

def test_perfil_completo():
    resultado = crear_perfil("Ana", 25, "leer", "viajar", twitter="@ana", instagram="@ana_ig")
    esperado = "Nombre: Ana\nEdad: 25\nHobbies: leer, viajar\nRedes sociales: twitter: @ana, instagram: @ana_ig"
    assert resultado == esperado

def test_perfil_sin_hobbies():
    resultado = crear_perfil("Juan", 30, twitter="@juan")
    esperado = "Nombre: Juan\nEdad: 30\nRedes sociales: twitter: @juan"
    assert resultado == esperado

def test_perfil_sin_redes():
    resultado = crear_perfil("Luis", 22, "fútbol", "música")
    esperado = "Nombre: Luis\nEdad: 22\nHobbies: fútbol, música"
    assert resultado == esperado

def test_perfil_sin_hobbies_ni_redes():
    resultado = crear_perfil("María", 18)
    esperado = "Nombre: María\nEdad: 18"
    assert resultado == esperado
