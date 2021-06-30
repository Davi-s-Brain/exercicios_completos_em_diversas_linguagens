
#Converte horas para segundos
def conversor(horas):
    return horas * 60 * 60
h = int(input("Quantas horas queres converter para segundos?"))
print(conversor(h))