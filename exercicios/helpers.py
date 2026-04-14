"""Funções auxiliares para os exercícios"""
import os
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 255)

# Exceção customizada para voltar ao menu
class VoltarAoMenu(Exception):
	"""Exceção para sinalizar que deve voltar ao menu de exercícios"""
	pass

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
	"""Volta ao menu com áudio"""
	texto = "Pressione Enter para voltar ao menu..."
	engine.say(texto)
	engine.runAndWait()
	input(texto)
	limparTela()
	raise VoltarAoMenu()

def fim2():
	"""Volta ao menu sem esperar áudio terminar"""
	texto = "Pressione Enter para voltar ao menu..."
	engine.say(texto)
	input(texto)
	limparTela()
	raise VoltarAoMenu()

def sair():
	"""Finaliza o programa sem áudio"""
	texto = "Pressione Enter para finalizar..."
	engine.say(texto)
	engine.runAndWait()
	input(texto)
	exit()

def sair2():
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
