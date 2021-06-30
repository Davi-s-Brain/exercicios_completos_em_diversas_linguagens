#Letra correspondente no alfabeto
letra = int(input("Digite um número de 1 a 15:"))
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
for i in alfabeto:
    if alfabeto[letra] == i:
        print("A letra correspondente é",alfabeto[letra-1])


'''
0 == a
1 == b
2 == c
etc
'''
