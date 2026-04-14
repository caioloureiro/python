"""Exercício Python 007: Média entre duas notas"""
from .helpers import limparTela, espacos, pause, fim, erroNum
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()

	print("Exercício Python 007")
	enunciado = "Crie um programa que leia duas notas de um aluno e mostre a sua média."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()

	try:

		engine.say("Digite a primeira nota")

		n1 = float(input("Digite a primeira nota: "))

		pause()

		engine.say("Digite a segunda nota")

		n2 = float(input("Digite a segunda nota: "))

		media = (n1 + n2) / 2
		
		texto = f"A média entre {n1} e {n2} é {media:.2f}"
		print(texto)
		engine.say(texto)
		
		resultado = "Aprovado" if media >= 7 else "Reprovado"
		
		espacos()
		
		print(f"Resultado: {resultado}")
		engine.say(f"Resultado: {resultado}")

		fim()
		
	except ValueError:
		erroNum()
