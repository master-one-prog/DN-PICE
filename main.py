from bioma import bioma
from bioma import Tundra
from bioma import Floresta_Temperada
from bioma import Deserto
from bioma import Organismo
from bioma import Coracao
from bioma import Cerebro



print("Olá! Você foi criado, informe seus dados: ")
nome = input("Informe Nome: ") 
idade = int(input("Informe Idade: ")) 

while True:

    print("")

    print(f"Perfeito! Bem vindo {nome}, qual bioma você desejaria spawnar? ")

    print("")

    print("""1 - Tundra (Enfrente frios congelantess🥶🥶🥶!!!)
    2 - Deserto (Enfrente um calor insuportável🥵🥵🥵!!!)
    3- Floresta Temperada (Vive em um ambiente amênuo🙃🙃🙃!!! )""")

    op_bioma = int(input("Qual sua batalha? "))

    estacao = input("Ótima escolha!! por fim, qual estação vc gostaria de enfrentar? (inverno, verão, outro) ")  #fazer range de biomas



    if op_bioma == 1:
        bioma = Tundra(estacao, "Tundra") 

    elif op_bioma == 2:
        bioma = Deserto(estacao, "Deserto")

    elif op_bioma == 3:
        bioma = Floresta_Temperada(estacao, "Floresta temperada")

    else:
        print("Bioma não válido")



    corpo = Organismo(nome, idade, bioma)

    print("""Qual ação você deseja fazer? 
    # 1- Escalar 
    # 2- Correr
    # 3- Nadar
    # 4- Pular""" )


    print("")
    acao = int(input("Escolha:"))

    if acao == 1:
        altura = int(input("Qual altura você deseja escalar? (em metros) "))
        corpo.Escalar(altura)

    elif acao == 2:
        distancia = int(input("Qual a distancia que você deseja correr? (em metros)"))
        corpo.Correr(distancia)

    elif acao == 3:
        Distancia = int(input("Qual a distancia que você deseja nadar? (em metros)"))
        corpo.Nadar(Distancia)

    elif acao == 4:
        forca_impulso = int(input("Qual a força de impulso você deseja? (em Newtons)"))
        corpo.Pular(forca_impulso)

    opcao = input("Deseja continuar jogando? (s/n)")
    if opcao == "s" or opcao == "S":
        print("Boa jogo!")
    elif opcao == "n" or opcao == "N":
        print("Adeus")
        break

