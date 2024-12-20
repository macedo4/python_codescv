print("Alistamento Militar Exército Brasileiro.")
nome_user = str(input("Digite o seu nome completo: "))
ano_de_nascimento = int(input("Por favor, informe quando você nasceu: "))
idade_max = 45
idade_min = 18
ano_atual = 2024
idade = ano_atual - ano_de_nascimento
tempo_que_falta = idade_min - idade
if idade < idade_min:
    print(f"Prezado {nome_user}, lamentamos. Mas você tem {idade} anos, ainda faltam {tempo_que_falta} anos para se alistar.")
elif idade == idade_min:
    print("Você já tem a idade adequada para se alistar.")
elif idade > idade_max:
    print("Você não pode mais se alistar.")
else:
    print("Você ainda pode se alistar.")