from Eje6_Modelamiento_de_datos import aplicar_descuento

def test_aplicar_descuento():
    productos = [
        {"nombre": "Item A", "precio": 100.0},
        {"nombre": "Item B", "precio": 200.0},
    ]
    resultado = aplicar_descuento(productos)
    assert resultado == [90.0, 180.0]

def test_aplicar_descuento_precio_cero():
    productos = [
        {"nombre": "Item C", "precio": 0.0},
    ]
    resultado = aplicar_descuento(productos)
    assert resultado == [0.0]
