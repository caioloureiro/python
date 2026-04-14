"""Exercício Python 008: Conversão de metros"""
from .helpers import limparTela, espacos, fim, erroNum, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 8')

	print("Exercício Python 008")
	enunciado = "Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."
	print(enunciado)
	engine.say(enunciado)
	pause()
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
