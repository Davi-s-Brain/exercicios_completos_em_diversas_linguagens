# VÊ SE OS NÚMEROS SÃO DIVISÍVEIS POR 3 E POR 7
soma_tres = 0
for num in range(1,201):
    if num % 3 == 0 or num % 7 == 0:
        soma_tres += num
print(soma_tres)
