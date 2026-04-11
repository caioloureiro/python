# EXERCÍCIOS PYTHON - CURSO EM VÍDEO
import os
import requests
import pyttsx3
import pyautogui

# Inicializa o motor de voz
engine = pyttsx3.init()

# Configura a velocidade (opcional)
engine.setProperty('rate', 255)

# No Windows, envia o comando de tela cheia
pyautogui.hotkey('alt', 'enter')

def limparTela():
	print("'nt' refere-se ao Windows, 'posix' ao Linux/Mac")
	os.system('cls' if os.name == 'nt' else 'clear')

def espacos():
	print("")
	print("")
	print("")

def pause():
	engine.say("Pressione Enter para continuar...")
	engine.runAndWait()
	input("Pressione Enter para continuar...")

def fim():
	engine.say("Pressione Enter para finalizar...")
	engine.runAndWait()
	input("\n\nPressione Enter para finalizar...")

#Início do programa
#Tela de seleção de exercícios
print(""
"Bem-vindo aos exercícios de Python!\n" \
"001 - Escreva 'Olá, Mundo!' na tela.\n" \
"002 - Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.\n" \
"003 - Crie um programa que leia dois números e mostre a soma entre eles.\n" \
"004 - Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.\n" \
"005 - Crie um programa que leia um número e mostre o seu antecessor e o seu sucessor.\n" \
"006 - Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.\n" \
"007 - Crie um programa que leia duas notas de um aluno e mostre a sua média.\n" \
"008 - Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.\n" \
"009 - Crie um programa que leia um número e mostre a sua tabuada.\n" \
"010 - Crie um programa que leia um valor em reais e o converta para dólares.\n" \
"011 - Crie um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta necessária para pintá-la.\n" \
"012 - Crie um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.\n" \
"013 - Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.\n" \
"014 - Crie um programa que converta uma temperatura digitada em °C e converta para °F.\n"
"015 - Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.\n" \
"")

engine.say("Digite o número do exercício que deseja executar.")
engine.runAndWait()
exercicio = input("Digite o número do exercício que deseja executar: ")

if not exercicio.isdigit():
	print("Exercício inválido.")
	engine.say("Exercício inválido.")
	fim()
	exit()

if exercicio == "001":
	limparTela()

	print("Exercício Python 001")
	print("Crie um programa que escreva 'Olá, Mundo!' na tela.")
	espacos()

	msg = "Olá, Mundo!"

	print(msg)
	engine.say(msg)

if exercicio == "002":
	limparTela()

	print("Exercício Python 002")
	print("Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.")
	espacos()

	engine.say("Digite o seu nome")

	nome = input("Digite seu nome: ")

	# print('print("Olá {}! Prazer em te conhecer!".format(nome))')
	# Forma antiga de formatar strings
	# A forma nova é colocar um 'f' antes da string e usar chaves para inserir variáveis diretamente na string

	print(f"Olá {nome}! Prazer em te conhecer!")
	engine.say(f"Olá {nome}! Prazer em te conhecer!")

if exercicio == "003":
	limparTela()

	print("Exercício Python 003")
	print("Crie um programa que leia dois números e mostre a soma entre eles.")
	espacos()

	try:

		engine.say("Digite o primeiro número")

		n1 = int(input("Digite o primeiro número: "))

		pause()

		engine.say("Digite o segundo número")

		n2 = int(input("Digite o segundo número: "))

		soma = n1 + n2

		print(f"A soma entre {n1} e {n2} é {soma}.")
		engine.say(f"A soma entre {n1} e {n2} é {soma}.")

	except ValueError:
		print("Erro: digite apenas números inteiros.")
		engine.say("Erro: digite apenas números inteiros.")

if exercicio == "004":
	limparTela()

	print("Exercício Python 004")
	print("Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.")
	espacos()

	engine.say("Digite algo")

	valor = input("Digite algo: ")

	print(f"O tipo primitivo desse valor é {type(valor)}")

	engine.say(valor)

	if valor.isspace():
		print(f"Só tem espaços? {valor.isspace()}")
		engine.say("Só tem espaços")

	if valor.isnumeric():
		print(f"É numérico? {valor.isnumeric()}")
		engine.say("É numérico")

	if valor.isalpha():
		print(f"É letra? {valor.isalpha()}")
		engine.say("É letra")

	if valor.isalnum():
		print(f"É alfanumérico? {valor.isalnum()}")
		engine.say("É alfanumérico")

	if valor.isupper():
		print(f"É maiúsculo? {valor.isupper()}")
		engine.say("É maiúsculo")

	if valor.islower():
		print(f"É minúsculo? {valor.islower()}")
		engine.say("É minúsculo")

	if valor.istitle():
		print(f"Está capitalizado? {valor.istitle()}")
		engine.say("Está capitalizado")

