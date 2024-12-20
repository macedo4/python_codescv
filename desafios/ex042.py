print("Analisando Triangulos 2.0")
try:#Entradas
    a = float(input("Digite o primeiro segmento: "))
    b = float(input("Digite o segundo segmento: "))
    c = float(input("Digite o terceiro segmento: "))
except ValueError:
    print("Perdão, seus digitos são inválidos. Por favor, tente novamente.")
#Existência de triângulo.
if (a+b > c) and (a+c > b) and (b+a > c) and (b+c > a) and (c+a > b):
    print("Triângulo Válido")
    if (a==b) and (a==c) and (b==a) and (b==c) and (c==a) and (c==b):
        print("Triângulo Equilátero")
    elif (a==b) and (a==c) and (b==c) and (c==b):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não a formação de Triângulos")



