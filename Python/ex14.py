#Calcula a hipotenusa
def triangulaçao(t1,t2):
    return (((t1**2)+(t2**2))**(1/2))
cateto_1 = float(input("Valor do cateto 1:"))
cateto_2 = float(input("Valor do cateto 2:"))
print(triangulaçao(cateto_1,cateto_2))
