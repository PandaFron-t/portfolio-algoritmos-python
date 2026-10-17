"""Categoria de natação.

Origem: Lista 3 do notebook acadêmico de 2025, célula 21.
Conceito: Condições encadeadas.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    idade = int(input("Digite a idade do nadador: "))

    if idade <= 8:
        categoria = "Infantil A"
    elif idade < 13:
        categoria = "Infantil B"
    elif idade < 18:
        categoria = "Juvenil A"
    elif idade < 21:
        categoria = "Juvenil B"
    else:
        categoria = "Sênior"

    print("Categoria:", categoria)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
