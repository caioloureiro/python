# EXERCÍCIOS PYTHON - CURSO EM VÍDEO
import os
import requests
import pyttsx3
import pyautogui
import math

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
	texto = ""
	print(texto)
	print(texto)
	print(texto)

def pause():
	texto = "Pressione Enter para continuar..."
	engine.say(texto)
	engine.runAndWait()
	input(texto)

def pause2():
	texto = "Pressione Enter para continuar..."
	engine.say(texto)
	input(texto)

def fim():
	texto = "Pressione Enter para finalizar..."
	engine.say(texto)
	engine.runAndWait()
	input(texto)
	exit()

def fim2():
	texto = "Pressione Enter para finalizar..."
	engine.say(texto)
	input(texto)
	exit()

def erroNum():
	texto = "Erro: digite apenas números."
	print(texto)
	engine.say(texto)
	fim()

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
"016 - Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.\n" \
"017 - Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.\n"
"018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.\n"
"")

texto = "Digite o número do exercício que deseja executar: "
engine.say(texto)
engine.runAndWait()
exercicio = input(texto)

if not exercicio.isdigit():
	erroNum()
	exit()

if exercicio == "001":
	limparTela()

	print("Exercício Python 001")
	print("Crie um programa que escreva 'Olá, Mundo!' na tela.")
	espacos()

	texto = "Olá, Mundo!"
	print(texto)
	engine.say(texto)
	fim()

if exercicio == "002":
	limparTela()

	print("Exercício Python 002")
	print("Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.")
	espacos()

	texto = "Digite o seu nome: "
	engine.say(texto)
	nome = input(texto)

	texto = f"Olá {nome}! Prazer em te conhecer!"
	print(texto)
	engine.say(texto)
	fim()

if exercicio == "003":
	limparTela()

	print("Exercício Python 003")
	print("Crie um programa que leia dois números e mostre a soma entre eles.")
	espacos()

	try:

		texto = "Digite o primeiro número: "
		engine.say(texto)

		n1 = int(input(texto))

		pause()

		texto = "Digite o segundo número: "
		engine.say(texto)

		n2 = int(input(texto))

		soma = n1 + n2

		texto = f"A soma entre {n1} e {n2} é {soma}."
		print(texto)
		engine.say(texto)
		fim()

	except ValueError:
		erroNum()

if exercicio == "004":
	limparTela()

	print("Exercício Python 004")
	print("Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.")
	espacos()

	texto = "Digite algo: "

	engine.say(texto)
	valor = input(texto)

	texto = f"Você digitou: {valor}"
	print(texto)
	engine.say(texto)
	pause()

	if valor.isspace():
		print(f"Só tem espaços? {valor.isspace()}")
		engine.say("Só tem espaços")
		pause()

	if valor.isnumeric():
		print(f"É numérico? {valor.isnumeric()}")
		engine.say("É numérico")
		pause()

	if valor.isalpha():
		print(f"É letra? {valor.isalpha()}")
		engine.say("É letra")
		pause()

	if valor.isalnum():
		print(f"É alfanumérico? {valor.isalnum()}")
		engine.say("É alfanumérico")
		pause()

	if valor.isupper():
		print(f"É maiúsculo? {valor.isupper()}")
		engine.say("É maiúsculo")
		pause()

	if valor.islower():
		print(f"É minúsculo? {valor.islower()}")
		engine.say("É minúsculo")
		pause()

	if valor.istitle():
		print(f"Está capitalizado? {valor.istitle()}")
		engine.say("Está capitalizado")
		pause()
	
	fim2()

if exercicio == "005":
	limparTela()

	print("Exercício Python 005")
	print("Crie um programa que leia um número e mostre o seu antecessor e o seu sucessor.")
	espacos()

	try:

		texto = "Digite um número: "

		engine.say(texto)

		n = int(input(texto))

		texto1 = f"Analisando o valor {n}"
		print(texto1)
		engine.say(texto1)

		texto2 = f"Seu antecessor é {n-1}"
		print(texto2)
		engine.say(texto2)

		texto3 = f"Seu sucessor é {n+1}"
		print(texto3)
		engine.say(texto3)

		fim()

	except ValueError:
		erroNum()

