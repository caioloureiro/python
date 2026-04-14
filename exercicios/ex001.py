"""Exercício Python 001: Escreva 'Olá, Mundo!' na tela"""
from .helpers import limparTela, espacos, fim, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 1f')

	print("Exercício Python 001")
	enunciado = "Crie um programa que escreva 'Olá, Mundo!' na tela."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()
	texto = "Olá, Mundo!"
	print(texto)
	engine.say(texto)
	espacos()
	fim()