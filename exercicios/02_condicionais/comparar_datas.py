"""Comparação de datas.

Origem: Lista 3 do notebook acadêmico de 2025, célula 23.
Conceito: Comparação de tuplas.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    print("Digite a primeira data:")
    dia1 = int(input("Dia: "))
    mes1 = int(input("Mês: "))
    ano1 = int(input("Ano: "))

    print("Digite a segunda data:")
    dia2 = int(input("Dia: "))
    mes2 = int(input("Mês: "))
    ano2 = int(input("Ano: "))

    if (ano1, mes1, dia1) > (ano2, mes2, dia2):
        print("A primeira data é mais recente.")
    elif (ano1, mes1, dia1) < (ano2, mes2, dia2):
        print("A segunda data é mais recente.")
    else:
        print("As datas são iguais.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
