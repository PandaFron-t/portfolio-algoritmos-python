"""Fórmula de peso do enunciado.

Origem: Lista 3 do notebook acadêmico de 2025, célula 19.
Conceito: Seleção entre fórmulas.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()
    altura = float(input("Digite a altura (em metros): "))

    if sexo == "M":
        peso_ideal = (72.7 * altura) - 58
    elif sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        peso_ideal = None
        print("Sexo inválido.")

    if peso_ideal is not None:
        print("Peso ideal:", round(peso_ideal, 2), "kg")


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
