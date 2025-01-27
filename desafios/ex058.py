"""Jogo da Adivinhação 2.0"""
tentativas = 0
from random import randint
numero_escolhido_pc = randint(1,5)
print("Bem-vindo ao Jogo da Adivinhação de Erica")
seu_numero = int(input("Escolha um número de 1 - 5: "))
while seu_numero != numero_escolhido_pc:
    tentativas +=1
    print('Ops... Você errou')
    seu_numero = int(input("Escolha um número de 1 - 5: "))
print(f'Você acertou e precisou de {tentativas} tentativas, derrotaste Erica')