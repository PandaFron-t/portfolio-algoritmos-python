"""Inspeção de qualidade.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 37.
Conceito: Repetição e intervalo.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    n = int(input("Digite o número de peças: "))
    boas = 0

    for i in range(n):
        medida = float(input(f"Medida da peça {i+1}: "))
        if 9.5 <= medida <= 10.5:
            boas += 1

    print("Peças dentro do padrão:", boas)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
