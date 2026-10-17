"""Ano bissexto.

Origem: Lista 3 do notebook acadêmico de 2025, célula 25.
Conceito: Operadores lógicos e resto.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    ano = int(input("Digite um ano: "))

    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print("O ano é bissexto.")
    else:
        print("O ano não é bissexto.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
