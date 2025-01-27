#r = 'S'
#cont = 0
#cont_resposta = 0

#while r == 'S':
#    numero = int(input('Informe um número: '))
#    cont += 1
#    r = str(input('Quer continuar? [S/N]')).upper()
#    cont_resposta += 1
#print(f'Você informou {cont} números')



n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Informe um número: '))
    if n % 2 == 0:
        par +=1
    else:
        impar += 1
print(f'Você digitou {par-1} pares')
print(f'Você digitou {impar} impares')