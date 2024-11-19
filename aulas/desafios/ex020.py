from random import shuffle

pessoa1 = str(input("Digite o nome da pessoa: "))
pessoa2 = str(input("Digite o nome da pessoa: "))
pessoa3 = str(input("Digite o nome da pessoa: "))
pessoa4 = str(input("Digite o nome da pessoa: "))
pessoas = [pessoa3, pessoa4, pessoa2, pessoa1]
shuffle(pessoas)
print("A ordem de apresentação será: \n=======")
print(pessoas)
