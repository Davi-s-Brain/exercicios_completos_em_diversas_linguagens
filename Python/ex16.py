#Faz o mesmo que o anterior mas N vezes é repetido
palavra = input("Digite uma palavra:")
delimitador = input("Digite o que vai separar as palavras:")
repete = int(input("Quantas vezes você quer repetir isso?"))

def palavras_ao_vento(palav, delim, n):
    return ((palav + delim)*(n-1)) + palav
print(palavras_ao_vento(palavra,delimitador,repete))
