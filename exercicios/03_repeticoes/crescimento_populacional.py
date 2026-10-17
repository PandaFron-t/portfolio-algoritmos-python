"""Crescimento populacional.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 43.
Conceito: Repetição com condição de parada.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

from math import isfinite


def main():
    populacao = int(input("População inicial: "))
    taxa = float(input("Taxa de crescimento (%): "))
    populacao_alvo = int(input("População alvo: "))
    if populacao <= 0 or populacao_alvo <= 0:
        raise ValueError("as populações devem ser maiores que zero.")
    if not isfinite(taxa) or taxa < 0:
        raise ValueError("a taxa deve ser um número finito maior ou igual a zero.")
    fator = 1 + taxa / 100
    if populacao < populacao_alvo and fator <= 1:
        print("A população alvo não será alcançada com essa taxa.")
        return
    anos = 0
    while populacao < populacao_alvo:
        populacao *= fator
        anos += 1
    print("Anos necessários:", anos)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
