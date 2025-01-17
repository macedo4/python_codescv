#trabalhando com bibliotecas = c
from time import sleep
#declaração de variaveis e interacao com usuario = c
nome_aluno = str(input('Digite seu nome: '))
av1 = float(input('Digite a nota da sua primeira avalição: '))
av2 = float(input('Digite a nota da sua segunda avaliação: '))
av3 = float(input('Digite a nota da sua terceira avaliação: '))
#calculo de media = c
media_calc = (av1 + av2 + av3) / 3
#condicoes = nf
if media_calc < 6:
    print(f'Sua média foi de: {media_calc:.1f}')
    sleep(2)
    print(f'Aluno(a) {nome_aluno} foi reprovado')
else:
    print(f'Sua média foi de: {media_calc:.1f}')
    sleep(2)
    print(f'Aluno(a) {nome_aluno} foi aprovado')
