def dia():
    Dia =int(input("selecione o dia da semana: "))
    if Dia == 1:
        print("Segunfa-feira jogar bola")
    elif Dia == 2:
        print("Terça-feira tomar sorvete")
    elif Dia == 3:
        print("Quarta-feira ir ao parque")
    if Dia >3:
        return print("Dia da semana não encontrado!")
    else:
        print("Dia escolhido com sucesso!")
dia()
