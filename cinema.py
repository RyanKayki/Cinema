import os

# TABELA
while True:
    os.system('cls')
    print("\n ----------Tabela de Preço----------")
    print("\n Olá caro cliente, por gentileza compre seus ingressos")
    print("\n ----------Valores----------")
    print("\n Até 17 Anos:             = R$ 15,00")
    print("\n De 18 Anos aos 59 Anos:  = R$ 30,00")
    print("\n Acima dos 60 Anos:       = R$ 20,00")

    try:
        quant = int(input("\n Insira o número de pessoas (max=2):"))

        if quant < 1 or quant > 2:
            print("\n Quantidade inválida")
        else:
            if quant == 1:
                anos = int(input("Por favor, informe a sua idade:"))
            else:
                anos = int(input("Por favor, informe a sua idade:"))
                anos1 = int(input("Agora, informe a idade do seu acompanhante:"))

            # PRIMEIRO INGRESSO
            if anos < 18:
                preco = 15
            elif anos < 60:
                preco = 30
            else:
                preco = 20

            # SEGUNDO INGRESSO
            if quant == 2:
                if anos1 < 18:
                    preco1 = 15
                elif anos1 < 60:
                    preco1 = 30
                else:
                    preco1 = 20

            # VALOR A PAGAR
            if quant == 1:
                print("\n Você está comprando:", quant, "bilhete e deve pagar: R$", preco)
            else:
                print("\n Você está comprando:", quant, "bilhete e deve pagar: R$", preco + preco1)

            input("Pressione Enter para continuar...")
            

    except ValueError:
        input("Erro: Insira um valor válido, Pressione Enter para continuar...")
        
