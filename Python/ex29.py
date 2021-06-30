# SOMA OS NÚMEROS DE UM INTERVALO
num = int(input("Número inteiro aqui:"))
soma = 0
if num < 0:
    print("Números positivos por favor!")
for num in range(1, num + 1):
    soma += num
print(f"A soma dos números entre {1} e {num} é {soma}")