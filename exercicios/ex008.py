"""Exercício Python 008: Conversão de metros"""
from .helpers import limparTela, espacos, fim, erroNum
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()

	print("Exercício Python 008")
	print("Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.")
	espacos()

	try:
		engine.say("Digite um valor em metros")
		metros = float(input("Digite um valor em metros: "))

		texto = f"{metros} metros equivalem a {metros*100} centímetros e {metros*1000} milímetros."
		print(texto)
		engine.say(texto)
		fim()

	except ValueError:
		erroNum()
