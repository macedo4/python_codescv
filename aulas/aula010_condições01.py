"""tempo = int(input("Seu carro tem quantos anos? "))
if tempo <= 3:
    print("Você tem um carro novo")
else:
    print("Você tem um carro velho.")"""
"""nome = str(input("Qual o seu nome? ")).upper()
if nome == "GUSTAVO":
    print("Belo nome.")
else:
    print("Que nome normal.")"""
nota1 = float(input("Digite sua nota: "))
nota2 = float(input("DIgite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = (nota1 + nota2) / 2
if media <= 6:
    print(f"Sua média foi abaixo de 6.0. Estude mais! | Média: {media:.1f} ")
else:
    print(f"Sua média foi maior de 6.0. Parabéns! | Média: {media:.1f}")
