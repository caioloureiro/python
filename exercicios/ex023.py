"""Exercício Python 023: Análise de dígitos de um número"""
from .helpers import limparTela, espacos, fim, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 0e')

	print("Exercício Python 023")
	enunciado = "Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados, ou seja, unidade, dezena, centena e milhar."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()
	
	engine.say(f"Digite um número entre 0 e 9999: ")
	numero = int(input("Digite um número entre 0 e 9999: "))

	pause()
	
	if numero < 0 or numero > 9999:
		print("Erro: o número deve estar entre 0 e 9999!")
		engine.say("Erro: o número deve estar entre 0 e 9999!")
		espacos()
		fim()
		return
	
	# Formata com zeros à esquerda
	# numero_str = str(numero).zfill(4)
	# unidade = int(numero_str[3])
	# dezena = int(numero_str[2])
	# centena = int(numero_str[1])
	# milhar = int(numero_str[0])

	unidade = numero // 1 % 10
	dezena = numero // 10 % 10
	centena = numero // 100 % 10
	milhar = numero // 1000 % 10
	
	espacos()

	texto04 = f"Unidade: {unidade}"
	print(texto04)
	engine.say(texto04)
	espacos()
	
	texto03 = f"Dezena: {dezena}"
	print(texto03)
	engine.say(texto03)
	espacos()
	
	texto02 = f"Centena: {centena}"
	print(texto02)
	engine.say(texto02)
	espacos()
	
	texto01 = f"Milhar: {milhar}"
	print(texto01)
	engine.say(texto01)
	espacos()
	
	fim()
