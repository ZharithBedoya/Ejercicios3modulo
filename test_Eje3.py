import pytest
from Eje3_Contador_de_llamadas import crear_contador

def test_contador_independiente():
    """
    Verifica que dos contadores creados sean independientes.
    """
    contador1 = crear_contador()
    contador2 = crear_contador()

    # Ambos empiezan en 1
    assert contador1() == 1
    assert contador2() == 1

    # Cada uno incrementa su propio conteo
    assert contador1() == 2
    assert contador2() == 2

    # Ambos siguen siendo independientes
    assert contador1() == 3
    assert contador2() == 3

def test_contador_reinicia():
    """
    Verifica que cada contador empieza desde 1.
    """
    contador = crear_contador()
    assert contador() == 1
    assert contador() == 2

def test_contador_multiple():
    """
    Verifica que múltiples contadores pueden existir y funcionar independientemente.
    """
    contadores = [crear_contador() for _ in range(3)]
    for i in range(3):
        for contador in contadores:
            assert contador() == i + 1
