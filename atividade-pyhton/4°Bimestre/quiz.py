pontos = 0
while True:
    ask = int(input("Quantos países há na America Latina?: "))
    if(ask == 20 ):
        print("resposta correta")
        pontos +=1
        print(f"seus pontos são:{pontos}")
    else:
        print("resposta errada")



    copa = int(input("Quantas copas o Brasil já ganhou?: "))
    if(copa == 5 ):
        print("resposta correta")
        pontos +=1
        print(f"seus pontos são:{pontos}")
    else:
        print("resposta errada")



    brasil = int(input("Quantas capitais o Brasil tem?: "))
    if(brasil == 1):
        print("resposta correta")
        pontos +=1
        print(f"seus pontos são:{pontos}")
    else:
        print("resposta errada")


    soma = int(input("Qual é a soma de 33 + 34?: "))
    if(soma == 67 ):
        print("resposta correta")
        pontos +=1
        print(f"seus pontos são:{pontos}")
    else:
        print("resposta errada")


    anos = int(input("Quantos anos o Brasil tem?: "))
    if(anos == 526 ):
        print("resposta correta")
        pontos +=1
        print(f"seus pontos finais são:{pontos}")
    else:
        print("resposta errada")

    if pontos == 5:
        print("Parabéns voçê acertou todas!")
        break
    pontos = 0