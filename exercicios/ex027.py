"""Exercício Python 027: Primeiro e último nome de uma pessoa"""
from .helpers import limparTela, espacos, fim, pause
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()
	os.system('color 7f')

	print("Exercício Python 027")
	enunciado = "Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()
	
	nome_completo = input("Digite o nome completo da pessoa: ")
	engine.say(f"Você digitou: {nome_completo}")
	
	nomes = nome_completo.strip().split()
	
	if len(nomes) < 2:
		print("Erro: Digite um nome completo (primeiro e último nome)!")
		engine.say("Erro: Digite um nome completo com primeiro e último nome")
		espacos()
		fim()
		return
	
	primeiro_nome = nomes[0]
	ultimo_nome = nomes[-1]
	
	espacos()
	print(f"Primeiro nome: {primeiro_nome}")
	engine.say(f"Primeiro nome: {primeiro_nome}")
	espacos()
	
	print(f"Último nome: {ultimo_nome}")
	engine.say(f"Último nome: {ultimo_nome}")
	espacos()
	
	fim()
