import Bioma

print("Olá! Você foi criado, informe seus dados: ")
nome = input("Informe Nome: ") 
idade = int(input("Informe Idade: ")) 

print("")

print(f"Perfeito! Bem vindo {nome}, qual bioma você desejaria spawnar? ")

print("")

print("""1 - Tundra (Enfrente frios congelantess🥶🥶🥶!!!)
2 - Deserto (Enfrente um calor insuportável🥵🥵🥵!!!)
3- Floresta Temperada (Vive em um ambiente amênuo🙃🙃🙃!!! )""")

op_bioma = int(input("Qual sua batalha? "))

estacao = input("Ótima escolha!! por fim, qual estação vc gostaria de enfrentar? (inverno, verão, outro) ")  #fazer range de biomas

if op_bioma == 1:
    bioma = Bioma.Tundra(estacao, "Tundra") 

elif op_bioma == 2:
    bioma = Bioma.Deserto(estacao, "Deserto")

elif op_bioma == 3:
    bioma = Bioma.Floresta_Temperada(estacao, "Floresta temperada")

else:
    print("Bioma não válido")



corpo = Bioma.Organismo(nome, idade, bioma)

print("""Qual ação você deseja fazer? 
# 1- Escalar """ )


print("")
acao = int(input("Escolha:"))

if acao == 1:
    altura = int(input("Qaul altura vc deseja escaalar? (em metros) "))
    escalar = Bioma.Organismo.Escalar(altura)
