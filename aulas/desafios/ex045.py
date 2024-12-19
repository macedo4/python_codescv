from random import randint
from time import sleep
print("Pedra, Papel e Tesoura")
print("""
[1] Pedra
[2] Papel
[3] Tesoura""")
jogador = int(input("Qual sua opção: "))
maquina = randint(1,3)
if jogador == maquina:
    print("Verificando resultados....")
    sleep(2)
    print("Empate")
#JOgador vence#

elif jogador == 1 and maquina == 3:
    print("Verificando resultados....")
    sleep(2)
    print("Jogador = Pedra | Maquina = Tesoura | Jogador vence ")
elif jogador == 2 and maquina == 1:
    print("Verificando resultados....")
    sleep(2)
    print("Jogador = Papel | Maquina = Pedra | Jogador vence ")
elif jogador == 3 and maquina == 2:
    print("Verificando resultados....")
    sleep(2)
    print("Jogador = Tesoura | Maquina = Papel | Jogador vence ")

#Maquina vence
elif maquina == 1 and jogador == 3:
    print("Verificando resultados....")
    sleep(2)
    print("Maquina = Pedra Jogador = Tesoura | Maquina vence ")
elif maquina == 2 and jogador == 1:
    print("Verificando resultados....")
    sleep(2)
    print("Maquina = Papel Jogador = Pedra | Maquina vence ")
elif maquina == 3 and jogador == 2:
    print("Verificando resultados....")
    sleep(2)
    print("Maquina = Tesoura Jogador = Papel | Maquina vence ")

print("Bom jogo")
