#DE 3, VÊ QUEM É O MAIOR
n1 = int(input("Primeiro número:"))
n2 = int(input("Segundo número:"))
n3 = int(input("Terceiro número:"))
def os_maiorais(a,b,c):
    if a > b and a > c:
        print(f"{a} é o maior")
    if b > a and b > c:
        print(f"{b} é o maior")
    if c > a and c > b:
        print(f"{c} é o maior")

os_maiorais(n1,n2,n3)