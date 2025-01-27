valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
operacao = 0
while operacao != 5:
    print('-=-'*10)
    print('''
    =========Menu========
    [1] somar
    [2] multiplicar
    [3] maior número
    [4] novos números
    [5] sair do programa''')
    operacao = int(input('Escolha uma opção: '))
    if operacao == 1:
        print(f'A soma dos valores é {valor1 + valor2}')
    elif operacao == 2:
        print(f'A multiplicação dos valores é {valor1 * valor2}')
    elif operacao == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}')
        elif valor2 > valor1:
            print(f'O maior valor é {valor2}')
        else:
            print('Não tem maior valor')
    elif operacao == 4:
        print('Novos valores')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif operacao == 5:
        print('-=-' * 10)
        print('Saindo do programa...')
        break
print('Programa finalizado')