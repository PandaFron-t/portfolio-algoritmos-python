"""Contagem de passos.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 41.
Conceito: Acumulador e metas.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    passos_totais = 0
    meta_dias = 0

    for dia in range(7):
        passos = int(input(f"Passos no dia {dia+1}: "))
        passos_totais += passos
        if passos >= 10000:
            meta_dias += 1

    media_passos = passos_totais / 7
    print("Passos totais:", passos_totais)
    print("Média diária:", media_passos)
    print("Dias com meta atingida:", meta_dias)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
