atleta_idade = int(input("DIgite sua idade: "))
if atleta_idade <= 9:
    print("Categoria: MIRIM")
elif atleta_idade <= 14:
    print("Categoria: INFANTIL")
elif atleta_idade <= 19:
    print("Categoria: JUNIOR")
elif atleta_idade <= 20:
    print("Categoria: SENIOR")
else:
    print("Categoria: MASTER")