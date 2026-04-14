"""Exercício Python 017: Hipotenusa de um triângulo retângulo"""
from .helpers import limparTela, espacos, pause, fim, erroNum
import pyttsx3
import math

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
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

		# hipotenusa = (cot_oposto ** 2 + cat_adjacente ** 2) ** (1/2)
		hipotenusa = math.hypot(cat_oposto, cat_adjacente)

		texto = f"A hipotenusa vai medir {hipotenusa:.2f}."
		print(texto)
		engine.say(texto)
		fim()

	except ValueError:
		erroNum()
