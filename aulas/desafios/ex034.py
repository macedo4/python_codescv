seu_salario = float(input("Digite seu salário: R$"))
salario_maximo = 1250
if seu_salario >= salario_maximo:
    aumento10 = (seu_salario*10/100) + seu_salario
    print(f"Seu salário com 10% de aumento é R${aumento10:.2f}")
else:
    aumento15 = (seu_salario*15/100) + seu_salario
    print(f"Seu salário com 15% de aumento é R${aumento15:.2f}")