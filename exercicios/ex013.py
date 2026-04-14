"""Exercício Python 013: Aumento de salário"""
from .helpers import limparTela, espacos, pause, fim, erroNum
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()

	print("Exercício Python 013")
	enunciado = "Crie um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()

	try:

		texto = "Digite o salário do funcionário: R$ "
		engine.say(texto)
		salario = float(input(texto))

		pause()
		texto = "Digite a porcentagem de aumento: "
		engine.say(texto)
		aumento = float(input(texto))
		
		salario_aumento = (salario * aumento / 100)
		novo_salario = salario + salario_aumento
		
		texto = f"O funcionário que ganhava R$ {salario:.2f} com {aumento:.0f}% de aumento vai passar a ganhar R$ {novo_salario:.2f}."
		print(texto)
		engine.say(texto)
		fim()

	except ValueError:
		erroNum()
