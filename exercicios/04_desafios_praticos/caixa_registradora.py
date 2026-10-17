"""Caixa registradora.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 42.
Conceito: Acumulador e desconto.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

from math import isfinite


def main():
    total = 0
    while True:
        preco = float(input("Digite o preço do item (0 para parar): "))
        if preco == 0:
            break
        if not isfinite(preco) or preco < 0:
            raise ValueError("o preço deve ser um número finito maior que zero.")
        total += preco
    if total > 200:
        total *= 0.9
    print(f"Valor a pagar: R$ {total:.2f}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
