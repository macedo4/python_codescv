print("=========Lojas Macedo========")

valor_de_compras = float(input("Valor total das compras: R$"))
print("""
Formas de Pagamento(surpresa escondida)
=======================
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão
========================
""")
opcoes_de_pagamento = int(input("Digite sua forma de pagamanto: [1-4] "))

if opcoes_de_pagamento == 1:
    desconto = 10
    preco_final = valor_de_compras - valor_de_compras * (desconto / 100)
    print(f"Seu preço final é R${preco_final:.2f}")

elif opcoes_de_pagamento == 2:
    desconto = 5
    preco_final = valor_de_compras - valor_de_compras * (desconto / 100)
    print(f"Seu preço final é R${preco_final:.2f}")


elif opcoes_de_pagamento == 3:
    print(f"Seu preço final {valor_de_compras:.2f}")


elif opcoes_de_pagamento == 4:
    preco_final = valor_de_compras + (valor_de_compras * 20 / 100)
    parcelas_quant = int(input("Quantas parcelas? "))
    parcelas_valor = preco_final / parcelas_quant
    print(f"Sua comprar será parcelada em {parcelas_quant}x de R${parcelas_valor:.2f} com juros")
    print(f"Sua compra de R${valor_de_compras:.2f}, agora custa R${preco_final:.2f}")
