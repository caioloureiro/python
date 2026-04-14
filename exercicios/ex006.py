"""Exercício Python 006: Dobro, triplo e raiz quadrada"""
from .helpers import limparTela, espacos, fim, erroNum, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 6')
	print("Exercício Python 006")
	enunciado = "Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada."
	print(enunciado)
	engine.say(enunciado)
	pause()
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