if exercicio == "005":
	limparTela()

	print("Exercício Python 005")
	print("Crie um programa que leia um número e mostre o seu antecessor e o seu sucessor.")
	espacos()

	try:

		engine.say("Digite um número")

		n = int(input("Digite um número: "))

		print(f"Analisando o valor {n}")
		engine.say(f"Analisando o valor {n}")

		print(f"Seu antecessor é {n-1}")
		engine.say(f"Seu antecessor é {n-1}")

		print(f"Seu sucessor é {n+1}")
		engine.say(f"Seu sucessor é {n+1}")

	except ValueError:
		print("Erro: digite apenas números inteiros.")
		engine.say("Erro: digite apenas números inteiros.")

if exercicio == "006":
	limparTela()

	print("Exercício Python 006")
	print("Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.")
	espacos()

	try:

		engine.say("Digite um número")
		n = int(input("Digite um número: "))

		print(f"O dobro de {n} é {n*2}")
		engine.say(f"O dobro de {n} é {n*2}")

		print(f"O triplo de {n} é {n*3}")
		engine.say(f"O triplo de {n} é {n*3}")

		print(f"A raiz quadrada de {n} é {n**0.5:.2f}")
		engine.say(f"A raiz quadrada de {n} é {n**0.5:.2f}")

	except ValueError:
		print("Erro: digite apenas números inteiros.")
		engine.say("Erro: digite apenas números inteiros.")

if exercicio == "007":
	limparTela()

	print("Exercício Python 007")
	print("Crie um programa que leia duas notas de um aluno e mostre a sua média.")
	espacos()

	try:

		engine.say("Digite a primeira nota")

		n1 = float(input("Digite a primeira nota: "))

		pause()

		engine.say("Digite a segunda nota")

		n2 = float(input("Digite a segunda nota: "))

		media = (n1 + n2) / 2
		
		print(f"A média entre {n1} e {n2} é {media:.2f}")
		engine.say(f"A média entre {n1} e {n2} é {media:.2f}")
		
		resultado = "Aprovado" if media >= 7 else "Reprovado"
		
		espacos()
		
		print(f"Resultado: {resultado}")
		engine.say(f"Resultado: {resultado}")
		
	except ValueError:
		print("Erro: digite apenas números.")
		engine.say("Erro: digite apenas números.")

if exercicio == "008":
	limparTela()

	print("Exercício Python 008")
	print("Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.")
	espacos()

	try:
		engine.say("Digite um valor em metros")
		metros = float(input("Digite um valor em metros: "))

		print(f"{metros} metros equivalem a {metros*100} centímetros e {metros*1000} milímetros.")
		engine.say(f"{metros} metros equivalem a {metros*100} centímetros e {metros*1000} milímetros.")

	except ValueError:
		print("Erro: digite apenas números.")
		engine.say("Erro: digite apenas números.")

if exercicio == "009":
	limparTela()

	print("Exercício Python 009")
	print("Crie um programa que leia um número e mostre a sua tabuada.")
	espacos()

	try:
		n = int(input("Digite um número: "))

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
		engine.say("Erro: digite apenas números inteiros.")

if exercicio == "010":
	limparTela()

	print("Exercício Python 010")
	print("Crie um programa que leia um valor em reais e o converta para dólares.")
	espacos()

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

	dolar = buscar_dolar()
	if dolar is not None: # Se a cotação foi obtida com sucesso, continue com o programa
		try:

			engine.say("Digite um valor em reais:")
			reais = float(input("Digite um valor em reais: "))

			convertido = reais / dolar
			print(f"Com R$ {reais:.2f} você pode comprar US$ {convertido:.2f} (cotação: R$ {dolar:.2f}).")
			engine.say(f"Com R$ {reais:.2f} você pode comprar US$ {convertido:.2f} (cotação: R$ {dolar:.2f}).")

			pause()

			limparTela()

			engine.say("Digite um valor em dólares:")

			dolares = float(input("Digite um valor em dólares: "))

			convertido_reais = dolares * dolar
			print(f"Com US${dolares:.2f} você pode comprar R$ {convertido_reais:.2f} (cotação: R$ {dolar:.2f}).")
			engine.say(f"Com US${dolares:.2f} você pode comprar R$ {convertido_reais:.2f} (cotação: R$ {dolar:.2f}).")

		except ValueError:
			print("Erro: digite apenas números.")
			engine.say("Erro: digite apenas números.")

