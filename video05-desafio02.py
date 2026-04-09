# Criar um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
nome = input("Digite seu nome: ")
dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

print(f"Olá {nome}! Você nasceu no dia {dia:02d} de {mes:02d} de {ano}.")

espere = input("Pressione Enter para sair...")