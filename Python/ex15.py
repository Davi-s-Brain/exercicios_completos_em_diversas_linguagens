#Separa as palavras por barras, vírgulas entre outros
palavras_ao_vento = input("Digite uma palavra:")
delineador = input("Digite um delimitador para a palavra:")

def separa_os_coisos(palavrinha,separador):
    return (palavrinha + separador + palavrinha)
print(separa_os_coisos(palavras_ao_vento,delineador))
