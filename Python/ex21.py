#VÊ A MÉDIA DA CRIANÇA REBELDE
def notas_loukas(num1a,num2a,num3a,num4a): 
    peso1 = 2
    peso2 = 3
    media = ((num1a*peso1)+(num2a*peso1)+(num3a*peso2)+(num4a*peso2))/10
    print(f"A média é de {media}")
    if media < 3:
        print("REPROVADO!")
    elif media >= 3 and media < 5:
        print("RECUPERAÇÃO")
    else:
        print("VOCÊ PASSOU, desta vez!")
     
num1 = float(input("Digite a primeira nota:"))
num2 = float(input("Digite a segunda nota:"))
num3 = float(input("Digite a terceira nota:"))
num4 = float(input("Digite a quarta nota:"))

notas_loukas(num1,num2,num3,num4)