"""Exercício Python 014: Conversão de temperatura"""
from .helpers import limparTela, espacos, pause, fim, erroNum
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 5f')

	print("Exercício Python 014")
	enunciado = "Crie um programa que converta uma temperatura digitada em Celsius e converta para Fahrenheit."
	print(enunciado)
	engine.say(enunciado)
	pause()
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
