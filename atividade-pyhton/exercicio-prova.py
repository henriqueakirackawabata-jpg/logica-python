def classificar_estudante():
    idade = int(input("Insira a idade do estudante: "))
    if idade < 5:
        print("O estudante é um bebê")
    elif idade < 12:
        print("O estudante é uma criança")
    elif idade < 18:
        print("O estudante é um adolescente")
    else:
         print("O estudante é um adulto")

classificar_estudante()