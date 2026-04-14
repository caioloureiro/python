"""Exercício Python 019: Sortear aluno para apagar o quadro"""
from .helpers import limparTela, espacos, fim, erroNum, pause
import pyttsx3
import random

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()

	print("Exercício Python 019")
	enunciado = "Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()

	try:

		alunos = []
		for i in range(4):
			texto = f"Digite o nome do aluno {i+1}: "
			engine.say(texto)
			aluno = input(texto)
			alunos.append(aluno)
			pause()

		escolhido = random.choice(alunos)

		texto = f"O aluno escolhido para apagar o quadro é: {escolhido}."
		print(texto)
		engine.say(texto)
		fim()

	except ValueError:
		erroNum()
