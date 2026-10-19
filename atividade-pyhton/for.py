import random

num_int = random.randint(1, 100)
print(f"\nNúmeros aleatórios entre 1 e 100: ")

matriz = [[0 for coluna in  range(3)] for linha in range(2)]
 
for linha in range(2):
     for coluna in range(3):
        print(matriz[linha][coluna], end=" ")
     print()

matriz[0][1] = 3
print() 
for linha in range(2):
     for coluna in range(3):
         print(matriz[linha][coluna], end=" ")
     print()



