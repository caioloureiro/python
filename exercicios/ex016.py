"""Exercício Python 016: Porção inteira de um número"""
from .helpers import limparTela, espacos, pause, fim, erroNum
import pyttsx3
import math

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()

	print("Exercício Python 016")
	print("Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.")
	espacos()

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
