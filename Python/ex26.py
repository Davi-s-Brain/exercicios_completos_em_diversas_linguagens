#ORDENA OS NÚMEROS 
n1 = int(input("Primeiro número:"))
n2 = int(input("Segundo número:"))
n3 = int(input("Terceiro número:"))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(n3,n2,n1) 
    else:
        print(n2,n3,n1) #Pronto, arrumado, CATAPIMBA
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print(n3,n1,n2)
    else:
        print(n1,n3,n2) #PEWN
if n3 > n1 and n3 > n2:
    if n2 > n1:
        print(n1,n2,n3)
    else:
        print(n2,n1,n3) #ACABOU GARAY