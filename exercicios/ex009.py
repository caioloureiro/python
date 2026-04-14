"""Exercício Python 009: Tabuada"""
from .helpers import limparTela, espacos, fim, erroNum
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
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
