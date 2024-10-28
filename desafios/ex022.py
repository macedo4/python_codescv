nome = str(input("Nome: "))
mai = nome.upper()
min = nome.lower()
primeironome = len(nome.split()[0])
semspaco = len(nome.replace(' ', ''))
print(f"""============================
        - Seu nome em minúsculo: {min}.
        - Seu nome em maiúsculo: {mai}.
        - Primeiro nome tem {primeironome} caracteres.
        - Sem espaço temos: {semspaco} caracteres.""")