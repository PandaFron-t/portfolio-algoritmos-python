"""Análise de chuvas.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 38.
Conceito: Acumulador e maior valor.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    total_chuva = 0
    maior = 0
    dia_maior = 1

    for dia in range(1, 31):
        chuva = float(input(f"Chuva no dia {dia}: "))
        total_chuva += chuva
        if chuva > maior:
            maior = chuva
            dia_maior = dia

    media_chuva = total_chuva / 30
    print("Total de chuva:", total_chuva)
    print("Média de chuva:", media_chuva)
    print("Dia com mais chuva:", dia_maior)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
