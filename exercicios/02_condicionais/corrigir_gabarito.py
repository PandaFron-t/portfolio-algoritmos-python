"""Correção de gabarito.

Origem: Lista 3 do notebook acadêmico de 2025, célula 29.
Conceito: Comparação e contador.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    print("Digite suas respostas (a, b, c ou d):")
    res1 = input("Questão 1: ").lower()
    res2 = input("Questão 2: ").lower()
    res3 = input("Questão 3: ").lower()

    print("Digite o gabarito:")
    gab1 = input("Gabarito 1: ").lower()
    gab2 = input("Gabarito 2: ").lower()
    gab3 = input("Gabarito 3: ").lower()

    acertos = 0
    if res1 == gab1:
        acertos += 1
    if res2 == gab2:
        acertos += 1
    if res3 == gab3:
        acertos += 1

    print("Total de acertos:", acertos)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
