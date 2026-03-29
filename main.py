
tabuleiro = [["   " for j in range(8)]for i in range(8)]
pecas_brancas = [' T ',' C ','>B ',' D ',' R ',' B<',' C ',' T ',' P ']
pecas_pretas = [' t ',' c ','>b ',' d ',' r ',' b<',' c ',' t ',' p ']
jogador = 2

def montar_tabuleiro():
    for l in range(8):
        for c in range(8):
            if l == 0:
                tabuleiro[l][c] = pecas_brancas[c]
            elif l == 1:
                tabuleiro[l][c] = pecas_brancas[8]

            if l == 6:
                tabuleiro[l][c] = pecas_pretas[8]
            elif l == 7:
                tabuleiro[l][c] = pecas_pretas[c]

montar_tabuleiro()


def visualizacao():
    for l in range(8):
        for c in range(8):
            print(f"[{tabuleiro[l][c]}]", end="")
        print()

visualizacao()

while True:
    if jogador % 2 == 0:
        while True:
            l = int(input("Qual a linha da peça que deseja mexer:")) -1
            c = int(input("Qual a coluna da peça que deseja mexer:")) -1
            destinoL = int(input("Qual a linha que deseja enviar a peça:")) -1
            destinoC = int(input("Qual a coluna que deseja enviar a peça:")) -1

            if -1 < l < 8 and -1 < c < 8 and -1 < destinoL < 8 and -1 < destinoC < 8:
                break

        condicao = Gerenciador(tabuleiro,l,c,destinoL,destinoC)
        condicao.adiministracao()

        if (condicao) == 1:
            tabuleiro[destinoL][destinoC] = tabuleiro[l][c]
            tabuleiro[l][c] = "   "
            jogador = + 1

        else:
            print("Jogada invalida")
