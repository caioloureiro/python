"""Exercício Python 012: Desconto"""
from .helpers import limparTela, espacos, pause, fim, erroNum
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()

	print("Exercício Python 012")
	print("Crie um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.")
	espacos()

	try:

		texto = "Digite o preço do produto: "
		engine.say(texto)
		preco = float(input(texto))

		pause()

		texto = "Digite a porcentagem de desconto: "
		engine.say(texto)
		desconto = float(input(texto))
	
		preco_desconto = (preco * desconto / 100)
		valor_final = preco - preco_desconto
		
		texto = f"O produto que custava R$ {preco:.2f} com {desconto:.0f}% de desconto vai custar R${valor_final:.2f}."
		print(texto)
		engine.say(texto)

		fim()

	except ValueError:
		erroNum()
