"""Exercício Python 005: Antecessor e sucessor"""
from .helpers import limparTela, espacos, fim, erroNum, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 5')

	print("Exercício Python 005")
	enunciado = "Crie um programa que leia um número e mostre o seu antecessor e o seu sucessor."
	print(enunciado)
	engine.say(enunciado)
	pause()
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
