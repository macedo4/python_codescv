#for c in range(0,6):
#    print('oi')
#print("fim")


#para pular de 2 em 2= for c in range(0,7,2):


#contagem regressiva
#for c in range(6,0,-1):
#    print(c)
#print('finalizado')

#contagem progressiva:
#for c in range(0,7):
    #print(c)

inicio = int(input("Inicio :"))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
for c in range(inicio, fim+1, passo):
    print(c)

#somatorio
s = 0
for c in range(0,5):
    n = int(input("Digite um número: "))
    s += n
print(s)