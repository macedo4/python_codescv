print("Média de notas")
nota_one = float(input("Qual sua primeira nota? "))
nota_two = float(input("Qual sua segunda nota? "))
media_de_notas = (nota_one+nota_two) / 2
if media_de_notas < 5.0:
    print(f"Média: {media_de_notas:.1f} Reprovado!")
elif media_de_notas == 5 or media_de_notas == 6:
    print(f"Média: {media_de_notas:.1f} Recuperação!")
else:
    print(f"Média: {media_de_notas:.1f} Aprovado")