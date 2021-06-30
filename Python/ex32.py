# QUANTAS VOGAIS TEM UM PALAVRA
palavra = input("Digite uma palavra para saber quantas vogais ela possui:")
vogais = 0
for i in palavra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vogais += 1
print(vogais)
