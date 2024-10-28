numero = int(input("Número: "))
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000
print(f'Unidade: {unidade} '
      f'Dezena: {dezena} '
      f'Centena: {centena} '
      f'Milhar: {milhar} ')
