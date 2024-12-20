nome = str(input("Qual é o seu nome? "))
if nome == 'Macedo':
    print("Que nome bonito")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Nome bem conhecido")
elif nome in 'Karem Safira Priscila':
    print("Belo nome feminino")
else:
    print("Nome normal")
print(f"Tenha um bom dia {nome}")