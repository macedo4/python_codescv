primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão aritmética: '))

n_termos = 10
termo_atual = primeiro_termo
contador = 0

while n_termos != 0:
    total_de_termos = contador + n_termos
    while contador < total_de_termos:
        print(f'{termo_atual}',end='➡️' )
        contador += 1
        termo_atual += razao
    print('PAUSA')
    n_termos = int(input('Quantos termos a mais você quer exibir? '))
print(f'Finalizado, foram {contador} termos exibidos')