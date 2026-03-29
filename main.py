tabuleiro = [["   " for j in range(8)]for i in range(8)]
pecas_brancas = [' T ',' C ','>B ',' D ',' R ',' B<',' C ',' T ',' P ']
pecas_pretas = [' t ',' c ','>b ',' d ',' r ',' b<',' c ',' t ',' p ']

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
