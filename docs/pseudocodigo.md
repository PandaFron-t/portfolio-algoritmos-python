# Conceitos e pseudocódigo

Material de apoio extraído do notebook de 2025. O pseudocódigo descreve o raciocínio e não deve ser executado pelo interpretador Python.

## Fundamentos

Um algoritmo é uma sequência finita de passos para resolver um problema. A entrada fornece os dados; o processamento transforma esses dados; a saída apresenta o resultado.

Para resolver um exercício: entender o enunciado, definir entradas e saídas, planejar a sequência, implementar e verificar casos normais e de borda.

## Média e situação do aluno

```text
Início
    Ler nota1, nota2
    media ← (nota1 + nota2) / 2
    Se media ≥ 7 então
        Escrever "Aprovado"
    Senão
        Escrever "Reprovado"
    FimSe
Fim
```

## Soma de dois números

```text
Algoritmo SomaDoisNumeros
   Declare num1, num2, soma: Real

   Escreva("Digite o primeiro número: ")
   Leia(num1)
   Escreva("Digite o segundo número: ")
   Leia(num2)

   soma <- num1 + num2
   Escreva("A soma é: ", soma)
Fim
```

## Parcelamento de uma compra

```text
Algoritmo PrestacaoCompra
   Declare valor_compra, prestacao: Real

   Escreva("Digite o valor da compra: ")
   Leia(valor_compra)

   prestacao <- valor_compra / 12
   Escreva("O valor de cada prestação é: ", prestacao)
Fim
```

## Troca de valores

```text
Algoritmo TrocaValores
   Declare a, b, temp: Caracter

   Escreva("Digite o valor de A: ")
   Leia(a)
   Escreva("Digite o valor de B: ")
   Leia(b)

   temp <- a
   a <- b
   b <- temp

   Escreva("Novo valor de A: ", a)
   Escreva("Novo valor de B: ", b)
Fim
```

## Média de três notas

```text
Algoritmo MediaAluno
   Declare nome: Caracter
   Declare nota1, nota2, nota3, media: Real

   Escreva("Digite o nome do aluno: ")
   Leia(nome)

   Escreva("Digite a primeira nota: ")
   Leia(nota1)
   Escreva("Digite a segunda nota: ")
   Leia(nota2)
   Escreva("Digite a terceira nota: ")
   Leia(nota3)

   media <- (nota1 + nota2 + nota3) / 3

   Escreva("Aluno: ", nome)
   Escreva("Média: ", media)
Fim
```

## Consumo de combustível

```text
Algoritmo ConsumoMedio
   Declare distancia, combustivel, consumo: Real

   Escreva("Digite a distância percorrida (km): ")
   Leia(distancia)
   Escreva("Digite o total de combustível gasto (litros): ")
   Leia(combustivel)

   consumo <- distancia / combustivel
   Escreva("Consumo médio (km/l): ", consumo)
Fim
```

## Fórmula de peso do enunciado

```text
Algoritmo PesoIdeal
   Declare sexo: Caracter
   Declare altura, peso_ideal: Real

   Escreva("Digite o sexo (M/F): ")
   Leia(sexo)
   Escreva("Digite a altura: ")
   Leia(altura)

   Se sexo = "M" Então
      peso_ideal <- (72.7 * altura) - 58
   Senão
      Se sexo = "F" Então
         peso_ideal <- (62.1 * altura) - 44.7
      Senão
         Escreva("Sexo inválido.")
         FimAlgoritmo
      FimSe
   FimSe

   Escreva("Peso ideal: ", peso_ideal)
Fim
```

## Categoria de natação

```text
Algoritmo CategoriaNatacao
   Declare idade: Inteiro
   Declare categoria: Caracter

   Escreva("Digite a idade: ")
   Leia(idade)

   Se idade <= 8 Então
      categoria <- "Infantil A"
   Senão Se idade < 13 Então
      categoria <- "Infantil B"
   Senão Se idade < 18 Então
      categoria <- "Juvenil A"
   Senão Se idade < 21 Então
      categoria <- "Juvenil B"
   Senão
      categoria <- "Sênior"
   FimSe

   Escreva("Categoria: ", categoria)
Fim
```

## Comparação de datas

```text
Algoritmo CompararDatas
   Declare dia1, mes1, ano1, dia2, mes2, ano2: Inteiro

   Escreva("Digite a primeira data:")
   Leia(dia1)
   Leia(mes1)
   Leia(ano1)

   Escreva("Digite a segunda data:")
   Leia(dia2)
   Leia(mes2)
   Leia(ano2)

   Se ano1 > ano2 ou (ano1 = ano2 e mes1 > mes2) ou (ano1 = ano2 e mes1 = mes2 e dia1 > dia2) Então
      Escreva("A primeira data é mais recente.")
   Senão Se ano1 < ano2 ou (ano1 = ano2 e mes1 < mes2) ou (ano1 = ano2 e mes1 = mes2 e dia1 < dia2) Então
      Escreva("A segunda data é mais recente.")
   Senão
      Escreva("As datas são iguais.")
   FimSe
Fim
```

## Ano bissexto

```text
Algoritmo AnoBissexto
   Declare ano: Inteiro

   Escreva("Digite um ano: ")
   Leia(ano)

   Se (ano mod 400 = 0) ou (ano mod 4 = 0 e ano mod 100 <> 0) Então
      Escreva("O ano é bissexto.")
   Senão
      Escreva("O ano não é bissexto.")
   FimSe
Fim
```

## Desconto por valor da compra

```text
Algoritmo DescontoCompra
   Declare valor, desconto, total: Real

   Escreva("Digite o valor da compra: ")
   Leia(valor)

   Se valor >= 500 Então
      desconto <- valor * 0.25
   Senão Se valor >= 200 Então
      desconto <- valor * 0.20
   Senão
      desconto <- valor * 0.15
   FimSe

   total <- valor - desconto

   Escreva("Valor da compra: ", valor)
   Escreva("Desconto: ", desconto)
   Escreva("Total a pagar: ", total)
Fim
```

## Correção de gabarito

```text
Algoritmo CorrecaoQuestoes
   Declare res1, res2, res3, gab1, gab2, gab3: Caracter
   Declare acertos: Inteiro

   acertos <- 0

   Escreva("Digite suas respostas:")
   Leia(res1)
   Leia(res2)
   Leia(res3)

   Escreva("Digite o gabarito:")
   Leia(gab1)
   Leia(gab2)
   Leia(gab3)

   Se res1 = gab1 Então
      acertos <- acertos + 1
   FimSe
   Se res2 = gab2 Então
      acertos <- acertos + 1
   FimSe
   Se res3 = gab3 Então
      acertos <- acertos + 1
   FimSe

   Escreva("Total de acertos: ", acertos)
Fim
```

Os pseudocódigos registram as soluções acadêmicas originais. As validações acrescentadas aos scripts em 2026 podem não estar representadas nesses passos.
