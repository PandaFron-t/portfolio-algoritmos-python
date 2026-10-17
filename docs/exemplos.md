# Exemplos de execução

Cada bloco de entrada representa o que deve ser digitado, na ordem solicitada pelo script. Use ponto nos números decimais. A saída indicada é um trecho relevante do resultado.

Os enunciados abaixo resumem o material de 2025; a versão completa está no [notebook original](../notebooks/portfolio_original_2025.ipynb). Os scripts revisados e suas limitações estão descritos no [README](../README.md).

## Soma de dois números

Ler dois números e exibir a soma.

[Ver código](../exercicios/01_fundamentos/soma_dois_numeros.py)

Entrada:

```text
2
3
```

Resultado esperado:

```text
A soma é: 5.0
```

## Parcelamento de uma compra

Dividir o valor de uma compra em 12 parcelas sem juros.

[Ver código](../exercicios/01_fundamentos/parcelamento_compra.py)

Entrada:

```text
120
```

Resultado esperado:

```text
O valor de cada prestação é: 10.0
```

## Troca de valores

Ler dois valores, trocar suas posições e exibir o resultado.

[Ver código](../exercicios/01_fundamentos/troca_valores.py)

Entrada:

```text
azul
roxo
```

Resultado esperado:

```text
Novo valor de A: roxo
```

## Média de três notas

Ler o nome de um aluno e três notas e calcular a média aritmética.

[Ver código](../exercicios/01_fundamentos/media_tres_notas.py)

Entrada:

```text
João
6
7
8
```

Resultado esperado:

```text
Média: 7.0
```

## Consumo de combustível

Dividir a distância percorrida pelo combustível gasto; exigir distância não negativa e combustível positivo.

[Ver código](../exercicios/01_fundamentos/consumo_combustivel.py)

Entrada:

```text
100
10
```

Resultado esperado:

```text
Consumo médio (km/l): 10.0
```

## Situação do aluno

Calcular a média de duas notas e informar aprovação quando a média for maior ou igual a 7.

[Ver código](../exercicios/02_condicionais/situacao_aluno.py)

Entrada:

```text
7
7
```

Resultado esperado:

```text
Aprovado!
```

## Fórmula de peso do enunciado

Aplicar a fórmula fornecida no enunciado para altura e sexo M/F. É um exercício de condicionais.

[Ver código](../exercicios/02_condicionais/peso_ideal.py)

Entrada:

```text
M
1.8
```

Resultado esperado:

```text
72.86
```

## Categoria de natação

Classificar a idade nas faixas até 8, até 12, até 17, até 20 e a partir de 21 anos.

[Ver código](../exercicios/02_condicionais/categoria_natacao.py)

Entrada:

```text
13
```

Resultado esperado:

```text
Categoria: Juvenil A
```

## Comparação de datas

Ler duas datas válidas e informar qual é a mais recente, ou se são iguais. A existência das datas ainda não é validada.

[Ver código](../exercicios/02_condicionais/comparar_datas.py)

Entrada:

```text
1
1
2025
1
1
2026
```

Resultado esperado:

```text
A segunda data é mais recente.
```

## Ano bissexto

Verificar a divisibilidade por 400 ou por 4 sem divisibilidade por 100.

[Ver código](../exercicios/02_condicionais/ano_bissexto.py)

Entrada:

```text
2000
```

Resultado esperado:

```text
O ano é bissexto.
```

## Desconto por valor da compra

Aplicar desconto de 15% abaixo de R$ 200, 20% de R$ 200 até abaixo de R$ 500 e 25% a partir de R$ 500.

[Ver código](../exercicios/02_condicionais/desconto_compra.py)

Entrada:

```text
500
```

Resultado esperado:

```text
Total a pagar: 375.0
```

## Correção de gabarito

Comparar três respostas com o gabarito e contar os acertos.

[Ver código](../exercicios/02_condicionais/corrigir_gabarito.py)

Entrada:

```text
a
b
c
a
b
d
```

Resultado esperado:

```text
Total de acertos: 2
```

## Notas de uma turma

Calcular a média de três notas de cada aluno e contar aprovados e reprovados.

[Ver código](../exercicios/03_repeticoes/notas_turma.py)

Entrada:

```text
2
7
7
7
5
5
5
```

Resultado esperado:

```text
Total reprovados: 1
```

## Inspeção de qualidade

Contar peças cuja medida está no intervalo inclusivo de 9,5 a 10,5.

[Ver código](../exercicios/03_repeticoes/inspecao_qualidade.py)

Entrada:

```text
3
9.5
10.5
11
```

Resultado esperado:

```text
Peças dentro do padrão: 2
```

## Análise de chuvas

Ler 30 dias e informar total, média e o primeiro dia com maior chuva. Se todos forem zero, informar o dia 1.

[Ver código](../exercicios/03_repeticoes/analise_chuvas.py)

Entrada: digite **1** para cada um dos **30 dias**.

Resultado esperado:

```text
Dia com mais chuva: 1
```

## Simulação de investimento

Partir de R$ 500 e, por 12 meses, adicionar R$ 100 antes de aplicar 0,5% de rendimento.

[Ver código](../exercicios/03_repeticoes/simulacao_investimento.py)

Este exercício não solicita entrada.

Resultado esperado:

```text
Saldo após 12 meses: 1770.56
```

## Pesquisa de satisfação

Ler idade e satisfação de 1 a 5 até idade zero; calcular médias e contar notas a partir de 4.

[Ver código](../exercicios/03_repeticoes/pesquisa_satisfacao.py)

Entrada:

```text
20
4
30
2
0
```

Resultado esperado:

```text
Nota média: 3.0
```

## Contagem de passos

Ler passos de sete dias, calcular total e média e contar dias com pelo menos 10 mil passos.

[Ver código](../exercicios/03_repeticoes/atividade_fisica.py)

Entrada: digite **10000** para cada um dos **7 dias**.

Resultado esperado:

```text
Dias com meta atingida: 7
```

## Crescimento populacional

Contar anos até a população atingir o alvo; tratar taxa zero, negativa e alvo já atingido.

[Ver código](../exercicios/03_repeticoes/crescimento_populacional.py)

Entrada:

```text
100
10
121
```

Resultado esperado:

```text
Anos necessários: 2
```

## Conta média de energia

Calcular a média de contas: R$ 0,50/kWh até 100 kWh, R$ 0,75 por kWh excedente e R$ 10 fixos por mês.

[Ver código](../exercicios/03_repeticoes/conta_energia.py)

Entrada:

```text
2
100
200
```

Resultado esperado:

```text
Média da conta de energia: 97.50
```

## Total vendido por produto

Somar quantidades vendidas do código escolhido até receber código zero. Exigir códigos e quantidades positivos.

[Ver código](../exercicios/04_desafios_praticos/total_vendido_produto.py)

Entrada:

```text
10
10
2
20
4
10
3
0
```

Resultado esperado:

```text
Total vendido do produto 10 : 5
```

## Simulador de caixa eletrônico

Simular depósitos e saques até a operação F; validar operações, valores e saldo disponível.

[Ver código](../exercicios/04_desafios_praticos/caixa_eletronico.py)

Entrada:

```text
100
D
50
S
20
F
```

Resultado esperado:

```text
Saldo final: R$ 130.00
```

## Caixa registradora

Somar preços positivos até receber zero e aplicar 10% de desconto somente quando o total superar R$ 200.

[Ver código](../exercicios/04_desafios_praticos/caixa_registradora.py)

Entrada:

```text
100
150
0
```

Resultado esperado:

```text
Valor a pagar: R$ 225.00
```
