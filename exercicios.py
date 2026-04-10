#EXERCÍCIOS PYTHON - CURSO EM VÍDEO
import os

def limparTela():
    # 'nt' refere-se ao Windows, 'posix' ao Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def mudarTela():
    input("Pressione Enter para continuar...")
    limparTela()
    
# Exercício Python 001
# Crie um programa que escreva "Olá, Mundo!" na tela.
input("Iniciando ex001...")

msg = "Olá, Mundo!"

print(msg)

mudarTela()

# Exercício Python 002
# Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
input("Iniciando ex002...")

nome = input("Digite seu nome: ")

# print("Olá {}! Prazer em te conhecer!".format(nome)) 
# Forma antiga de formatar strings
# A forma nova é colocar um 'f' antes da string e usar chaves para inserir variáveis diretamente na string
print(f"Olá {nome}! Prazer em te conhecer!")

mudarTela()

# Exercício Python 003
# Somando dois números
input("Iniciando ex003...")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2
print(f"A soma entre {n1} e {n2} é {soma}.")

mudarTela()

# Exercício Python 004
# Dissecando uma variável
input("Iniciando ex004...")

valor = input("Digite algo: ")

print(f"O tipo primitivo desse valor é {type(valor)}")

if valor.isspace():
    print(f"Só tem espaços? {valor.isspace()}")

if valor.isnumeric():
	print(f"É numérico? {valor.isnumeric()}")
	
if valor.isalpha():
	print(f"É letra? {valor.isalpha()}")

if valor.isalnum():
	print(f"É alfanumérico? {valor.isalnum()}")

if valor.isupper():
	print(f"É maiúsculo? {valor.isupper()}")

if valor.islower():
	print(f"É minúsculo? {valor.islower()}")

if valor.istitle():
	print(f"Está capitalizado? {valor.istitle()}")

mudarTela()

# Exercício Python 005
# Antecessor e sucessor
input("Iniciando ex005...")

n = int(input("Digite um número: "))
print(f"Analisando o valor {n}")
print(f"Seu antecessor é {n-1}")
print(f"Seu sucessor é {n+1}")

mudarTela()