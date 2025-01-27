num = cont = maior_num = menor_num = soma = 0
respo = 'S'
while respo == 'S':
    num = int(input('Digite um número: '))
    respo = str(input('Quer continuar? [S/N]')).upper()
    cont += 1
    soma += num
    if cont == 1:
        maior_num = num
        menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        if num < menor_num:
            menor_num = num
media = soma / cont
print(f'Você digitou {cont} números e média deles é {media:.1f}')
print(f'O maior número {maior_num} e o menor número {menor_num}')