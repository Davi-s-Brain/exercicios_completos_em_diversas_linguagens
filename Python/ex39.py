#Vê quantos números primos tem entre 1 a n
from ex38 import primo

cont = 0
num = int(input("Digite um número:")) 
for i in range(2,num):
    if primo(i) == True:
        cont += 1

print(cont)