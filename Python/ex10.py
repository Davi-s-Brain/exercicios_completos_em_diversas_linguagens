massa = float(input("Digite seu peso para calcular seu IMC:"))
alt = float(input("Digite agora sua altura:"))
imc = massa / (alt * alt) 
print("Seu IMC é {:.2f}".format(imc))
