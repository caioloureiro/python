"""Exercício Python 021: Reproduzir arquivo MP3"""
from .helpers import limparTela, espacos, fim, pause
import pyttsx3
import os
import pygame

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

	print('Executando o audio...')

	espacos()

	pygame.init()
	pygame.mixer.music.load('issets/sonic.mp3')
	pygame.mixer.music.play()
	pygame.event.wait()
	
	fim()
