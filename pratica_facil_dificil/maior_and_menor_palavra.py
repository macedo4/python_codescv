palavras = ["python", "asimov", "código", "web", "programação"]
maior_palavra = palavras[0]
menor_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    elif len(palavra) < len(menor_palavra):
        menor_palavra = palavra
print(f"A menor palavra é: {menor_palavra}")
print(f"A maior a palavra é: {maior_palavra}")