word_user = str(input('Digite uma frase: ')).strip().upper()
word = word_user.split()
not_space = ''.join(word)
if not_space == not_space[::-1]:
    print(f'A frase "{not_space}" é um palíndromo.')
else:
    print(f'A frase "{not_space}" não é um palíndromo.')