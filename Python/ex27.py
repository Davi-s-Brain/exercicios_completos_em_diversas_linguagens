#CONTA QUANTAS VEZES UM NÚMERO APARECE EM UM NÚMERO COM 3 ALGARISMOS
num = int(input("Digite um número de 3 unidades:"))
d = int(input("Digite apenas 1 número:"))
cont = 0

ultimo = num % 10 
meio = (num // 10) % 10
primeiro = ((num // 10) // 10) % 10

if ultimo == d:
    cont +=  1
if meio == d:
    cont += 1
if primeiro == d:
    cont +=  1
print(cont)
