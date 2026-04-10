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

print("Operações Aritméticas e funções matemáticas")
mudarTela()

print("+ Adição")
print('5+5')
print( 5+5)
mudarTela()

print("- Subtração")
print('10-5')
print(10-5)
mudarTela()

print("* Multiplicação")
print('5*5')
print(5*5)
mudarTela()

print("/ Divisão")
print('10/5')
print(10/5)
mudarTela()

print("** Potenciação")
print('5**2')
print(5**2)
mudarTela()

print("// Divisão inteira")
print('10//3')
print(10//3)
mudarTela()

print("% Resto da divisão")
print('10%3')
print(10%3)
mudarTela()

print("Ordem de precedência: () ** * / // % + -")
print("1º () Parênteses")
print("2º ** Potenciação")
print("3º * / // % Multiplicação, Divisão, Divisão inteira e Resto da divisão")
print("4º + - Adição e Subtração")

espacos()

print("5+3*2==11")
print(5+3*2)

print("3*5+4**2==31")
print(3*5+4**2)

print("3*(5+4)**2==243")
print(3*(5+4)**2)

mudarTela()