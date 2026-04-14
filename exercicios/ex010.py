"""Exercício Python 010: Conversão de moedas"""
from .helpers import limparTela, espacos, pause, fim, erroNum
import pyttsx3
import requests
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 9')

	print("Exercício Python 010")
	enunciado = "Crie um programa que leia um valor em reais e o converta para dólares."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()

	def buscar_dolar():
		try:
			url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
			resposta = requests.get(url)
			dados = resposta.json()
			return float(dados["USDBRL"]["bid"])
		except requests.exceptions.ConnectionError:
			print("Erro: sem conexão com a internet.")
			return None
		except Exception as e:
			print(f"Erro ao buscar cotação: {e}")
			return None

	dolar = buscar_dolar()
	if dolar is not None:
		try:

			texto = "Digite um valor em reais: "
			engine.say(texto)
			reais = float(input(texto))

			convertido = reais / dolar
			texto = f"Com R$ {reais:.2f} você pode comprar US$ {convertido:.2f} (cotação: R$ {dolar:.2f})."
			print(texto)
			engine.say(texto)

			pause()

			limparTela()

			texto = "Digite um valor em dólares: "
			engine.say(texto)
			dolares = float(input(texto))

			convertido_reais = dolares * dolar
			texto = f"Com US${dolares:.2f} você pode comprar R$ {convertido_reais:.2f} (cotação: R$ {dolar:.2f})."
			print(texto)
			engine.say(texto)

			fim()

		except ValueError:
			erroNum()
