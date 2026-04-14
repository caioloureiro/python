"""Exercício Python 003: Leia dois números e mostre a soma"""
from .helpers import limparTela, espacos, pause, fim, erroNum
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 3')

	print("Exercício Python 003")
	enunciado = "Crie um programa que leia dois números e mostre a soma entre eles."
	print(enunciado)
	engine.say(enunciado)
	pause()
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
