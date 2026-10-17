"""Troca de valores.

Origem: Lista 2 do notebook acadêmico de 2025, célula 11.
Conceito: Variáveis e atribuição.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    a = input("Digite o valor de A: ")
    b = input("Digite o valor de B: ")

    a, b = b, a

    print("Novo valor de A:", a)
    print("Novo valor de B:", b)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
