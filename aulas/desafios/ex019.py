import random
aluno1 = str(input("Digite o nome do 1º aluno(a): "))
aluno2 = str(input("Digite o nome do 2º aluno(a): "))
aluno3 = str(input("Digite o nome do 3º aluno(a): "))
aluno4 = str(input("Digite o nome do 4º aluno(a): "))
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido_da_lua = random.choice(alunos)
print(f"Aluno(a) escolhido foi {escolhido_da_lua}")