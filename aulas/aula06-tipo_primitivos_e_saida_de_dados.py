
'''
TIpos primitivos:
Int=4 - 9 - 10
Bool= True - False
Str = "ola" - "5"
float = "5.7"

Podemos ver o tipo:
print(type(n1))
metodos para ver se possivel converter
print(n1.isnumeric()) #todos os caracteres são numericos?
print(n1.isalpha()) #todos os caracteres são letras?
print(n1.isdigit()) #todos os caracteres são digitos?
print(n1.isalnum()) #todos os caracteres são alphanumericos?
obs
print(n1.isupper()) #todas a letras são maiusculas
print(n1.islower()) #todas a letras são minusculas
print(n1.swapcase()) #converte maiusculas para minusculas e minusculas para maiusculas

print(n1.capitalize()) #primeira letra em maiuscula e o resto em minuscula
print(n1.upper()) #todas as letras em maiuscula
print(n1.lower()) #todas as letras em minuscula

print(n1.replace('5', 'X')) #substitui o caracter '5' por 'X'
print(n1.lstrip('5')) #remove caracteres a esquerda até encontrar um diferente de '5'
print(n1.rstrip('5')) #remove caracteres a direita até encontrar um diferente de '5'

print(n1.split('5')) #divide a string em uma lista de strings usando o separador '5'

print(n1.count('5')) #conta quantas vezes o caracter '5' aparece na string

print(n1.startswith('5')) #verifica se a string começa com '5'
print(n1.endswith('5')) #verifica se a string termina com '5'

print(n1.find('5')) #retorna o indice do primeiro caracter '5' na string
print(n1.rfind('5')) #retorna o indice do ultimo caracter '5' na string

print(n1.format(n2)) #substitui {} com o valor de n2
print(f"{n1} + {n2} = {soma}") #f-string

print(float(n1)) #converte para float
print(int(n1)) #converte para inteiro

print(bin(n1)) #converte para binario
print(oct(n1)) #converte para octal
print(hex(n1)) #converte para hexadecimal

#Funções

   
Conversões:

'''
