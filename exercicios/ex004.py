"""Exercício Python 004: Informações sobre o tipo primitivo"""
from .helpers import limparTela, espacos, pause, fim2
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 4')

	print("Exercício Python 004")
	enunciado = "Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()

	texto = "Digite algo: "

	engine.say(texto)
	valor = input(texto)

	texto = f"Você digitou: {valor}"
	print(texto)
	engine.say(texto)
	pause()

	if valor.isspace():
		print(f"Só tem espaços? {valor.isspace()}")
		engine.say("Só tem espaços")
		pause()

	if valor.isnumeric():
		print(f"É numérico? {valor.isnumeric()}")
		engine.say("É numérico")
		pause()

	if valor.isalpha():
		print(f"É letra? {valor.isalpha()}")
		engine.say("É letra")
		pause()

	if valor.isalnum():
		print(f"É alfanumérico? {valor.isalnum()}")
		engine.say("É alfanumérico")
		pause()

	if valor.isupper():
		print(f"É maiúsculo? {valor.isupper()}")
		engine.say("É maiúsculo")
		pause()

	if valor.islower():
		print(f"É minúsculo? {valor.islower()}")
		engine.say("É minúsculo")
		pause()

	if valor.istitle():
		print(f"Está capitalizado? {valor.istitle()}")
		engine.say("Está capitalizado")
		pause()
	
	fim2()
