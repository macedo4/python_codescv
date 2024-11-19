from math import trunc
numeroreal = float(input("Digite um número real: "))
parteinteira = trunc(numeroreal)
print(f"Parte inteira: {parteinteira}")
#outra forma:
numeromesmo = float(input("Digite um número real: "))
print(f"Parte inteira: {int(numeromesmo)}")