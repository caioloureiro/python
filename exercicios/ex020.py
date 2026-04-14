"""Exercício Python 020: Sortear ordem de apresentação"""
from .helpers import limparTela, espacos, fim, fim2, erroNum, pause
import pyttsx3
import random
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color bf')

	print("Exercício Python 020")
	enunciado = "O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."
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

		random.shuffle(alunos)

		texto = "A ordem de apresentação dos trabalhos será:"
		print(texto)
		engine.say(texto)

		for i, aluno in enumerate(alunos, start=1):
			texto_linha = f"{i}º - {aluno}"
			print(texto_linha)
			engine.say(texto_linha)

		pause()
		fim()

	except ValueError:
		erroNum()
