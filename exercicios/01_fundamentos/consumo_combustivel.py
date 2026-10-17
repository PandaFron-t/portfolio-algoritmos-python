"""Consumo de combustível.

Origem: Lista 2 do notebook acadêmico de 2025, célula 15.
Conceito: Razão e validação de divisor.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

from math import isfinite


def main():
    distancia = float(input("Digite a distância percorrida (em km): "))
    combustivel = float(input("Digite o total de combustível gasto (em litros): "))
    if not isfinite(distancia) or distancia < 0:
        raise ValueError("a distância deve ser um número finito maior ou igual a zero.")
    if not isfinite(combustivel) or combustivel <= 0:
        raise ValueError("o combustível deve ser um número finito maior que zero.")
    consumo = distancia / combustivel
    print("Consumo médio (km/l):", consumo)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
