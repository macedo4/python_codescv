idade_media = 0
homem_mais_velho = 0
nome_homem_mais_velho = ''
mocas_menores_idade = 0

for c in range(1,5):
    print(f'-----{c}ª Pessoa-----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    idade_media += idade
    sexo = str(input('Sexo [F/M]: ')).upper().strip()

    if sexo == 'M' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mocas_menores_idade += 1
media_id = idade_media / 4
print('-----Resultados-----')
print(f'A média da idade do grupo é {media_id:.2f}')
print(f"O homem mais velho é {nome_homem_mais_velho} e sua idade é de {homem_mais_velho} anos")
print(f'No total são {mocas_menores_idade} mulheres como menos de 20 anos')

