#Vê o IMC e indica a faixa de peso da pessoa
def imc(pes,alt):
    imc = pes/(alt**2)
    if imc <= 18.5:
        print("Você está abaixo do peso! Vá ao médico!") # Abaixo do peso
    elif imc > 18.5 and imc < 24.9:
        print("Você está com o peso normal, parabéns!") # Peso normal
    elif imc > 25 and imc < 29.9:
        print("Você está acima do peso ideal, puta merda mano!") # Sobrepeso
    elif imc > 30 and imc < 34.9:
        print("Você está com Obesidade I, meu Deus do céu!") # Obesidade I
    elif imc > 35 and imc < 39.9:
        print("Você está com Obesidade II, vai pro médico AGORA!!") # Obeisdade II
    elif imc > 40:
        print("Você vai morrer, Obeisdade III.") # Obesidade III
    print("Imc = {:.2f}".format(imc)) # Printa o IMC
    return " "
#peso = float(input("Digite seu peso:"))
#altura = float(input("Digite sua altura:"))
#print(imc(peso,altura))