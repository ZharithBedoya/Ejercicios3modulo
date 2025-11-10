from Eje7_filtrado_de_estudiantes import filtrar_estudiantes_aprobados

def test_filtrar_estudiantes_aprobados():
    estudiantes = [
        ("Ana", 4.5),
        ("Juan", 2.8),
        ("Maria", 3.9),
        ("Luis", 2.9),
        ("Sofia", 3.0),
    ]
    resultado = filtrar_estudiantes_aprobados(estudiantes)
    esperado = [
        ("Ana", 4.5),
        ("Maria", 3.9),
        ("Sofia", 3.0),
    ]
    assert resultado == esperado

def test_filtrar_todos_reprobados():
    estudiantes = [
        ("Pedro", 2.0),
        ("Lucia", 1.5),
    ]
    resultado = filtrar_estudiantes_aprobados(estudiantes)
    assert resultado == []

def test_filtrar_todos_aprobados():
    estudiantes = [
        ("Carlos", 3.5),
        ("Elena", 4.0),
    ]
    resultado = filtrar_estudiantes_aprobados(estudiantes)
    assert resultado == estudiantes
