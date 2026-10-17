"""Simulação de investimento.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 39.
Conceito: Acumulação e crescimento.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    saldo = 500
    for mes in range(12):
        saldo += 100  # aporte
        saldo *= 1.005  # juros de 0.5%

    print("Saldo após 12 meses:", round(saldo, 2))


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
