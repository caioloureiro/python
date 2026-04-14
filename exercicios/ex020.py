"""Exercício Python 020: Sortear ordem de apresentação"""
from .helpers import limparTela, espacos, fim, erroNum
import pyttsx3
import random

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()

	print("Exercício Python 020")
	print("O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.")
	espacos()

	try:

		alunos = []
		for i in range(4):
			texto = f"Digite o nome do aluno {i+1}: "
			engine.say(texto)
			aluno = input(texto)
			alunos.append(aluno)

		random.shuffle(alunos)

		texto = "A ordem de apresentação dos trabalhos será:"
		print(texto)
		engine.say(texto)

		for i, aluno in enumerate(alunos, start=1):
			texto_linha = f"{i}º - {aluno}"
			print(texto_linha)
			engine.say(texto_linha)

		fim()

	except ValueError:
		erroNum()
