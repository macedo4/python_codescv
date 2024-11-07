print("Sistemas de Velocidade")
print("Velocidade permitida: 80Km/h")
velocidade_motorista = float(input("Sua velocidade: "))
velocidade_permitida = 80
base_de_multa = ( velocidade_motorista - velocidade_permitida) * 7
if velocidade_motorista > velocidade_permitida:
    print(f"Multado! multa de R${base_de_multa:.2f}")
else:
    print("Sem multa, siga em frente.")