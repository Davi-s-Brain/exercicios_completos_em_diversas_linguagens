#Cria uma lista digitada pelo usuário
x = int(input("Quantos números tu pretende colocar?"))
lista = []
for i in range(1,x):
    lista.append(input("Digita ae:"))
    ultimo = len(lista)
    if ultimo == -1:
        lista.clear()
    print(lista)

