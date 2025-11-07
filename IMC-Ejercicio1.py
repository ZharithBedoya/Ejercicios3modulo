from rich import print
from rich.panel import Panel


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso en kg y la altura en metros.

    Args:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.

    Returns:
        float: El valor del IMC calculado.
    """
    return peso / (altura ** 2)


def main() -> None:
    """Función principal del programa."""
    print("[bold cyan]--- Bienvenido al calculador de IMC ---[/bold cyan]\n")

    # Entrada de datos
    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en kg: "))

    # Cálculo
    imc = calcular_imc(peso, altura)

    # Clasificación según el IMC
    if imc < 18.5:
        estado = "[blue]Bajo peso[/blue]"
    elif imc < 25:
        estado = "[green]Peso normal[/green]"
    elif imc < 30:
        estado = "[yellow]Sobrepeso[/yellow]"
    else:
        estado = "[red]Obesidad[/red]"

    # Resultado con panel decorativo
    resultado = (
        f"[bold white]Tu IMC es:[/bold white] {imc:.2f}\n"
        f"[bold white]Estado:[/bold white] {estado}"
    )

    print(Panel(resultado, title="[bold magenta]Resultado[/bold magenta]", expand=False))


if __name__ == "__main__":
    main()
