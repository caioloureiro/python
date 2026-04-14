"""Funções auxiliares para os exercícios"""
import os
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def limparTela():
	"""Limpa a tela do console"""
	print("'nt' refere-se ao Windows, 'posix' ao Linux/Mac")
	os.system('cls' if os.name == 'nt' else 'clear')

def espacos():
	"""Imprime três linhas em branco"""
	print("")
	print("")
	print("")

def pause():
	"""Pausa e aguarda Enter com áudio"""
	texto = "Pressione Enter para continuar..."
	engine.say(texto)
	engine.runAndWait()
	input(texto)

def pause2():
	"""Pausa e aguarda Enter sem esperar áudio terminar"""
	texto = "Pressione Enter para continuar..."
	engine.say(texto)
	input(texto)

def fim():
	"""Finaliza o programa com áudio"""
	texto = "Pressione Enter para finalizar..."
	engine.say(texto)
	engine.runAndWait()
	input(texto)
	exit()

def fim2():
	"""Finaliza o programa sem esperar áudio terminar"""
	texto = "Pressione Enter para finalizar..."
	engine.say(texto)
	input(texto)
	exit()

def erroNum():
	"""Mostra erro de entrada numérica"""
	texto = "Erro: digite apenas números."
	print(texto)
	engine.say(texto)
	fim()
