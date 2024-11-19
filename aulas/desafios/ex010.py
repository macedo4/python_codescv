print("Quantos dólares você pode comprar? ")
real = float(input("Quantos reais você tem em sua carteira? R$"))
valor_dolar_atual = 5.67
quantidade_dolares = real / valor_dolar_atual
print((f"Você pode comprar US${quantidade_dolares:.2f} dólares."))
