maiorPeso = 0
menorPeso = 0
for c in range(1,5):
    peso_pessoas = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maiorPeso = peso_pessoas
        menorPeso = peso_pessoas
    else:
        if peso_pessoas > maiorPeso:
            maiorPeso = peso_pessoas
        if peso_pessoas < menorPeso:
            menorPeso = peso_pessoas
print(f"O maior peso é {maiorPeso}Kg")
print(f"O menor peso é {menorPeso}kg")