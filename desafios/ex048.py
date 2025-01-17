soma = 0
cont = 0
for c in range(1,500,2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os valores solicitados {soma}')
print(f'A quantidade de valores solicitados {cont}')