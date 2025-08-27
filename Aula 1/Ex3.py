def Jokenpo(a, b):
    if(a == "TESOURA" and b == "PEDRA"):
        return "JOGADOR 2 ganhou!!!"
    elif(a == "TESOURA" and b == "PAPEL"):
        return "JOGADOR 1 ganhou!!!"
    elif(a == "PEDRA" and b == "TESOURA"):
        return "JOGADOR 1 ganhou!!!"
    elif(a == "PEDRA" and b == "PAPEL"):
        return "JOGADOR 2 ganhou!!!"
    elif(a == "PAPEL" and b == "TESOURA"):
        return "JOGADOR 2 ganhou!!!"
    else:
        return "JOGADOR 1 ganhou!!!"


a = input("Escolha o que vai jogar jogador 1: ").upper()
b = input("Escolha o que vai jogar jogador 2: ").upper()

while(a == b):
    print("EMPATE!!! Vamos denovo")
    a = input("Escolha o que vai jogar jogador 1: ").upper()
    b = input("Escolha o que vai jogar jogador 2: ").upper()
print(Jokenpo(a, b))

