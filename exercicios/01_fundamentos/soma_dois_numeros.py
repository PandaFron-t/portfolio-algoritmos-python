"""Soma de dois números.

Origem: Lista 2 do notebook acadêmico de 2025, célula 7.
Conceito: Entrada, saída e operadores.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print("A soma é:", soma)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
