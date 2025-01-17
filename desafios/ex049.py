cont = 0
soma = 0
for c in range(1,7):
    num_user = int(input(f'Digite o {c}º número: '))
    cont = num_user
    if cont % 2 == 0:
        soma = soma + num_user
        cont += 1
print(f"Você informou {cont} números PARES e a soma deles é {soma}")
