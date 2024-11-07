r1 = float(input("Digite a primeira reta: "))
r2 = float(input("DIgite a segunda reta: "))
r3 = float(input("DIgite a terceira reta: "))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print("Ótimo, forma um triângulo.")
else:
    print("Não forma um triângulo.")