def crear_contador():
    """
    Crea un contador independiente que se puede incrementar.

    Retorna:
    función incrementar que aumenta y devuelve el conteo actual.
    """
    conteo = 0

    def incrementar():
        nonlocal conteo
        conteo += 1
        return conteo

    return incrementar


# Pruebas de independencia de contadores
contador1 = crear_contador()
contador2 = crear_contador()

print(contador1())  # Salida: 1
print(contador1())  # Salida: 2

print(contador2())  # Salida: 1
print(contador2())  # Salida: 2

print(contador1())  # Salida: 3
