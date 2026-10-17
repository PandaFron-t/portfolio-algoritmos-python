"""Situação do aluno.

Origem: Lista 1 do notebook acadêmico de 2025, célula 4.
Conceito: Média e decisão.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    n1 = float(input("Primeira Nota do Aluno:"))
    n2 = float(input("Segunda Nota do Aluno:"))

    media = (n1 + n2) /2

    if media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
