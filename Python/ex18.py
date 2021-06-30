# coding=utf-8
# O usuário digita o número de colunas e linhas e eu faço o que devo fazer

tabuleiro = int(input("Qual o tamanho do tabuleiro você quer?(De 1 a 10)"))

def matriz(mat):
    linha = ("#--" * tabuleiro) + "#" + "\n"
    coluna  = ("|  " * tabuleiro) + "|" + "\n"
    print(((f"{linha}{coluna}")*tabuleiro)+linha)

matriz(tabuleiro)