if exercicio == "011":
	limparTela()

	print("Exercício Python 011")
	print("Crie um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta necessária para pintá-la.")
	espacos()

	try:

		engine.say("Digite a largura da parede em metros")

		largura = float(input("Digite a largura da parede em metros: "))

		pause()

		engine.say("Digite a altura da parede em metros")

		altura = float(input("Digite a altura da parede em metros: "))

		area = largura * altura
		tinta = area / 2

		print(f"Sua parede tem {largura:.2f}x{altura:.2f} metros.")
		engine.say(f"Sua parede tem {largura:.2f} por {altura:.2f} metros.")

		print(f"A área da parede é {area:.2f} m².")
		engine.say(f"A área da parede é {area:.2f} metros quadrados.")

		print(f"Você precisará de {tinta:.2f} litros de tinta para pintar a parede.")
		engine.say(f"Você precisará de {tinta:.2f} litros de tinta para pintar a parede.")

	except ValueError:
		print("Erro: digite apenas números.")
		engine.say("Erro: digite apenas números.")

if exercicio == "012":
	limparTela()

	print("Exercício Python 012")
	print("Crie um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.")
	espacos()

	try:

		engine.say("Digite o preço do produto")

		preco = float(input("Digite o preço do produto: R$ "))

		pause()

		engine.say("Digite a porcentagem de desconto")

		desconto = float(input("Digite a porcentagem de desconto: "))
	
		preco_desconto = (preco * desconto / 100)
		valor_final = preco - preco_desconto
		
		print(f"O produto que custava R$ {preco:.2f} com {desconto:.0f}% de desconto vai custar R${valor_final:.2f}.")
		engine.say(f"O produto que custava R$ {preco:.2f} com {desconto:.0f}% de desconto vai custar R$ {valor_final:.2f}.")

	except ValueError:
		print("Erro: digite apenas números.")
		engine.say("Erro: digite apenas números.")

if exercicio == "013":
	limparTela()

	print("Exercício Python 013")
	print("Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.")
	espacos()

	try:

		engine.say("Digite o salário do funcionário")

		salario = float(input("Digite o salário do funcionário: R$"))

		pause()

		engine.say("Digite a porcentagem de aumento")

		aumento = float(input("Digite a porcentagem de aumento: "))
		
		salario_aumento = (salario * aumento / 100)
		novo_salario = salario + salario_aumento
		
		print(f"O funcionário que ganhava R$ {salario:.2f} com {aumento:.0f}% de aumento vai passar a ganhar R$ {novo_salario:.2f}.")
		engine.say(f"O funcionário que ganhava R$ {salario:.2f} com {aumento:.0f}% de aumento vai passar a ganhar R$ {novo_salario:.2f}.")

	except ValueError:
		print("Erro: digite apenas números.")
		engine.say("Erro: digite apenas números.")

if exercicio == "014":
	limparTela()

	print("Exercício Python 014")
	print("Crie um programa que converta uma temperatura digitada em °C e converta para °F.")
	espacos()

	try:

		engine.say("Digite a temperatura em Celsius:")

		celsius = float(input("Digite a temperatura em °C: "))
		fahrenheit = (celsius * 9/5) + 32
		
		print(f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F.")
		engine.say(f"{celsius:.2f} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit.")

		pause()

		limparTela()

		engine.say("Digite a temperatura em Fahrenheit:")

		fahrenheit = float(input("Digite a temperatura em °F: "))
		celsius = (fahrenheit - 32) * 5/9

		print(f"{fahrenheit:.2f}°F equivalem a {celsius:.2f}°C.")
		engine.say(f"{fahrenheit:.2f} graus Fahrenheit equivalem a {celsius:.2f} graus Celsius.")

	except ValueError:
		print("Erro: digite apenas números.")
		engine.say("Erro: digite apenas números.")

if exercicio == "015":
	limparTela()

	print("Exercício Python 015")
	print("Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.")
	espacos()

	try:

		engine.say("Digite a quantidade de quilômetros percorridos")

		km = float(input("Digite a quantidade de quilômetros percorridos: "))

		pause()

		engine.say("Digite a quantidade de dias alugados")

		dias = int(input("Digite a quantidade de dias alugados: "))

		preco_km = km * 0.15
		preco_dias = dias * 60
		preco_total = preco_km + preco_dias

		print(f"O preço a pagar é R$ {preco_total:.2f}.")
		engine.say(f"O preço a pagar é R$ {preco_total:.2f}.")

	except ValueError:
		print("Erro: digite apenas números.")
		engine.say("Erro: digite apenas números.")

fim()
