'''
 i = 10
while i >= 0:
    print(i)
    i -= 1 
else:
    print("Lançando foguete") 
'''

'''
index = 0
while index <= 10:
    print(index)
    index += 1
'''
'''
index = 1
while index <= 10:
    if index == 5:
        break
    print(index)
    index = index +1
'''


'''
i = 0
while i <= 10:
    if i %2 !=0:
        i += 1
    continue
print(i, end=" ")
i += 1
'''


while True:
    fruta = input("Digite o nome da fruta: ")
    print(f"Fruta: {fruta}")
    continua = input("Deseja continuar execuando? [s,n]: ").lower()
    if continua == "n":
        break