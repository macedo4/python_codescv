from datetime import date
maiorIdade = 0
menorIdade = 0
data_atual = date.today().year
for c in range(1,8):
    datas_nascimentos = int(input(f'Quando a {c}ª pessoa nasceu? '))
    idade =  data_atual - datas_nascimentos
    if idade >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1
print(f'Resumindo, tivemos {maiorIdade} pessoas maiores de idade')
print(f'Resumindo, tivemos {menorIdade} pessoas menores de idade')