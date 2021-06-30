#Vê se é primo ou não
def primo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True       

#num = int(input("Digite um número para ver se o mesmo é primo ou não:"))
#print(primo(num))