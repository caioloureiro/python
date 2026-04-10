# EXERCÍCIOS PYTHON - CURSO EM VÍDEO

import os
import requests

def limparTela():
    print("'nt' refere-se ao Windows, 'posix' ao Linux/Mac")
    os.system('cls' if os.name == 'nt' else 'clear')

def mudarTela():
    input("\n\nPressione Enter para continuar...")
    limparTela()
    
def espacos():
	print("")
	print("")
	print("")

def fim():
	input("\n\nPressione Enter para finalizar...")

def buscar_dolar():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url)
        dados = resposta.json()
        return float(dados["USDBRL"]["bid"])
    except requests.exceptions.ConnectionError:
        print("Erro: sem conexão com a internet.")
        return None
    except Exception as e:
        print(f"Erro ao buscar cotação: {e}")
        return None
    
print("Exercício Python 001")
print("Crie um programa que escreva 'Olá, Mundo!' na tela.")
espacos()

msg = "Olá, Mundo!"

print(msg)

mudarTela()

print("Exercício Python 002")
print("Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.")
espacos()

nome = input("Digite seu nome: ")

# print('print("Olá {}! Prazer em te conhecer!".format(nome))')
# Forma antiga de formatar strings
# A forma nova é colocar um 'f' antes da string e usar chaves para inserir variáveis diretamente na string

print(f"Olá {nome}! Prazer em te conhecer!")

mudarTela()

print("Exercício Python 003")
print("Somando dois números")
espacos()

try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    soma = n1 + n2
    print(f"A soma entre {n1} e {n2} é {soma}.")
except ValueError:
    print("Erro: digite apenas números inteiros.")

mudarTela()

print("Exercício Python 004")
print("Dissecando uma variável")
espacos()

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

print("Exercício Python 005")
print("Antecessor e sucessor de um número")
espacos()

try:
    n = int(input("Digite um número: "))
    print(f"Analisando o valor {n}")
    print(f"Seu antecessor é {n-1}")
    print(f"Seu sucessor é {n+1}")
except ValueError:
    print("Erro: digite apenas números inteiros.")

mudarTela()

print("Exercício Python 006")
print("Dobro, triplo e raiz quadrada")
espacos()

try:
    n = int(input("Digite um número: "))
    print(f"O dobro de {n} é {n*2}")
    print(f"O triplo de {n} é {n*3}")
    print(f"A raiz quadrada de {n} é {n**0.5:.2f}")
except ValueError:
    print("Erro: digite apenas números inteiros.")

mudarTela()

print("Exercício Python 007")
print("Média Aritmética")
espacos()

try:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    media = (n1 + n2) / 2
    
    print(f"A média entre {n1} e {n2} é {media:.2f}")
    
    resultado = "Aprovado" if media >= 7 else "Reprovado"
    
    espacos()
    
    print(f"Resultado: {resultado}")
    
except ValueError:
    print("Erro: digite apenas números.")

mudarTela()

print("Exercício Python 008")
print("Conversor de medidas")
espacos()

try:
    metros = float(input("Digite um valor em metros: "))
    print(f"{metros} metros equivalem a {metros*100} centímetros e {metros*1000} milímetros.")
except ValueError:
    print("Erro: digite apenas números.")

mudarTela()

print("Exercício Python 009")
print("Tabuada")
espacos()

try:
    n = int(input("Digite um número para ver sua tabuada: "))
    print(f"Tabuada de {n}:")
    print(f"{n} x 1 = {n*1}")
    print(f"{n} x 2 = {n*2}")
    print(f"{n} x 3 = {n*3}")
    print(f"{n} x 4 = {n*4}")
    print(f"{n} x 5 = {n*5}")
    print(f"{n} x 6 = {n*6}")
    print(f"{n} x 7 = {n*7}")
    print(f"{n} x 8 = {n*8}")
    print(f"{n} x 9 = {n*9}")
    print(f"{n} x 10 = {n*10}")
except ValueError:
    print("Erro: digite apenas números inteiros.")

mudarTela()

print("Exercício Python 010")
print("Conversor de moedas")
espacos()

dolar = buscar_dolar()
if dolar is not None:
    try:
        reais = float(input("Digite um valor em reais: "))
        convertido = reais / dolar
        print(f"Com R${reais:.2f} você pode comprar US${convertido:.2f} (cotação: R${dolar:.2f}).")
    except ValueError:
        print("Erro: digite apenas números.")

fim()