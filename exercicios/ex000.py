"""Exercício Python 001: Escreva 'Olá, Mundo!' na tela"""
from .helpers import limparTela, espacos, fim, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 0a')

	os.system('curl parrot.live')
	
	pause()