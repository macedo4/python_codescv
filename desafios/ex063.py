num = cont = soma = 0
num = int(input('Digite um número [999 finaliza] '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 finaliza] '))
print(f'Você digitou {cont} números e a soma deles é {soma} ')