if exercicio == "006":
	limparTela()

	print("Exercício Python 006")
	print("Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.")
	espacos()

	try:

		engine.say("Digite um número")
		n = int(input("Digite um número: "))

		texto1 = f"O dobro de {n} é {n*2}"
		print(texto1)
		engine.say(texto1)

		texto2 = f"O triplo de {n} é {n*3}"
		print(texto2)
		engine.say(texto2)

		texto3 = f"A raiz quadrada de {n} é {n**0.5:.2f}"
		print(texto3)
		engine.say(texto3)

		fim()

	except ValueError:
		erroNum()

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
		
		texto = f"A média entre {n1} e {n2} é {media:.2f}"
		print(texto)
		engine.say(texto)
		
		resultado = "Aprovado" if media >= 7 else "Reprovado"
		
		espacos()
		
		print(f"Resultado: {resultado}")
		engine.say(f"Resultado: {resultado}")

		fim()
		
	except ValueError:
		erroNum()

if exercicio == "008":
	limparTela()

	print("Exercício Python 008")
	print("Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.")
	espacos()

	try:
		engine.say("Digite um valor em metros")
		metros = float(input("Digite um valor em metros: "))

		texto = f"{metros} metros equivalem a {metros*100} centímetros e {metros*1000} milímetros."
		print(texto)
		engine.say(texto)
		fim()

	except ValueError:
		erroNum()

if exercicio == "009":
	limparTela()

	print("Exercício Python 009")
	print("Crie um programa que leia um número e mostre a sua tabuada.")
	espacos()

	try:
		n = int(input("Digite um número: "))

		texto = f"Tabuada de {n}:"
		print(texto)

		for i in range(1, 101):
			texto_linha = f"{n} x {i:2} = {n*i:2}"
			print(texto_linha)

		engine.say(f"Tabuada exibida na tela.")

		fim()

	except ValueError:
		erroNum()

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

			texto = "Digite um valor em reais: "
			engine.say(texto)
			reais = float(input(texto))

			convertido = reais / dolar
			texto = f"Com R$ {reais:.2f} você pode comprar US$ {convertido:.2f} (cotação: R$ {dolar:.2f})."
			print(texto)
			engine.say(texto)

			pause()

			limparTela()

			texto = "Digite um valor em dólares: "
			engine.say(texto)
			dolares = float(input(texto))

			convertido_reais = dolares * dolar
			texto = f"Com US${dolares:.2f} você pode comprar R$ {convertido_reais:.2f} (cotação: R$ {dolar:.2f})."
			print(texto)
			engine.say(texto)

			fim()

		except ValueError:
			erroNum()

if exercicio == "011":
	limparTela()

	print("Exercício Python 011")
	print("Crie um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta necessária para pintá-la.")
	espacos()

	try:

		texto = "Digite a largura da parede em metros: "
		engine.say(texto)
		largura = float(input(texto))

		pause()

		texto = "Digite a altura da parede em metros: "
		engine.say(texto)
		altura = float(input(texto))

		area = largura * altura
		tinta = area / 2

		texto1 = f"Sua parede tem {largura:.2f}x{altura:.2f} metros."
		print(texto1)
		engine.say(texto1)

		texto2 = f"A área da parede é {area:.2f} m²."
		print(texto2)
		engine.say(texto2)

		texto3 = f"Você precisará de {tinta:.2f} litros de tinta para pintar a parede."
		print(texto3)
		engine.say(texto3)

		fim()

	except ValueError:
		erroNum()

if exercicio == "012":
	limparTela()

	print("Exercício Python 012")
	print("Crie um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.")
	espacos()

	try:

		texto = "Digite o preço do produto: "
		engine.say(texto)
		preco = float(input(texto))

		pause()

		texto = "Digite a porcentagem de desconto: "
		engine.say(texto)
		desconto = float(input(texto))
	
		preco_desconto = (preco * desconto / 100)
		valor_final = preco - preco_desconto
		
		texto = f"O produto que custava R$ {preco:.2f} com {desconto:.0f}% de desconto vai custar R${valor_final:.2f}."
		print(texto)
		engine.say(texto)

		fim()

	except ValueError:
		erroNum()

