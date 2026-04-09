# Crie um script Python que leia dois números e tente mostrar a soma entre eles. 
# Caso o usuário digite algo que não seja um número, mostre uma mensagem de erro e não deixe o programa ser interrompido.

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

try:
    numero1 = int(numero1)
    numero2 = int(numero2)
    soma = numero1 + numero2
    print(f"A soma dos números é: {soma}")
except ValueError:
    print("Erro: Você deve digitar apenas números.")

espere = input("Pressione Enter para sair...")