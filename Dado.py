#Programa que sorteia números em um dado

from random import randint #Importa o randint da biblioteca Random 

resposta = input("Quer rolar um dado? (s/n)") #Verifica se a pessoa quer rolar o dado
tratamento = resposta.lower() #Deixa a resposta em minúscula

def sorte(i):
    while (i == "s"):
        if (resposta == 's'): #Verifica a validade da resposta
            sortear = randint(1,6)
            print("o número sorteado foi {}".format(sortear))
            i = input("Quer continuar a rolar?")
    
    if (i == "n"): #Encerra o loop
        print("Adeus")    
    if (i != "n" and i != 's'):
        print("Comando inválido, tente novamente!")
    
sorte(resposta)