"""Exercício Python 024: Verificar se cidade começa com SANTO"""
from .helpers import limparTela, espacos, fim, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 0e')

	print("Exercício Python 024")
	enunciado = "Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()
	
	cidade = input("Digite o nome de uma cidade: ")
	engine.say(f"Você digitou: {cidade}")
	
	cidade_maiuscula = cidade.upper().strip()
	
	espacos()
	if cidade_maiuscula.startswith("SANTO"):
		mensagem = f"A cidade '{cidade}' começa com SANTO."
		print(mensagem)
		engine.say(mensagem)
	else:
		mensagem = f"A cidade '{cidade}' NÃO começa com SANTO."
		print(mensagem)
		engine.say(mensagem)
	
	espacos()
	fim()
