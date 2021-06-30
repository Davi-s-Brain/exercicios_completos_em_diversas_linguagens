# VÊ SE É VOGAL OU NÃO
def Maoe (x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    else:
        return False
Letra = input("Digite UMA letra para ver se ela é vogal:")
print(Maoe(Letra))

