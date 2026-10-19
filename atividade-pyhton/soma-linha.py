import random

def imprime_matriz(matriz):
    for linha in matriz:
        for numero in linha:
            print(f"{numero}", end=" ")
        print()

while True:
    
    linhas = int(input("Digite a quantidade de linhas da matriz: "))
    colunas = int(input("Digite a quantidade de colunas da matriz: "))
    
   
    matriz = [[random.randint(1, 100) for C in range(colunas)] for L in range(linhas)]
    
    print("\n MATRIZ GERADA ")
    imprime_matriz(matriz)
    
        
    linha_escolhida = int(input(f"Selecione a linha que deseja somar (1 a {linhas}): "))
    
    if 1 <= linha_escolhida <= linhas:
        inicio_linha = linha_escolhida - 1
        
        soma = sum(matriz[inicio_linha])
        
        print(f"-> A soma dos elementos da linha {linha_escolhida} é: {soma}\n")
    else:
        print("Erro: Linha inválida para o tamanho desta matriz.\n")
        
    nova_matriz = input("Deseja criar outra matriz? [s/n]: ").lower()
    if nova_matriz == 'n':
        print("Programa encerrado.")
        break
