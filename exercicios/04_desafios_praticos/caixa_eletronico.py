"""Simulador de caixa eletrônico.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 36.
Conceito: Menu, saldo e validação.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

from math import isfinite


def ler_valor(mensagem, permitir_zero=False):
    """Lê um valor finito e verifica o limite permitido."""
    try:
        valor = float(input(mensagem))
    except ValueError:
        raise ValueError("informe um número válido.") from None
    if not isfinite(valor):
        raise ValueError("o valor deve ser finito.")
    if valor < 0 or (valor == 0 and not permitir_zero):
        limite = "maior ou igual a zero" if permitir_zero else "maior que zero"
        raise ValueError(f"o valor deve ser {limite}.")
    return valor


def main():
    saldo = ler_valor("Informe o saldo inicial: ", permitir_zero=True)
    while True:
        operacao = input("Digite a operação (D = depósito / S = saque / F = fim): ").strip().upper()
        if operacao == "F":
            break
        if operacao not in ("D", "S"):
            print("Operação inválida. Escolha D, S ou F.")
            continue
        try:
            valor = ler_valor("Digite o valor: ")
        except ValueError as erro:
            print(f"Entrada inválida: {erro}")
            continue
        if operacao == "D":
            saldo += valor
        elif valor <= saldo:
            saldo -= valor
        else:
            print("Saldo insuficiente")
    print(f"Saldo final: R$ {saldo:.2f}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
