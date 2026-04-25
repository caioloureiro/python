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
	print(
"""Bem-vindo aos exercícios de Python!
001 - Escreva 'Olá, Mundo!' na tela.
002 - Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
003 - Crie um programa que leia dois números e mostre a soma entre eles.
004 - Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
005 - Crie um programa que leia um número e mostre o seu antecessor e o seu sucessor.
006 - Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.
007 - Crie um programa que leia duas notas de um aluno e mostre a sua média.
008 - Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
009 - Crie um programa que leia um número e mostre a sua tabuada.
010 - Crie um programa que leia um valor em reais e o converta para dólares.
011 - Crie um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta necessária para pintá-la.
012 - Crie um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
013 - Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
014 - Crie um programa que converta uma temperatura digitada em °C e converta para °F.
015 - Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
016 - Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.
017 - Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
020 - O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
022 - Crie um programa que leia o nome completo de uma pessoa e mostre: o nome em maiúsculas, o nome em minúsculas, a quantidade de letras sem espaços e a quantidade de letras do primeiro nome.
023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados, ou seja, unidade, dezena, centena e milhar.
024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
026 - Crie um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
027 - Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente.
Pressione ESC para sair.\n\n"""
	)

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
		elif exercicio == "022":
			from exercicios import ex022
			ex022.executar()
		elif exercicio == "023":
			from exercicios import ex023
			ex023.executar()
		elif exercicio == "024":
			from exercicios import ex024
			ex024.executar()
		elif exercicio == "025":
			from exercicios import ex025
			ex025.executar()
		elif exercicio == "026":
			from exercicios import ex026
			ex026.executar()
		elif exercicio == "027":
			from exercicios import ex027
			ex027.executar()
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