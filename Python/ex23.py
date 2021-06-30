#VÊ SE A DATA DIGITADA É VÁLIDA OU NÃO
from ex22 import mes_daora
data = int(input("Digite o dia:"))
mês = int(input("Digite o mês:"))
ano = int(input("Digite o ano:"))
def verifica_ano(c):
    if c >= 1900 and c <= 2019:
        return True
    else:
        return False
print(mes_daora(mês,data))
print(verifica_ano(ano))