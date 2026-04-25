"""Exercício Python 026: Análise da letra A em uma frase"""
from .helpers import limparTela, espacos, fim, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 0e')

	print("Exercício Python 026")
	enunciado = "Crie um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra 'A', em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()
	
	frase = input("Digite uma frase: ")
	engine.say(f"Você digitou: {frase}")
	
	frase_maiuscula = frase.upper()
	
	quantidade_a = frase_maiuscula.count("A")
	primeira_posicao = frase_maiuscula.find("A")
	ultima_posicao = frase_maiuscula.rfind("A")
	
	espacos()
	print(f"Quantidade de vezes que a letra 'A' aparece: {quantidade_a}")
	engine.say(f"Quantidade de vezes que a letra A aparece: {quantidade_a}")
	espacos()
	
	if primeira_posicao != -1:
		print(f"Primeira posição da letra 'A': {primeira_posicao + 1} (posição {primeira_posicao} a partir de 0)")
		engine.say(f"Primeira posição da letra A: {primeira_posicao + 1}")
	else:
		print("A letra 'A' não foi encontrada na frase.")
		engine.say("A letra A não foi encontrada na frase.")
	
	espacos()
	
	if ultima_posicao != -1:
		print(f"Última posição da letra 'A': {ultima_posicao + 1} (posição {ultima_posicao} a partir de 0)")
		engine.say(f"Última posição da letra A: {ultima_posicao + 1}")
	else:
		print("A letra 'A' não foi encontrada na frase.")
		engine.say("A letra A não foi encontrada na frase.")
	
	espacos()
	fim()
