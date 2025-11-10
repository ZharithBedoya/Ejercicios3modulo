from Eje10_Exploradaor_de_estructuras import explorar_estructura

def test_explorar_estructura_simple(monkeypatch):
    resultado = []

    def fake_print(text):
        # Elimina etiquetas de color Rich antes de guardar
        limpio = str(text).replace("[bold cyan]", "").replace("[/]", "").replace("[bold green]", "")
        resultado.append(limpio)

    import rich.console
    monkeypatch.setattr(rich.console.Console, "print", lambda self, text: fake_print(text))

    estructura = [1, [2, 3], {"a": 4}]
    explorar_estructura(estructura)

    valores = [
        "Valor: 1, Profundidad: 2",
        "Valor: 2, Profundidad: 3",
        "Valor: 3, Profundidad: 3",
        "Valor: 4, Profundidad: 3",
    ]

    assert all(any(v in r for r in resultado) for v in valores)


def test_explorar_estructura_valor_individual(monkeypatch):
    resultado = []

    def fake_print(text):
        limpio = str(text).replace("[bold cyan]", "").replace("[/]", "").replace("[bold green]", "")
        resultado.append(limpio)

    import rich.console
    monkeypatch.setattr(rich.console.Console, "print", lambda self, text: fake_print(text))

    explorar_estructura(42)

    assert any("Valor: 42" in r for r in resultado)
