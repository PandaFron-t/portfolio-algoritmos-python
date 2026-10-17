"""Parcelamento de uma compra.

Origem: Lista 2 do notebook acadêmico de 2025, célula 9.
Conceito: Divisão e valores monetários.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    valor_compra = float(input("Digite o valor da compra: "))
    prestacao = valor_compra / 12
    print("O valor de cada prestação é:", prestacao)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
