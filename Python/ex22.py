#VÊ SE O b, DENTRO DE UM MÊS, É VÁLIDO OU NÃO
def mes_daora(a,b):
    if a == 1 or a == 3 or a == 5 or a == 8 or a == 10 or a == 12 or a == 7:
        return b <= 31
    elif a == 2:
        return b <= 29
    if a == 4 or a == 6 or a == 11 or a == 9:
        return b <= 30
    if a > 12:
        return "Você é palhaço né? Não vou te retornar nada, até porque não existe."
    if b < 0 or b > 31:
        return False

#mes = int(input("Digite o número do mês:"))
#dia = int(input("Digite o número do dia a ser verificado:"))
#print(mes_daora(mes,dia))