"""Pesquisa de satisfação.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 40.
Conceito: Sentinela e médias.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    total_idade = 0
    total_nota = 0
    count = 0
    promotores = 0

    while True:
        idade = int(input("Digite a idade (0 para parar): "))
        if idade == 0:
            break
        nota = int(input("Nota de satisfação (1 a 5): "))
        total_idade += idade
        total_nota += nota
        count += 1
        if nota >= 4:
            promotores += 1

    if count > 0:
        print("Idade média:", total_idade / count)
        print("Nota média:", total_nota / count)
        print("Promotores:", promotores)
    else:
        print("Nenhum dado registrado.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
