"""Total vendido por produto.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 34.
Conceito: Filtro, sentinela e acumulador.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    codigo_x = int(input("Informe o código do produto a verificar: "))
    if codigo_x <= 0:
        raise ValueError("o código do produto deve ser maior que zero.")
    total_vendido = 0
    while True:
        codigo = int(input("Digite o código do produto (0 para parar): "))
        if codigo == 0:
            break
        if codigo < 0:
            raise ValueError("o código do produto deve ser maior que zero.")
        quantidade = int(input("Digite a quantidade vendida: "))
        if quantidade <= 0:
            raise ValueError("a quantidade vendida deve ser maior que zero.")
        if codigo == codigo_x:
            total_vendido += quantidade
    print("Total vendido do produto", codigo_x, ":", total_vendido)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
