"""Jogo da Adivinhação: """
from random import randint
numero_escolhido_pc = randint(1,5)
print("Bem-vindo ao Jogo da Adivinhação de Erica")
seu_numero = int(input("Escolha um número de 1 - 5: "))
if seu_numero == numero_escolhido_pc:
    print("Parabéns, acertastes o número escolhido!")
else:
    print(f"Errou! Erica escolheu {numero_escolhido_pc}")
print("FiM")