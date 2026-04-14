"""Exercício Python 018: Seno, cosseno e tangente"""
from .helpers import limparTela, espacos, fim, erroNum, pause
import pyttsx3
import math
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 9f')

	print("Exercício Python 018")
	enunciado = "Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."
	print(enunciado)
	engine.say(enunciado)
	pause()
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
