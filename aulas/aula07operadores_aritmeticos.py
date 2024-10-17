#operadores aritmeticos
# + soma
# * multiplicação
#/ divisão
#/ divisão
# ** potencia
# % resto da divisão
#// divisão inteira(divisão inteira nada de float

#ordem de precedencia
'''
1) ()
2) ** potencia
3) *, /, //, %
4) +, -

posição de palavras
{:=^20} centralizado

'''
print("pratica")
recebevalor = int(input("Digite um valor: "))
recebevlor2 = int(input("Digite outro valor: "))
soma = recebevalor + recebevlor2
multi = recebevalor * recebevlor2
divi = recebevalor / recebevlor2
potencia = recebevalor ** recebevlor2
resto = recebevalor % recebevlor2
#\n quebra a linha
#,end='" não quebra a linha
print(f'Informações: \n produto: {multi} - soma: {soma} - divi: {divi:.2f} - potencia: {potencia} - resto: {resto}')




































