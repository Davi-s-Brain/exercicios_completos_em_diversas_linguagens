#Converte metros por segundo para quilometros
def converte_flash(kilometros):
    return kilometros / 3.6
velocidade_da_luz = float(input("Digite a velocidade em metros por segundo\npara saber em kilometros por hora:"))
print(converte_flash(velocidade_da_luz))
