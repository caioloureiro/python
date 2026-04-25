"""Exercício Python 025: Verificar se há SILVA no nome"""
from .helpers import limparTela, espacos, fim, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 0e')

	print("Exercício Python 025")
	enunciado = "Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()
	
	nome = input("Digite o nome de uma pessoa: ")
	engine.say(f"Você digitou: {nome}")
	
	nome_maiusculo = nome.upper().strip()
	
	espacos()
	if "SILVA" in nome_maiusculo:
		mensagem = f"A pessoa '{nome}' tem SILVA no nome."
		print(mensagem)
		engine.say(mensagem)
	else:
		mensagem = f"A pessoa '{nome}' NÃO tem SILVA no nome."
		print(mensagem)
		engine.say(mensagem)
	
	espacos()
	fim()
