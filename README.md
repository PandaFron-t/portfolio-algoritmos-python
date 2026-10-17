# Algoritmos e lógica de programação em Python

23 exercícios desenvolvidos em 2025, no 1º semestre de Ciência da Computação na Unisagrado, organizados por tema e complexidade. Em 2026, o material foi separado em scripts executáveis, com documentação e revisão de casos de erro.

## Comece pelos destaques

| Exercício | O que demonstra |
| --- | --- |
| [Caixa eletrônico](exercicios/04_desafios_praticos/caixa_eletronico.py) | Menu de operações, atualização de saldo, bloqueio de saque acima do saldo e validação de valores. |
| [Caixa registradora](exercicios/04_desafios_praticos/caixa_registradora.py) | Soma de compras e desconto de 10% quando o total supera R$ 200. |
| [Total vendido por produto](exercicios/04_desafios_praticos/total_vendido_produto.py) | Filtragem por código e acumulação de quantidades vendidas. |

São exercícios de terminal. O último calcula vendas de um produto; cadastro, saldo de estoque e persistência fazem parte dos próximos projetos.

## Como executar

Requisito: **Python 3**. Os scripts usam somente a biblioteca padrão.

```bash
git clone https://github.com/PandaFron-t/portfolio-algoritmos-python.git
cd portfolio-algoritmos-python
python exercicios/04_desafios_praticos/caixa_eletronico.py
```

Conforme a instalação, use `python3` ou `py` no lugar de `python`. Digite os dados solicitados no terminal; use ponto para separar casas decimais, como `19.90`.

Exemplo no caixa eletrônico: saldo inicial `100`, operação `D`, valor `50`, operação `S`, valor `20` e operação `F`. Resultado: `Saldo final: R$ 130.00`.

Prefere estudar pelo navegador? O [notebook original](notebooks/portfolio_original_2025.ipynb) também está [disponível no Colab](https://colab.research.google.com/github/PandaFron-t/portfolio-algoritmos-python/blob/main/notebooks/portfolio_original_2025.ipynb). Ele foi preservado como registro histórico e contém pseudocódigo em células de código; execute somente as células Python. Para explicações separadas, veja [conceitos e pseudocódigo](docs/pseudocodigo.md).

## Catálogo de exercícios

As pastas seguem uma progressão de estudo. Os desafios práticos combinam conceitos das anteriores.

### 1. Fundamentos

Entrada e saída, variáveis, atribuição e operações.

| Exercício | Conceito principal |
| --- | --- |
| [Soma de dois números](exercicios/01_fundamentos/soma_dois_numeros.py) | Entrada, saída e operadores |
| [Parcelamento de uma compra](exercicios/01_fundamentos/parcelamento_compra.py) | Divisão e valores monetários |
| [Troca de valores](exercicios/01_fundamentos/troca_valores.py) | Variáveis e atribuição |
| [Média de três notas](exercicios/01_fundamentos/media_tres_notas.py) | Média aritmética |
| [Consumo de combustível](exercicios/01_fundamentos/consumo_combustivel.py) | Razão e validação de divisor |

### 2. Condicionais

Decisões, faixas de valores e comparações.

| Exercício | Conceito principal |
| --- | --- |
| [Situação do aluno](exercicios/02_condicionais/situacao_aluno.py) | Média e decisão |
| [Fórmula de peso do enunciado](exercicios/02_condicionais/peso_ideal.py) | Seleção entre fórmulas |
| [Categoria de natação](exercicios/02_condicionais/categoria_natacao.py) | Condições encadeadas |
| [Comparação de datas](exercicios/02_condicionais/comparar_datas.py) | Comparação de tuplas |
| [Ano bissexto](exercicios/02_condicionais/ano_bissexto.py) | Operadores lógicos e resto |
| [Desconto por valor da compra](exercicios/02_condicionais/desconto_compra.py) | Faixas de desconto |
| [Correção de gabarito](exercicios/02_condicionais/corrigir_gabarito.py) | Comparação e contador |

### 3. Repetições

Laços, sentinelas, contadores e acumuladores.

| Exercício | Conceito principal |
| --- | --- |
| [Notas de uma turma](exercicios/03_repeticoes/notas_turma.py) | Repetição e contadores |
| [Inspeção de qualidade](exercicios/03_repeticoes/inspecao_qualidade.py) | Repetição e intervalo |
| [Análise de chuvas](exercicios/03_repeticoes/analise_chuvas.py) | Acumulador e maior valor |
| [Simulação de investimento](exercicios/03_repeticoes/simulacao_investimento.py) | Acumulação e crescimento |
| [Pesquisa de satisfação](exercicios/03_repeticoes/pesquisa_satisfacao.py) | Sentinela e médias |
| [Contagem de passos](exercicios/03_repeticoes/atividade_fisica.py) | Acumulador e metas |
| [Crescimento populacional](exercicios/03_repeticoes/crescimento_populacional.py) | Repetição com condição de parada |
| [Conta média de energia](exercicios/03_repeticoes/conta_energia.py) | Tarifa por faixa e média |

### 4. Desafios práticos

Combinação dos fundamentos em situações de atendimento e vendas.

| Exercício | Conceito principal |
| --- | --- |
| [Total vendido por produto](exercicios/04_desafios_praticos/total_vendido_produto.py) | Filtro, sentinela e acumulador |
| [Simulador de caixa eletrônico](exercicios/04_desafios_praticos/caixa_eletronico.py) | Menu, saldo e validação |
| [Caixa registradora](exercicios/04_desafios_praticos/caixa_registradora.py) | Acumulador e desconto |

[Enunciados resumidos, entradas e resultados esperados dos 23 exercícios](docs/exemplos.md).

## Evolução

| Período | Entrega |
| --- | --- |
| 2025 | Listas acadêmicas e desafios reunidos no notebook original, com Python e pseudocódigo. |
| 2026 | Organização de 23 scripts em quatro categorias, nomes descritivos, ponto de entrada `main()`, catálogo e exemplos de execução. |
| 2026 | Revisão do caixa eletrônico, combustível, vendas, caixa registradora, energia, crescimento populacional e do caso sem chuva; testes de execução e regressão. |

Os exercícios básicos mantêm a abordagem inicial e pressupõem valores dentro do domínio do enunciado. Algumas validações ainda são pontos de evolução: notas e idades fora de faixa, datas inexistentes e alternativas diferentes de a, b, c ou d. A fórmula de peso é apenas a reprodução do exercício acadêmico.

Os simuladores monetários usam `float`, preservando o nível didático original. Representação em centavos ou `Decimal` fica como próxima melhoria.

## Verificação

Execute os exemplos e os casos de regressão:

```bash
python -m unittest discover -s tests -v
```

Os testes executam os 23 scripts e verificam também limites de desconto e ano bissexto, saldo insuficiente, entradas inválidas, divisão por zero e condições de parada.

## Próximos projetos

Todos os itens abaixo estão **planejados**.

| Ordem | Projeto | Primeira entrega | Conceitos a desenvolver |
| --- | --- | --- | --- |
| 1 | Controle de estoque no terminal | Cadastrar produtos, registrar entradas e saídas e salvar os dados em JSON. | Funções, dicionários, arquivos e validação. |
| 2 | Resumo de vendas em CSV | Calcular faturamento, ticket médio e produto mais vendido a partir de vendas fictícias. | Leitura de CSV, agrupamento e relatórios. |
| 3 | Agenda simples no terminal | Criar, listar e concluir tarefas com prazo. | Datas, persistência e organização de funções. |

## Contexto acadêmico

Construída na Unisagrado em 2025
