#Faça um agoritmo para mostrar uma matriz de orde N x M com os elementos aleatórios.

import random

def imprime_matriz(matriz):
    for linha in range(m):
        for coluna in range(n):
            print(matriz[linha][coluna], end=" ")
        print()

while True:
    m = int(input("Selecione a linha: "))
    n = int(input("Selecione a coluna: "))
    matriz = [[random.randint(1, 100) for coluna in range(n)] for linha in range(m)]
    imprime_matriz(matriz)
    continua = input("\nDeseja continuar?[s,n]: ").lower()
    if continua == "n":
        break 














#Faça um algoritmo para somar a linha de uma matriz passando o numero da linha.