#EXERCÍCIOS PYTHON - CURSO EM VÍDEO
import os

def limparTela():
    # 'nt' refere-se ao Windows, 'posix' ao Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Exercício Python 001
# Crie um programa que escreva "Olá, Mundo!" na tela.
espere = input("Iniciando ex001...")

msg = "Olá, Mundo!"

print(msg)

espere = input("Pressione Enter para continuar...")

limparTela()

# Exercício Python 002
# Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
espere = input("Iniciando ex002...")

nome = input("Digite seu nome: ")

# print("Olá {}! Prazer em te conhecer!".format(nome)) 
# Forma antiga de formatar strings
# A forma nova é colocar um 'f' antes da string e usar chaves para inserir variáveis diretamente na string
print(f"Olá {nome}! Prazer em te conhecer!")

espere = input("Pressione Enter para continuar...")

limparTela()

# Exercício Python 003
# Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.
espere = input("Iniciando ex003...")

espere = input("Pressione Enter para continuar...")