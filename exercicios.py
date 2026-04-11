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
print("Crie um programa que leia dois números e mostre a soma entre eles.")
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
print("Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.")
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
print("Crie um programa que leia um número e mostre o seu antecessor e o seu sucessor.")
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
print("Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.")
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
print("Crie um programa que leia duas notas de um aluno e mostre a sua média.")
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
print("Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.")
espacos()

try:
	metros = float(input("Digite um valor em metros: "))
	print(f"{metros} metros equivalem a {metros*100} centímetros e {metros*1000} milímetros.")
except ValueError:
	print("Erro: digite apenas números.")

mudarTela()

print("Exercício Python 009")
print("Crie um programa que leia um número e mostre a sua tabuada.")
espacos()

try:
	n = int(input("Digite um número para ver sua tabuada: "))
	print(f"Tabuada de {n}:")
	print(f"{n} x {1:2} = {n*1:2}")
	print(f"{n} x {2:2} = {n*2:2}")
	print(f"{n} x {3:2} = {n*3:2}")
	print(f"{n} x {4:2} = {n*4:2}")
	print(f"{n} x {5:2} = {n*5:2}")
	print(f"{n} x {6:2} = {n*6:2}")
	print(f"{n} x {7:2} = {n*7:2}")
	print(f"{n} x {8:2} = {n*8:2}")
	print(f"{n} x {9:2} = {n*9:2}")
	print(f"{n} x {10:2} = {n*10:2}")
except ValueError:
	print("Erro: digite apenas números inteiros.")

mudarTela()

print("Exercício Python 010")
print("Crie um programa que leia um valor em reais e o converta para dólares.")
espacos()

dolar = buscar_dolar()
if dolar is not None: # Se a cotação foi obtida com sucesso, continue com o programa
	try:
		reais = float(input("Digite um valor em reais: "))
		convertido = reais / dolar
		print(f"Com R${reais:.2f} você pode comprar US${convertido:.2f} (cotação: R${dolar:.2f}).")

		mudarTela()

		dolares = float(input("Digite um valor em dólares: "))
		convertido_reais = dolares * dolar
		print(f"Com US${dolares:.2f} você pode comprar R${convertido_reais:.2f} (cotação: R${dolar:.2f}).")
	except ValueError:
		print("Erro: digite apenas números.")

mudarTela()

print("Exercício Python 011")
print("Crie um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta necessária para pintá-la.")
espacos()

try:
	largura = float(input("Digite a largura da parede em metros: "))
	altura = float(input("Digite a altura da parede em metros: "))
	area = largura * altura
	tinta = area / 2
	print(f"Sua parede tem {largura:.2f}x{altura:.2f} metros.")
	print(f"A área da parede é {area:.2f} m².")
	print(f"Você precisará de {tinta:.2f} litros de tinta para pintar a parede.")
except ValueError:
	print("Erro: digite apenas números.")

mudarTela()

print("Exercício Python 012")
print("Crie um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.")
espacos()

try:
	preco = float(input("Digite o preço do produto: R$"))
	desconto = float(input("Digite a porcentagem de desconto: "))
	
	preco_desconto = (preco * desconto / 100)
	valor_final = preco - preco_desconto
	
	print(f"O produto que custava R${preco:.2f} com {desconto:.0f}% de desconto vai custar R${valor_final:.2f}.")
	
except ValueError:
	print("Erro: digite apenas números.")

mudarTela()

print("Exercício Python 013")
print("Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.")
espacos()

try:
	salario = float(input("Digite o salário do funcionário: R$"))
	aumento = float(input("Digite a porcentagem de aumento: "))
	
	salario_aumento = (salario * aumento / 100)
	novo_salario = salario + salario_aumento
	
	print(f"O funcionário que ganhava R${salario:.2f} com {aumento:.0f}% de aumento vai passar a ganhar R${novo_salario:.2f}.")

except ValueError:
	print("Erro: digite apenas números.")

print("Exercício Python 014")
print("Crie um programa que converta uma temperatura digitada em °C e converta para °F.")
espacos()

try:
	celsius = float(input("Digite a temperatura em °C: "))
	fahrenheit = (celsius * 9/5) + 32
	print(f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F.")
	
except ValueError:
	print("Erro: digite apenas números.")

fim()