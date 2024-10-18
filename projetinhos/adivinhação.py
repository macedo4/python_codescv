import random
numero_user = int(input("Digite um número de 1 a 10: "))
numero_escolhido = random.randint(1,10)
if numero_user == numero_escolhido:
    print("Você acertou!")
else:
    print("Você errou!")
    if numero_user > numero_escolhido:
        print("É menor")
    else:
        print("É maior")

print(f"Número do PC: {numero_escolhido}")
print(f"Seu número: {numero_user}")
