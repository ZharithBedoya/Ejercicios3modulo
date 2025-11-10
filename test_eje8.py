from Eje8_Transformacion_de_datos import obtener_palabras_mayusculas_largas, contar_longitud_palabras

def test_obtener_palabras_mayusculas_largas():
    texto = "HOLA ESTO ES UNA PRUEBA de PALABRAS MAYÚSCULAS GRANDES y PEQUEÑAS"
    resultado = obtener_palabras_mayusculas_largas(texto)
    esperado = ["PRUEBA", "PALABRAS", "MAYÚSCULAS", "GRANDES", "PEQUEÑAS"]
    # Solo incluyen las que tienen >=6 letras: "PRUEBA", "PALABRAS", "MAYÚSCULAS", "GRANDES"
    esperado = [p for p in esperado if len(p) >= 6]
    assert resultado == esperado

def test_contar_longitud_palabras():
    palabras = ["PRUEBA", "PALABRAS", "MAYÚSCULAS"]
    resultado = contar_longitud_palabras(palabras)
    esperado = { "PRUEBA": 6, "PALABRAS": 8, "MAYÚSCULAS": 10 }
    assert resultado == esperado

def test_texto_vacio():
    assert obtener_palabras_mayusculas_largas("") == []
    assert contar_longitud_palabras([]) == {}
