soma_total = 0
while True: 
    produto = float(input("Valor produto"))
    soma_total = soma_total + produto
    print(f"O total parcial é de R${soma_total}")
    continua = input("Deseja continuar?[s, f]: ")
    if continua == "f" :
        break
print(f"Total da compra = {soma_total}") 
 

