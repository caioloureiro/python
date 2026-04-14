# EXERCÍCIOS PYTHON - CURSO EM VÍDEO
import os
import sys
import pyautogui
import keyboard
import pyttsx3
import time
from exercicios.helpers import VoltarAoMenu

# Inicializa o motor de voz
engine = pyttsx3.init()

# Configura a velocidade (opcional)
engine.setProperty('rate', 255)

# No Windows, envia o comando de tela cheia
pyautogui.hotkey('alt', 'enter')

# Configurar hotkey para ESC - escreve "exit" e pressiona ENTER
def sair_com_esc():
	"""Função chamada quando ESC é pressionado"""
	os.system('color 4')
	pyautogui.typewrite('exit', interval=0)
	keyboard.press('enter')

keyboard.add_hotkey('esc', sair_com_esc)

# Loop principal para voltar ao menu
while True:
	#Tela de seleção de exercícios
	os.system('color 0a')
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
	"019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.\n" \
	"020 - O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.\n" \
	"021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.\n"
	"\n" \
	"Pressione ESC para sair.\n\n"
	"")

	texto = "Digite o número do exercício que deseja executar: "
	engine.say(f"{texto} ou pressione ESC para sair.")
	engine.runAndWait()

	exercicio = input(texto)

	# Se ESC foi pressionado, a entrada será "exit"
	if exercicio == "exit":
		print("Até logo!")
		time.sleep(1)
		sys.exit(0)

	# Se não for um número, mostra erro
	if not exercicio.isdigit():
		texto = "Erro: digite apenas números."
		print(texto)
		engine.say(texto)
		continue

	# Importa e executa o exercício selecionado
	try:
		if exercicio == "000":
			from exercicios import ex000
			ex000.executar()
		elif exercicio == "001":
			from exercicios import ex001
			ex001.executar()
		elif exercicio == "002":
			from exercicios import ex002
			ex002.executar()
		elif exercicio == "003":
			from exercicios import ex003
			ex003.executar()
		elif exercicio == "004":
			from exercicios import ex004
			ex004.executar()
		elif exercicio == "005":
			from exercicios import ex005
			ex005.executar()
		elif exercicio == "006":
			from exercicios import ex006
			ex006.executar()
		elif exercicio == "007":
			from exercicios import ex007
			ex007.executar()
		elif exercicio == "008":
			from exercicios import ex008
			ex008.executar()
		elif exercicio == "009":
			from exercicios import ex009
			ex009.executar()
		elif exercicio == "010":
			from exercicios import ex010
			ex010.executar()
		elif exercicio == "011":
			from exercicios import ex011
			ex011.executar()
		elif exercicio == "012":
			from exercicios import ex012
			ex012.executar()
		elif exercicio == "013":
			from exercicios import ex013
			ex013.executar()
		elif exercicio == "014":
			from exercicios import ex014
			ex014.executar()
		elif exercicio == "015":
			from exercicios import ex015
			ex015.executar()
		elif exercicio == "016":
			from exercicios import ex016
			ex016.executar()
		elif exercicio == "017":
			from exercicios import ex017
			ex017.executar()
		elif exercicio == "018":
			from exercicios import ex018
			ex018.executar()
		elif exercicio == "019":
			from exercicios import ex019
			ex019.executar()
		elif exercicio == "020":
			from exercicios import ex020
			ex020.executar()
		elif exercicio == "021":
			from exercicios import ex021
			ex021.executar()
		else:
			texto = "Exercício não encontrado!"
			print(texto)
			engine.say(texto)
	except VoltarAoMenu:
		# Volta ao menu sem exibir erro
		continue
	except Exception as e:
		texto = f"Erro ao carregar o exercício: {e}"
		print(texto)
		engine.say(texto)