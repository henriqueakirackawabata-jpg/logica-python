import random

def soma_matrizes(linhas, colunas):

    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            linha.append(random.randint(1, 10))
        matriz.append(linha)
    return matriz

def somar_matrizes(m1, m2, linhas, colunas):

    matriz_res = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(m1[i][j] + m2[i][j])
        matriz_res.append(linha)
    return matriz_res

def formatar_matriz(matriz):

    elementos = []
    for linha in matriz:
        for num in linha:
            elementos.append(str(num))
    return " ".join(elementos)


linhas = 3
colunas = 3

matriz1 =  soma_matrizes(linhas, colunas)
matriz2 =  soma_matrizes(linhas, colunas)
resultado = somar_matrizes(matriz1, matriz2, linhas, colunas)

print(f"Matriz 1: {formatar_matriz(matriz1)}")
print(f"Matriz 2: {formatar_matriz(matriz2)}")
print(f"Matriz resultado: {formatar_matriz(resultado)}")
