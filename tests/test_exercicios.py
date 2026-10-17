"""Verifica os exemplos e casos de borda dos scripts de terminal."""

from pathlib import Path
import os
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
EXEMPLOS = [('exercicios/01_fundamentos/soma_dois_numeros.py', '2\n3\n', 'A soma é: 5.0'),
 ('exercicios/01_fundamentos/parcelamento_compra.py',
  '120\n',
  'O valor de cada prestação é: 10.0'),
 ('exercicios/01_fundamentos/troca_valores.py', 'azul\nroxo\n', 'Novo valor de A: roxo'),
 ('exercicios/01_fundamentos/media_tres_notas.py', 'João\n6\n7\n8\n', 'Média: 7.0'),
 ('exercicios/01_fundamentos/consumo_combustivel.py',
  '100\n10\n',
  'Consumo médio (km/l): 10.0'),
 ('exercicios/02_condicionais/situacao_aluno.py', '7\n7\n', 'Aprovado!'),
 ('exercicios/02_condicionais/peso_ideal.py', 'M\n1.8\n', '72.86'),
 ('exercicios/02_condicionais/categoria_natacao.py', '13\n', 'Categoria: Juvenil A'),
 ('exercicios/02_condicionais/comparar_datas.py',
  '1\n1\n2025\n1\n1\n2026\n',
  'A segunda data é mais recente.'),
 ('exercicios/02_condicionais/ano_bissexto.py', '2000\n', 'O ano é bissexto.'),
 ('exercicios/02_condicionais/desconto_compra.py', '500\n', 'Total a pagar: 375.0'),
 ('exercicios/02_condicionais/corrigir_gabarito.py',
  'a\nb\nc\na\nb\nd\n',
  'Total de acertos: 2'),
 ('exercicios/03_repeticoes/notas_turma.py', '2\n7\n7\n7\n5\n5\n5\n', 'Total reprovados: 1'),
 ('exercicios/03_repeticoes/inspecao_qualidade.py',
  '3\n9.5\n10.5\n11\n',
  'Peças dentro do padrão: 2'),
 ('exercicios/03_repeticoes/analise_chuvas.py',
  '1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n',
  'Dia com mais chuva: 1'),
 ('exercicios/03_repeticoes/simulacao_investimento.py', '', 'Saldo após 12 meses: 1770.56'),
 ('exercicios/03_repeticoes/pesquisa_satisfacao.py', '20\n4\n30\n2\n0\n', 'Nota média: 3.0'),
 ('exercicios/03_repeticoes/atividade_fisica.py',
  '10000\n10000\n10000\n10000\n10000\n10000\n10000\n',
  'Dias com meta atingida: 7'),
 ('exercicios/03_repeticoes/crescimento_populacional.py',
  '100\n10\n121\n',
  'Anos necessários: 2'),
 ('exercicios/03_repeticoes/conta_energia.py',
  '2\n100\n200\n',
  'Média da conta de energia: 97.50'),
 ('exercicios/04_desafios_praticos/total_vendido_produto.py',
  '10\n10\n2\n20\n4\n10\n3\n0\n',
  'Total vendido do produto 10 : 5'),
 ('exercicios/04_desafios_praticos/caixa_eletronico.py',
  '100\nD\n50\nS\n20\nF\n',
  'Saldo final: R$ 130.00'),
 ('exercicios/04_desafios_praticos/caixa_registradora.py',
  '100\n150\n0\n',
  'Valor a pagar: R$ 225.00')]


