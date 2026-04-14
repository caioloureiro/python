"""Exercício Python 002: Leia o nome e mostre boas-vindas"""
from .helpers import limparTela, espacos, pause, fim
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()

	print("Exercício Python 002")
	print("Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.")
	espacos()

	texto = "Digite o seu nome: "
	engine.say(texto)
	nome = input(texto)

	texto = f"Olá {nome}! Prazer em te conhecer!"
	print(texto)
	engine.say(texto)
	fim()
