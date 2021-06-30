#Quadrado perfeito
def quadrado_maroto(n):
    '''for num in range(1,101):
        if (n**(1/2)) % num == 0:
            return True
        else:
            return False'''
    return (n**(1/2)) % 1 == 0


numero = int(input("Digite um número entre 1 e 100:"))
print(quadrado_maroto(numero))