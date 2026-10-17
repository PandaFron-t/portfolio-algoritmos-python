"""Desconto por valor da compra.

Origem: Lista 3 do notebook acadêmico de 2025, célula 27.
Conceito: Faixas de desconto.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    valor = float(input("Digite o valor da compra: "))

    if valor >= 500:
        desconto = valor * 0.25
    elif valor >= 200:
        desconto = valor * 0.20
    else:
        desconto = valor * 0.15

    total = valor - desconto

    print("Valor da compra:", valor)
    print("Desconto:", desconto)
    print("Total a pagar:", total)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
