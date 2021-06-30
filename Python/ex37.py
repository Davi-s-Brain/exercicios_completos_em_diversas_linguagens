from ex36 import imc
resposta = "s"
while resposta == "s":
    peso = float(input("Digite seu peso:"))
    altura = float(input("Digite sua altura:"))
    print(imc(peso,altura))
    resposta = input("Deseja realizar novos cálculos(s/n)?")        
print("Finalizando programa...")