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
	
	numero = int(input("Digite um número entre 0 e 9999: "))
	engine.say(f"Você digitou: {numero}")
	
	if numero < 0 or numero > 9999:
		print("Erro: o número deve estar entre 0 e 9999!")
		engine.say("Erro: o número deve estar entre 0 e 9999!")
		espacos()
		fim()
		return
	
	# Formata com zeros à esquerda
	numero_str = str(numero).zfill(4)
	
	milhar = int(numero_str[0])
	centena = int(numero_str[1])
	dezena = int(numero_str[2])
	unidade = int(numero_str[3])
	
	espacos()
	print(f"Milhar: {milhar}")
	engine.say(f"Milhar: {milhar}")
	espacos()
	
	print(f"Centena: {centena}")
	engine.say(f"Centena: {centena}")
	espacos()
	
	print(f"Dezena: {dezena}")
	engine.say(f"Dezena: {dezena}")
	espacos()
	
	print(f"Unidade: {unidade}")
	engine.say(f"Unidade: {unidade}")
	espacos()
	
	fim()
