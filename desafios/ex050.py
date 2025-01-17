primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da progressão aritmética: "))
decimo = primeiro_termo + (10-1) * razao
for c in range(primeiro_termo,decimo+razao,razao):
    print(f'{c}',end='➡️')