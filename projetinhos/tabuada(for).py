#Trabalhando com Bibliotecas
from time import sleep
#Iniciando Varíaveis
op = 0
#Entrada...
num = int(input('Digite um número: '))
while op !=6:
    #Menu de opções
    sleep(1)
    print("""
    ===========================
    MENU
    [1] Soma
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [5] Novo número
    [6] Sair
    ===========================
    """)
    #Escolhendo uma opção
    print('=-'*10)
    op = int(input('Escolha uma opção: '))
    print('=-'*10)
    #Soma
    if op == 1:
        for c in range(1,11):
            print(f'{num} + {c} = {num + c}')
    #Subtração
    elif op == 2:
        for c in range(1,11):
            print(f'{num} - {c} = {num - c}')
    #Multiplicação
    elif op == 3:
        for c in range(1,11):
            print(f'{num} *  {c} = {num * c}')
    #Divisão
    elif op == 4:
        if num == 0:
            print('A divisão por zero não é possivel')
        else:
            for c in range(1,11):
                    print(f'{num} / {c} =  {num / c:.1f}')
    #Novos números
    elif op == 5:
        num = int(input("Digite um novo número: "))
    #Entrada invalida
    elif op != 6:
        print('Opção inválida. Tente novamente.')