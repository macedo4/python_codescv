print("Soma de números")
try:
    first_number = int(input("Digite um número:  "))
    second_number = int(input("Digite mais um número: "))
    plus = first_number + second_number
    print(f"A soma dos números {first_number} + {second_number} = {plus}")
except ValueError:
    print("Digite números válidos, por favor.")