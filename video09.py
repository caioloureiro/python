# Video 09 - Tipagem de dados e formatação de strings
# Sobre print f-strings
# As f-strings facilitam muito a formatação de números e datas, que são as "máscaras" propriamente ditas:
# Objetivo	Código com f-string	Resultado (Exemplo)
# Casas Decimais	f"{valor:.2f}"	10.50
# Preenchimento	f"{numero:03d}"	007
# Separador de Milhar	f"{total:,}"	1,000,000
# Datas	f"{hoje:%d/%m/%Y}"	10/04/2026
# Resumo: qual usar?
# Use sempre f-strings (f"{variável}"). 
# Só utilize .format() se estiver trabalhando em um sistema muito antigo (Python 2.7 ou 3.5 para baixo) 
# ou se precisar montar a string dinamicamente antes de conhecer os valores.

import os

def limparTela():
    # 'nt' refere-se ao Windows, 'posix' ao Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def mudarTela():
    input("")
    limparTela()
    
def espacos():
	print("")
	print("")
	print("")

print("Tipagem de dados")
print("Int - Números inteiros")
print("Float - Números decimais")
print("Str - Textos")
print("Bool - Valores lógicos (True ou False)")

mudarTela()

n1 = int(input('Digite um valor: '))
print(type(n1))

n2 = int(input('Digite um valor: '))
print(type(n2))

s = n1 + n2
print(f'A soma entre {n1} e {n2} é igual a {s}.')

mudarTela()

n = bool(input('Digite algo: '))
print(n)
print(type(n))

mudarTela()

o = input('Digite outra coisa: ')
print(o)
print(type(o))
print("É numérico?")
print(o.isnumeric())
print("É letra?")
print(o.isalpha())
print("É Alphanumérico?")
print(o.isalnum())
print("É maiúsculo?")
print(o.isupper())

mudarTela()