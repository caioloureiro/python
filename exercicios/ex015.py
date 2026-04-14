"""Exercício Python 015: Preço de aluguel de carro"""
from .helpers import limparTela, espacos, pause, fim, erroNum
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 4')

	print("Exercício Python 015")
	enunciado = "Crie um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()

	try:

		texto = "Digite a quantidade de quilômetros percorridos: "
		engine.say(texto)
		km = float(input(texto))

		pause()

		texto = "Digite a quantidade de dias alugados: "
		engine.say(texto)
		dias = int(input(texto))

		preco_km = km * 0.15
		preco_dias = dias * 60
		preco_total = preco_km + preco_dias

		texto = f"O preço a pagar é R$ {preco_total:.2f}."
		print(texto)
		engine.say(texto)
		fim()

	except ValueError:
		erroNum()
