"""Exercício Python 022: Nome completo - maiúsculas, minúsculas e análise de letras"""
from .helpers import limparTela, espacos, fim, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 0e')

	print("Exercício Python 022")
	enunciado = "Crie um programa que leia o nome completo de uma pessoa e mostre: o nome em maiúsculas, o nome em minúsculas, a quantidade de letras sem espaços e a quantidade de letras do primeiro nome."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()
	
	nome = input("Digite o nome completo da pessoa: ")
	engine.say(f"Você digitou: {nome}")
	
	nome_maiusculo = nome.upper()
	nome_minusculo = nome.lower()
	quantidade_letras = len(nome.replace(" ", ""))
	primeiro_nome = nome.split()[0]
	quantidade_primeiro_nome = len(primeiro_nome)
	
	espacos()
	print(f"Nome em MAIÚSCULAS: {nome_maiusculo}")
	engine.say(f"Nome em maiúsculas: {nome_maiusculo}")
	espacos()
	
	print(f"Nome em minúsculas: {nome_minusculo}")
	engine.say(f"Nome em minúsculas: {nome_minusculo}")
	espacos()
	
	print(f"Quantidade de letras sem espaços: {quantidade_letras}")
	engine.say(f"Quantidade de letras sem espaços: {quantidade_letras}")
	espacos()
	
	print(f"Quantidade de letras do primeiro nome: {quantidade_primeiro_nome}")
	engine.say(f"Quantidade de letras do primeiro nome: {quantidade_primeiro_nome}")
	espacos()
	
	fim()
