print(("Média de notas"))
try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    if media < 6:
        print(("Reprovado"))
    else:
        print("Aprovado")
    print((f"A média final é {media:.1f}"))
except ValueError:
    print("Digite notas válidas")