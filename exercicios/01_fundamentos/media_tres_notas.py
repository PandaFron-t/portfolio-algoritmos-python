"""Média de três notas.

Origem: Lista 2 do notebook acadêmico de 2025, célula 13.
Conceito: Média aritmética.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
    print("Aluno:", nome)
    print("Média:", media)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