class ExerciciosTest(unittest.TestCase):
    def executar(self, caminho, entrada):
        return subprocess.run(
            [sys.executable, str(ROOT / caminho)],
            input=entrada,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            timeout=5,
        )

    def test_exemplos_documentados(self):
        for caminho, entrada, esperado in EXEMPLOS:
            with self.subTest(exercicio=caminho):
                resultado = self.executar(caminho, entrada)
                self.assertEqual(resultado.returncode, 0, resultado.stdout + resultado.stderr)
                self.assertIn(esperado, resultado.stdout)
                self.assertEqual(resultado.stderr, "")

    def test_caixa_eletronico(self):
        caminho = "exercicios/04_desafios_praticos/caixa_eletronico.py"
        casos = [
            ("100\nS\n-10\nF\n", "Saldo final: R$ 100.00"),
            ("100\nD\n-10\nF\n", "Saldo final: R$ 100.00"),
            ("100\nS\n150\nF\n", "Saldo insuficiente"),
            ("100\nX\nF\n", "Operação inválida"),
            ("100\nD\nnan\nF\n", "Saldo final: R$ 100.00"),
            ("100\nS\ninf\nF\n", "Saldo final: R$ 100.00"),
            ("100\nD\ntexto\nF\n", "Saldo final: R$ 100.00"),
            ("100\nD\n0\nF\n", "Saldo final: R$ 100.00"),
            ("0\nd\n10\ns\n10\nf\n", "Saldo final: R$ 0.00"),
        ]
        for entrada, esperado in casos:
            with self.subTest(entrada=entrada):
                resultado = self.executar(caminho, entrada)
                self.assertEqual(resultado.returncode, 0, resultado.stdout + resultado.stderr)
                self.assertIn(esperado, resultado.stdout)
        for entrada in ("-1\n", "nan\n", "texto\n"):
            with self.subTest(saldo_inicial=entrada):
                resultado = self.executar(caminho, entrada)
                self.assertEqual(resultado.returncode, 1)
                self.assertIn("Entrada inválida", resultado.stdout)
                self.assertNotIn("Traceback", resultado.stderr)

    def test_entradas_invalidas(self):
        casos = [
            ("01_fundamentos/consumo_combustivel", "100\n0\n"),
            ("01_fundamentos/consumo_combustivel", "-1\n10\n"),
            ("01_fundamentos/consumo_combustivel", "100\nnan\n"),
            ("03_repeticoes/conta_energia", "0\n"),
            ("03_repeticoes/conta_energia", "-1\n"),
            ("03_repeticoes/conta_energia", "1\n-10\n"),
            ("03_repeticoes/conta_energia", "1\ninf\n"),
            ("03_repeticoes/crescimento_populacional", "100\n-1\n200\n"),
            ("03_repeticoes/crescimento_populacional", "0\n10\n200\n"),
            ("03_repeticoes/crescimento_populacional", "100\nnan\n200\n"),
            ("04_desafios_praticos/total_vendido_produto", "0\n"),
            ("04_desafios_praticos/total_vendido_produto", "10\n10\n-1\n"),
            ("04_desafios_praticos/caixa_registradora", "-10\n"),
            ("04_desafios_praticos/caixa_registradora", "nan\n"),
            ("01_fundamentos/soma_dois_numeros", "texto\n"),
        ]
        for arquivo, entrada in casos:
            with self.subTest(exercicio=arquivo, entrada=entrada):
                resultado = self.executar(f"exercicios/{arquivo}.py", entrada)
                self.assertEqual(resultado.returncode, 1, resultado.stdout + resultado.stderr)
                self.assertIn("Entrada inválida", resultado.stdout)
                self.assertNotIn("Traceback", resultado.stderr)

    def test_crescimento_com_condicao_de_parada(self):
        caminho = "exercicios/03_repeticoes/crescimento_populacional.py"
        casos = [
            ("100\n0\n200\n", "não será alcançada"),
            ("100\n0\n100\n", "Anos necessários: 0"),
            ("100\n10\n50\n", "Anos necessários: 0"),
            ("100\n1e-20\n200\n", "não será alcançada"),
        ]
        for entrada, esperado in casos:
            with self.subTest(entrada=entrada):
                resultado = self.executar(caminho, entrada)
                self.assertEqual(resultado.returncode, 0, resultado.stdout + resultado.stderr)
                self.assertIn(esperado, resultado.stdout)

    def test_sem_chuva(self):
        resultado = self.executar(
            "exercicios/03_repeticoes/analise_chuvas.py", "0\n" * 30
        )
        self.assertEqual(resultado.returncode, 0)
        self.assertIn("Total de chuva: 0.0", resultado.stdout)
        self.assertIn("Dia com mais chuva: 1", resultado.stdout)

    def test_limites_de_desconto(self):
        casos = [
            ("02_condicionais/desconto_compra", "100\n", "Total a pagar: 85.0"),
            ("02_condicionais/desconto_compra", "200\n", "Total a pagar: 160.0"),
            ("02_condicionais/desconto_compra", "500\n", "Total a pagar: 375.0"),
            ("04_desafios_praticos/caixa_registradora", "200\n0\n", "R$ 200.00"),
            ("04_desafios_praticos/caixa_registradora", "201\n0\n", "R$ 180.90"),
        ]
        for arquivo, entrada, esperado in casos:
            with self.subTest(exercicio=arquivo, entrada=entrada):
                resultado = self.executar(f"exercicios/{arquivo}.py", entrada)
                self.assertEqual(resultado.returncode, 0)
                self.assertIn(esperado, resultado.stdout)

    def test_ano_bissexto(self):
        caminho = "exercicios/02_condicionais/ano_bissexto.py"
        for ano, esperado in [
            ("1900", "O ano não é bissexto."),
            ("2000", "O ano é bissexto."),
            ("2024", "O ano é bissexto."),
            ("2025", "O ano não é bissexto."),
        ]:
            with self.subTest(ano=ano):
                resultado = self.executar(caminho, ano + "\n")
                self.assertEqual(resultado.returncode, 0)
                self.assertIn(esperado, resultado.stdout)

    def test_pesquisa_sem_respostas(self):
        resultado = self.executar("exercicios/03_repeticoes/pesquisa_satisfacao.py", "0\n")
        self.assertEqual(resultado.returncode, 0)
        self.assertIn("Nenhum dado registrado.", resultado.stdout)


if __name__ == "__main__":
    unittest.main()
