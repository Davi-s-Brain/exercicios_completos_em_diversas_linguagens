#ANALISADOR DE TRIÂNGULOS
print("ANALISE SEUS TRIÂNGULOS")
r1 = int(input("Primeiro valor:"))
r2 = int(input("Segundo valor:"))
r3 = int(input("Terceiro valor:"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("AS RETAS PODEM FORMAR UM TRIÂNGULO!!!")
else:
    print("AS RETAS NÃO PODEM FORMAR UM TRIÂNGULO!!")
