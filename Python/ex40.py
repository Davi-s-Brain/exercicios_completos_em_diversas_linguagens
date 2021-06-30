# Troca a posição dos valores na lista
numerinhos = [1, 5, 42, 72]

def troca(i1,i2):
    y = numerinhos[i2] 
    x = numerinhos[i1]
    numerinhos[i1] = y
    numerinhos[i2] = x
    print(numerinhos)


num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
troca(num1,num2) 