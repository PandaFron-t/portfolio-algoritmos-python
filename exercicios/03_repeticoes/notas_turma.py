"""Notas de uma turma.

Origem: Desafio de programação do notebook acadêmico de 2025, célula 35.
Conceito: Repetição e contadores.
Veja enunciado resumido e exemplo em docs/exemplos.md.
"""

def main():
    n = int(input("Digite o número de alunos: "))
    aprovados = 0
    reprovados = 0

    for i in range(n):
        print(f"Aluno {i+1}:")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        media = (nota1 + nota2 + nota3) / 3
        if media >= 7.0:
            print("Aprovado")
            aprovados += 1
        else:
            print("Reprovado")
            reprovados += 1

    print("Total aprovados:", aprovados)
    print("Total reprovados:", reprovados)


if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        raise SystemExit(1)
