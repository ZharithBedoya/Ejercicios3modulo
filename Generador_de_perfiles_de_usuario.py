from typing import Tuple, Dict

def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genera un perfil de usuario con nombre, edad, hobbies y redes sociales.

    Args:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        *hobbies (str): Lista de hobbies del usuario.
        **redes_sociales (str): Diccionario de redes sociales y usuarios.

    Returns:
        str: Perfil formateado como string.
    """
    perfil = f"Nombre: {nombre}\nEdad: {edad}\n"
    if hobbies:
        perfil += f"Hobbies: {', '.join(hobbies)}\n"
    if redes_sociales:
        redes = ', '.join([f"{red}: {usuario}" for red, usuario in redes_sociales.items()])
        perfil += f"Redes sociales: {redes}\n"
    return perfil.strip()
