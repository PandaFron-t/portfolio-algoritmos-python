"""Conta média de energia.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 44.
Conceito: Tarifa por faixa e média.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

from math import isfinite


def main():
    meses = int(input("Quantos meses: "))
    if meses <= 0:
        raise ValueError("a quantidade de meses deve ser maior que zero.")
    total_conta = 0
    for i in range(meses):
        consumo = float(input(f"Consumo no mês {i+1} (kWh): "))
        if not isfinite(consumo) or consumo < 0:
            raise ValueError("o consumo deve ser um número finito maior ou igual a zero.")
        if consumo <= 100:
            custo = consumo * 0.5
        else:
            custo = 100 * 0.5 + (consumo - 100) * 0.75
        custo += 10
        total_conta += custo
    media = total_conta / meses
    print(f"Média da conta de energia: {media:.2f}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
