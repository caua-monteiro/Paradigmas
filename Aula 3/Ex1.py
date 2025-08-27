def main():
    n = int(input())
    jogadores = []
    for j in range(n):
        aux = {
            "nome": input(),
            "time": input(),
            "posicao": input(),
            "num_gols": int(input())
        }
        jogadores.append(aux)
    goleador = jogadores[0]
    for jogador in jogadores:
        if(jogador["num_gols"] > goleador["num_gols"]):
            goleador = jogador
    print(goleador)

main()