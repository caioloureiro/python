# Curso de Python

Repositório de exercícios e desafios do curso de Python.

## Arquivos

### exercicios.py

Menu interativo com 15 exercícios de Python. O programa exibe uma lista de exercícios e permite ao usuário escolher qual deseja executar:

1. **Exercício 001** — Escreva "Olá, Mundo!" na tela
2. **Exercício 002** — Leia o nome e exiba uma mensagem de boas-vindas
3. **Exercício 003** — Leia dois números e calcule a soma
4. **Exercício 004** — Leia um valor e mostre seu tipo primitivo e informações
5. **Exercício 005** — Leia um número e mostre antecessor e sucessor
6. **Exercício 006** — Leia um número e calcule dobro, triplo e raiz quadrada
7. **Exercício 007** — Leia duas notas e calcule a média
8. **Exercício 008** — Converta metros em centímetros e milímetros
9. **Exercício 009** — Exiba a tabuada de um número
10. **Exercício 010** — Converta reais em dólares (com cotação em tempo real)
11. **Exercício 011** — Calcule área de parede e tinta necessária
12. **Exercício 012** — Aplique desconto a um produto
13. **Exercício 013** — Calcule novo salário com aumento
14. **Exercício 014** — Converta temperatura de °C para °F
15. **Exercício 015** — Calcule preço de aluguel de carro

### video05.py

Exemplo básico de entrada de dados com `input()` e formatação de saída com f-strings. Lê nome, idade e peso do usuário e exibe uma mensagem personalizada.

### video05-desafio01.py

**Desafio 1 — Mensagem de boas-vindas**
Lê o nome do usuário e exibe uma mensagem de boas-vindas personalizada.

### video05-desafio02.py

**Desafio 2 — Data de nascimento formatada**
Lê nome, dia, mês e ano de nascimento e exibe a data formatada com zeros à esquerda (`{dia:02d}`).

### video05-desafio03.py

**Desafio 3 — Soma com tratamento de erro**
Lê dois números e exibe a soma. Utiliza `try/except ValueError` para tratar entradas inválidas sem interromper o programa.

## Conceitos abordados

- Entrada de dados com `input()`
- Conversão de tipos: `int()`, `float()`, `str()`
- Formatação de strings com f-strings
- Formatação numérica com especificadores (`:02d`, `:2f`)
- Tratamento de exceções com `try/except`
- Requisições HTTP com `requests` (cotação de moedas)
- Funções e modularização do código
- Indentação com TABs (tamanho 4)
- Estruturas condicionais (`if/elif/else`)

## Configuração

O projeto utiliza:

- **Editor Config** (`.editorconfig`) — Define padrão de indentação com TABs (tamanho 4)
- **Pylance** (`pyrightconfig.json`) — Configuração de análise estática do código

## Como executar

```bash
python exercicios.py
```

Ou para exercícios específicos:

```bash
python video05.py
python video05-desafio01.py
```
