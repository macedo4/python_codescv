#Atribuindo uma string em uma variavel
frase = 'Curso em Vídeo Python'
#Fatiamento de string:
print(frase[9])
print(frase[9:14])#seleciona tudo a partir da posição 9 e até a posição 14
print(frase[9::3])#seleciona tudo a partir da posição 9
print(frase[-5:])#seleciona tudo a partir da posição -5, contando do fim da string
print(frase[:20])#seleciona tudo até a posição 20
print(frase[::2])#seleciona tudo, pulando de 2 em 2
print(frase[::-1])#seleciona tudo, inverte a ordem
#Analise de string
print(len(frase)) #comprimento da string
print(frase.count('o')) #conta quantas vezes aparece 'o'
print(frase.find('Vídeo')) #procura 'Vídeo' na string e retorna a posição
print(frase.strip()) #remove espaço em branco no início e no final da string
print(frase.split()) #divide a string em uma lista de palavras
print(frase.startswith('Curso')) #verifica se a string começa com 'Curso'
print(frase.endswith('Python')) #verifica se a string termina com 'Python'
print(frase.lower().count('o')) #conta quantas vezes aparece 'o' em minúsculo
print(frase.upper().count('O')) #conta quantas vezes aparece 'O' em maiúsculo
print(frase.lower().capitalize()) #coloca a primeira letra da primeira palavra em maiúsculo e deixa as outras em minúsculo
print(frase.title()) #coloca a primeira letra de cada palavra em maiúsculo
print(frase.replace('Python', 'Java')) #substitui 'Python' por 'Java'
print(frase.lower()) #converte tudo para minúsculo
print(frase.upper()) #converte tudo para maiúsculo
print(frase.capitalize()) #coloca a primeira letra da primeira palavra em maiúsculo e deixa as outras em minúsculo
print(frase.title()) #coloca a primeira letra de cada palavra em maiúsculo
print(frase.replace('Python', 'Java')) #substitui 'Python' por 'Java'
print('Curso' in frase) #verifica se 'Curso' está presente na string
print(frase.rstrip())#trabalhando pela direita
print(frase.lstrip())#trabalhando pela esquerda

