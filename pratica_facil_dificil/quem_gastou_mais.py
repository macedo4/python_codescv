gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 300, 500, 700]

total_gastos_joao = sum(gastos_joao)
total_gastos_pedro = sum(gastos_pedro)

if gastos_joao > gastos_pedro:
    print("Quem gastou mais foi John")
elif gastos_pedro > gastos_joao:
    print("Quem gastou mais foi Peter")
else:
    print("Os dois gastaram a mesma quantia")

