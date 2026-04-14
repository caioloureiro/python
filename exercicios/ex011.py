"""Exercício Python 011: Cálculo de tinta para parede"""
from .helpers import limparTela, espacos, pause, fim, erroNum
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 255)

def executar():
	limparTela()

	print("Exercício Python 011")
	enunciado = "Crie um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta necessária para pintá-la."
	print(enunciado)
	engine.say(enunciado)
	pause()
	espacos()

	try:

		texto = "Digite a largura da parede em metros: "
		engine.say(texto)
		largura = float(input(texto))

		pause()

		texto = "Digite a altura da parede em metros: "
		engine.say(texto)
		altura = float(input(texto))

		area = largura * altura
		tinta = area / 2

		texto1 = f"Sua parede tem {largura:.2f}x{altura:.2f} metros."
		print(texto1)
		engine.say(texto1)

		texto2 = f"A área da parede é {area:.2f} m²."
		print(texto2)
		engine.say(texto2)

		texto3 = f"Você precisará de {tinta:.2f} litros de tinta para pintar a parede."
		print(texto3)
		engine.say(texto3)

		fim()

	except ValueError:
		erroNum()
