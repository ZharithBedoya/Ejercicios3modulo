from Eje9_sumatoria_con_redu import suma_total, concatenar_cadenas

def test_suma_total_vacia():
    assert suma_total([]) == 0

def test_suma_total_numeros():
    assert suma_total([1, 2, 3, 4, 5]) == 15
    assert suma_total([0, -1, 1]) == 0

def test_concatenar_cadenas_vacia():
    assert concatenar_cadenas([]) == ""

def test_concatenar_cadenas_texto():
    assert concatenar_cadenas(["Hola", " ", "SENA", "!"]) == "Hola SENA!"
    assert concatenar_cadenas(["a", "b", "c"]) == "abc"
