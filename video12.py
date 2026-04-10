# Video 12 - Operações Aritméticas e funções matemáticas
import os

def limparTela():
    # 'nt' refere-se ao Windows, 'posix' ao Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def mudarTela():
    input("")
    limparTela()

def espacos():
	print("")
	print("")
	print("")

def fim():
	input("")

print("Operações Aritméticas e funções matemáticas")
mudarTela()

print("+ Adição")
print('5+5', end=" = ")
print( 5+5)
mudarTela()

print("- Subtração")
print('10-5', end=" = ")
print(10-5)
mudarTela()

print("* Multiplicação")
print('5*5', end=" = ")
print(5*5)
mudarTela()

print("/ Divisão")
print('10/5', end=" = ")
print(10/5)
mudarTela()

print("** Potenciação")
print('5**2', end=" = ")
print(5**2)
print('pow(5,2)', end=" = ")
print(pow(5,2))
mudarTela()

print("// Divisão inteira")
print('10//3', end=" = ")
print(10//3)
mudarTela()

print("% Resto da divisão")
print('10%3', end=" = ")
print(10%3)
mudarTela()

print("Raiz Quadrada")
print('81**0.5', end=" = ")
print(81**0.5)
print('81**(1/2)', end=" = ")
print(81**(1/2))
mudarTela()

print("Raiz Cúbica")
print('125**(1/3)', end=" = ")
print(125**(1/3))
print(f"{125**(1/3):.2f}")
mudarTela()

print("Repetir caracteres")
print('A'*5)
print('='*10)
mudarTela()

print("" \
	"Ordem de precedência: () ** * / // % + - \n" \
	"1º () Parênteses \n" \
	"2º ** Potenciação \n" \
	"3º * / // % Multiplicação, Divisão, Divisão inteira e Resto da divisão\n" \
	"4º + - Adição e Subtração" \
"")

espacos()

print("5+3*2==11")
print(5+3*2)

print("3*5+4**2==31")
print(3*5+4**2)

print("3*(5+4)**2==243")
print(3*(5+4)**2)

mudarTela()

print('Formatação de strings')

nome = input("Digite seu nome: ")

mudarTela()

print(f"Olá {nome:50}! Prazer em te conhecer!")

mudarTela()

print(f"Olá {nome:>50}! Prazer em te conhecer!")

mudarTela()

print(f"Olá {nome:^50}! Prazer em te conhecer!")

mudarTela()

print(f"Olá {nome:=^50}! Prazer em te conhecer!")

mudarTela()

n1 = 10
n2 = 3
divisao = n1/n2
print(f"A divisão de {n1} por {n2} é {divisao:.2f}", end=" -> ")
print(':.2f limita a 2 casas decimais')

fim()