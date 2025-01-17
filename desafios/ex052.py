# Solicita um número inteiro ao usuário
num = int(input('Digite um número: '))

# Inicializa o contador de divisores
tot = 0

# Verifica os divisores do número
print("Analisando divisores:")
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[31m{c}\033[0m', end=' ')  # Divisor destacado em vermelho
        tot += 1
    else:
        print(f'\033[37m{c}\033[0m', end=' ')  # Não divisores em branco

# Resultado final
print(f'\n\nO número {num} foi dividido {tot} vezes.')

# Verifica se é primo
if tot == 2:
    print(f'O número {num} é \033[32mPRIMO\033[0m.')
else:
    print(f'O número {num} \033[31mNÃO é PRIMO\033[0m.')
