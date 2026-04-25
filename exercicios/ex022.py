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
	
	nome = str(input("Digite o nome completo da pessoa: ")).strip()
	engine.say(f"Você digitou: {nome}")
	
	nome_maiusculo = nome.upper()
	nome_minusculo = nome.lower()
	nome_sem_espacos = nome.replace(" ", "")
	quantidade_letras = len(nome_sem_espacos)
	primeiro_nome = nome.split()[0]
	quantidade_primeiro_nome = len(primeiro_nome)
	
	espacos()

	texto01 = f"Nome em MAIÚSCULAS: {nome_maiusculo}"
	print(texto01)
	engine.say(texto01)
	espacos()
	
	texto02 = f"Nome em minúsculas: {nome_minusculo}"
	print(texto02)
	engine.say(texto02)
	espacos()
	
	texto03 = f"Quantidade de letras sem espaços: {quantidade_letras}"
	print(texto03)
	engine.say(texto03)
	espacos()
	
	texto04 = f"Quantidade de letras do primeiro nome: {quantidade_primeiro_nome}"
	print(texto04)
	engine.say(texto04)
	espacos()
	
	fim()
