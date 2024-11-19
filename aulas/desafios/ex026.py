frase = str(input("Frase: ")).strip().upper()
contagem_a = frase.count("A")
primeira_posicao = frase.find("A")+1
ultima_posicao = frase.rfind("A") + 1
print(f"A letra 'A' apareceu {contagem_a} vezes na frase")
print(f"A sua primeira aparição foi na posição {primeira_posicao}.")
print(f"E apareceu na posição {ultima_posicao}, sua última aparição.")