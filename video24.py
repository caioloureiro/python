# Aula 08 - Utilizando Módulos

# import normal
# import math

# import específico
# from math import sqrt

# import específico com alias
# from math import sqrt, ceil

# https://www.python.org/

import pyttsx3
import math
import random
import emoji

engine = pyttsx3.init()
engine.setProperty('rate', 255)
engine.runAndWait()

def fim():
	prtFim = "Pressione Enter para sair..."
	engine.say(prtFim)
	engine.runAndWait()
	input(prtFim)

engine.say("Digite um número para calcular a raiz quadrada")
valor = input("Digite um número para calcular a raiz quadrada: ")

raiz = math.sqrt(float(valor))

num = random.randint(1, 100)

prt = f"A raiz quadrada de {valor} é {raiz}. \n" \
f"A raiz quadrada de {valor} é {math.ceil(raiz)} arredondado pra cima. \n" \
f"A raiz quadrada de {valor} é {math.floor(raiz)} arredondado pra baixo. \n" \
f"O número aleatório gerado é {num}. \n" \
f"O emoji de coração é {emoji.emojize(':red_heart:')}. \n"

print(prt)
engine.say(prt)

fim()