print("ALuguel de carro")
dias = int(input("Quantos dias alugados? "))
distancia_rodada = float(input("Distância percorrida: "))
conta_dias = dias * 60
conta_km = distancia_rodada * 0.15
total = conta_dias + conta_km
print(f"Você vai pagar R${total:.2f}")