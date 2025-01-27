masc = 'M'
feme = 'F'
sexo = str(input('Sexo: ')).upper()
while sexo != masc and sexo != feme:
    print('Sexo inválido. Por favor, digite M para masculino ou F para feminino.')
    sexo = str(input('Sexo: ')).upper()
print('Obrigado pela informação.')