distancia =  float(input("Digite a distência em Km/h: "))

if distancia < 200.00:
    preco = distancia * 0.50
else:
    preco = distancia * 0.25

print(f"Sua passagem custa: R${preco:.2f}")
