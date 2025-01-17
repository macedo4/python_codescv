print("Índice de Massa Corporal(IMC)")
print("Tabela de IMC")
print("""
    IMC 	            Classificação 	Obesidade (grau)
    Menor que 18,5 	    Magreza 	            0
    Entre 18,5 e 24,9 	Normal 	                0
    Entre 25,0 e 29,9 	Sobrepeso 	            I
    Entre 30,0 e 39,9 	Obesidade 	            II
    Maior que 40,0 	    Obesidade Grave 	    III""")
peso = float(input("Digite o seu peso: (Kg)"))
altura = float(input("Digite a sua altura: "))
imc_calc = peso / (altura * altura)

if imc_calc < 18.5:
    print(f"IMC: {imc_calc:.2f} - Magreza")
elif imc_calc > 18.5 and imc_calc < 24.9:
    print(f"IMC: {imc_calc:.2f} - Normal")
elif imc_calc > 25.0 and imc_calc < 29.9:
    print(f"IMC: {imc_calc:.2f} - Sobrepeso, Obesidade(grau) I")
    if imc_calc > 30.0 and imc_calc < 39.9:
        print(f"IMC: {imc_calc:.2f} - Obesidade, Obesidade(grau) II")
        if imc_calc > 40.0:
            print(f"IMC: {imc_calc:.2f} - Obesidade Grave, Obesidade(grau) III")
