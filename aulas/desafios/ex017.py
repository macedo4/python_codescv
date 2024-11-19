#Calculo da Hipotenusa
catetoposto = float(input("Digite o cateto oposto: "))
catetoadjacente = float(input("Digite o cateto adjacente: "))
hipotenusa = (catetoposto ** 2 + catetoadjacente ** 2) ** (1/2)
print(f"Utilizando o calculo da hipotenusa:{hipotenusa:.2f}")

#Usando a Biblioteca math
from math import hypot
hipotenusa_bibl= hypot(catetoposto, catetoadjacente)
print(f"Utilizando a biblioteca(math) {hipotenusa_bibl:.2f}")
