"""Exercício Python 021: Reproduzir arquivo MP3"""
from .helpers import limparTela, espacos, fim, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 9')

	print("Exercício Python 021")
	enunciado = "Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()

	try:

		texto = "Digite o caminho do arquivo MP3: "
		engine.say(texto)
		caminho_mp3 = input(texto)

		if os.path.isfile(caminho_mp3) and caminho_mp3.lower().endswith('.mp3'):
			engine.say(f"Reproduzindo {caminho_mp3}")
			engine.runAndWait()
			os.startfile(caminho_mp3)
			fim()
		else:
			texto = "Erro: arquivo não encontrado ou formato inválido. Certifique-se de digitar o caminho correto de um arquivo MP3."
			print(texto)
			engine.say(texto)
			fim()

	except Exception as e:
		texto = f"Erro ao tentar reproduzir o áudio: {e}"
		print(texto)
		engine.say(texto)
		fim()
