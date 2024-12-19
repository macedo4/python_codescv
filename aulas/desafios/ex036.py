print("GO!")
valor_da_casa = float(input("Informe o valor da casa: R$"))
seu_salario_comprador = float(input("Digite o seu salário atual: R$"))
anos = int(input("Em quantos anos planeja pagar?  "))

meses = anos * 12
prestacao = valor_da_casa / meses

limite = 0.3 * seu_salario_comprador

print("Resumo de informações: ")
print(f"Valor da casa: R${valor_da_casa:.2f}")
print(f"Prazo: {anos} anos {meses} meses")
print(f"Salário atual do comprador: R${seu_salario_comprador:.2f}")
print(f"Prestação: R${prestacao:.3f}")
print(f"Limite: {limite}")

if prestacao <= limite:
    print("Parábens, empréstimo aprovado.")
elif prestacao > limite:
    print("Empréstimo negado, limite ultrapassado")
