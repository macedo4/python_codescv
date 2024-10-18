print("Desconto em preços")
preço = float(input('Qual o preço? R$'))
desconto = preço - (preço*5/100)
print(f"O produto na qual custa R${preço:.2f} com o desconto de %5 passa ser de R${desconto:.2f}")
