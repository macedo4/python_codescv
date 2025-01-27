num = int(input('Digite um número para ver seu fatorial: '))
if num < 0:
    print('Números negativos não tem fatorial')
else:
    fatorial = 1
    calculo = ""
    for c in range(num, 0, -1):
        fatorial *= c
        if c == 1:
            calculo += f' {c} '
        else:
            calculo += f' {c} x'
    print(f'{num}! = {calculo} = {fatorial}')