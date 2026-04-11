# Curso de Python

Repositório de exercícios e desafios do curso de Python com interface interativa e síntese de fala.

## Arquivos

### exercicios.py

Menu interativo com 21 exercícios de Python, com síntese de fala (pyttsx3) integrada. O programa exibe uma lista de exercícios e permite ao usuário escolher qual deseja executar.

**Funcionalidades:**

- ✅ **Síntese de fala** — Cada exercício é narrado em áudio
- ✅ **Alt+Enter** — Ativa tela cheia ao abrir
- ✅ **ESC na tela inicial** — Pressione para sair do programa
- ✅ **Código padronizado** — Usa variáveis de texto para evitar repetição

**Exercícios (001-021):**

1. Escreva "Olá, Mundo!" na tela
2. Mensagem de boas-vindas personalizada
3. Soma de dois números
4. Análise de tipo primitivo e propriedades
5. Antecessor e sucessor de um número
6. Dobro, triplo e raiz quadrada
7. Média de notas com aprovação/reprovação
8. Conversão de metros em centímetros e milímetros
9. Tabuada de um número
10. Conversão de reais em dólares (cotação em tempo real)
11. Cálculo de cor e tinta para parede
12. Desconto em produto
13. Aumento de salário
14. Conversão de temperatura °C ↔ °F
15. Cálculo de aluguel de carro
16. Porção inteira de número
17. Cálculo de hipotenusa
18. Seno, cosseno e tangente de ângulo
19. Sorteio de aluno para apagar quadro
20. Sorteio de ordem de apresentação
21. Reprodução de arquivo MP3

### video05.py

Exemplo básico de entrada de dados com `input()` e formatação de saída com f-strings.

### video05-desafio01.py

**Desafio 1 — Mensagem de boas-vindas**
Lê o nome do usuário e exibe uma mensagem de boas-vindas personalizada.

### video05-desafio02.py

**Desafio 2 — Data de nascimento formatada**
Lê nome, dia, mês e ano de nascimento e exibe a data formatada.

### video05-desafio03.py

**Desafio 3 — Soma com tratamento de erro**
Lê dois números e exibe a soma com tratamento de exceções.

## Dependências instaladas

```bash
pip install requests
pip install pyttsx3
pip install pyautogui
pip install pygame
pip install emoji
pip install keyboard
```

## Conceitos abordados

- Entrada de dados com `input()`
- Conversão de tipos: `int()`, `float()`, `str()`
- Formatação de strings com f-strings e variáveis
- Tratamento de exceções com `try/except`
- Requisições HTTP com `requests` (cotação em tempo real)
- Síntese de fala com `pyttsx3`
- Automação com `pyautogui` e `keyboard`
- Funções e modularização
- Threading para monitorar teclas
- Indentação com TABs (tamanho 4)
- Estruturas condicionais e loops

## Configuração

O projeto utiliza:

- **Editor Config** (`.editorconfig`) — TABs tamanho 4
- **Pylance** (`pyrightconfig.json`) — Análise estática

## Como executar

```bash
# Modo completo (tela cheia + som)
python exercicios.py

# Exercíciosespecíficos
python video05.py
python video05-desafio01.py
```

## Controles

| Tecla         | Ação                          |
| ------------- | ----------------------------- |
| **ESC**       | Sair (apenas na tela inicial) |
| **Alt+Enter** | Tela cheia (ao abrir)         |
| **Enter**     | Continuar/Próximo             |