if exercicio == "013":
	limparTela()

	print("Exercício Python 013")
	print("Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.")
	espacos()

	try:

		texto = "Digite o salário do funcionário: R$ "
		engine.say(texto)
		salario = float(input(texto))

		pause()
		texto = "Digite a porcentagem de aumento: "
		engine.say(texto)
		aumento = float(input(texto))
		
		salario_aumento = (salario * aumento / 100)
		novo_salario = salario + salario_aumento
		
		texto = f"O funcionário que ganhava R$ {salario:.2f} com {aumento:.0f}% de aumento vai passar a ganhar R$ {novo_salario:.2f}."
		print(texto)
		engine.say(texto)
		fim()

	except ValueError:
		erroNum()

if exercicio == "014":
	limparTela()

	print("Exercício Python 014")
	print("Crie um programa que converta uma temperatura digitada em °C e converta para °F.")
	espacos()

	try:

		texto = "Digite a temperatura em Celsius: "
		engine.say(texto)
		celsius = float(input(texto))

		fahrenheit = (celsius * 9/5) + 32
		
		texto1 = f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F."
		print(texto1)
		engine.say(texto1)

		pause()

		limparTela()

		texto = "Digite a temperatura em Fahrenheit: "
		engine.say(texto)
		fahrenheit = float(input(texto))

		celsius = (fahrenheit - 32) * 5/9

		texto2 = f"{fahrenheit:.2f}°F equivalem a {celsius:.2f}°C."
		print(texto2)
		engine.say(texto2)
		fim()

	except ValueError:
		erroNum()

if exercicio == "015":
	limparTela()

	print("Exercício Python 015")
	print("Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.")
	espacos()

	try:

		texto = "Digite a quantidade de quilômetros percorridos: "
		engine.say(texto)
		km = float(input(texto))

		pause()

		texto = "Digite a quantidade de dias alugados: "
		engine.say(texto)
		dias = int(input(texto))

		preco_km = km * 0.15
		preco_dias = dias * 60
		preco_total = preco_km + preco_dias

		texto = f"O preço a pagar é R$ {preco_total:.2f}."
		print(texto)
		engine.say(texto)
		fim()

	except ValueError:
		erroNum()

if exercicio == "016":
	limparTela()

	print("Exercício Python 016")
	print("Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.")
	espacos()

	import math

	try:

		texto = "Digite um número: "
		engine.say(texto)
		num = float(input(texto))

		texto1 = f"A porção inteira (trunc) de {num} é {math.trunc(num)}."
		print(texto1)
		engine.say(texto1)

		pause()

		limparTela()

		texto2 = f"A porção inteira (int) de {num} é {int(num)}."
		print(texto2)
		engine.say(texto2)
		fim()

	except ValueError:
		erroNum()

if exercicio == "017":
	limparTela()

	print("Exercício Python 017")
	print("Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.")
	espacos()

	try:

		texto = "Digite o comprimento do cateto oposto: "
		engine.say(texto)
		cat_oposto = float(input(texto))

		pause()

		texto = "Digite o comprimento do cateto adjacente: "
		engine.say(texto)
		cat_adjacente = float(input(texto))

		hipotenusa = math.hypot(cat_oposto, cat_adjacente)

		texto = f"A hipotenusa vai medir {hipotenusa:.2f}."
		print(texto)
		engine.say(texto)
		fim()

	except ValueError:
		erroNum()

if exercicio == "018":
	limparTela()

	print("Exercício Python 018")
	print("Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.")
	espacos()

	try:

		texto = "Digite um ângulo em graus: "
		engine.say(texto)
		angulo_graus = float(input(texto))

		angulo_radianos = math.radians(angulo_graus)

		seno = math.sin(angulo_radianos)
		cosseno = math.cos(angulo_radianos)
		tangente = math.tan(angulo_radianos)

		texto1 = f"O seno de {angulo_graus:.2f}° é {seno:.2f}."
		print(texto1)
		engine.say(texto1)

		texto2 = f"O cosseno de {angulo_graus:.2f}° é {cosseno:.2f}."
		print(texto2)
		engine.say(texto2)

		texto3 = f"A tangente de {angulo_graus:.2f}° é {tangente:.2f}."
		print(texto3)
		engine.say(texto3)

		fim()

	except ValueError:
		erroNum()