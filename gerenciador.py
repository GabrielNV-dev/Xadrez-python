class Gerenciador ():

    def __init__(self,tabuleiro,l,c,destinoL,destinoC):
        self.tabuleiro = tabuleiro
        self.l = l
        self.c = c
        self.destinoL = destinoL
        self.destinoC = destinoC

    def adiministracao(self):

        if self.tabuleiro[self.l][self.c] == " P " or self.tabuleiro[self.l][self.c] ==  " p ":
            print("peao")

        elif self.tabuleiro[self.l][self.c] == " T " or self.tabuleiro[self.l][self.c] ==  " t ":
            print("torre")

        elif self.tabuleiro[self.l][self.c] == " C " or self.tabuleiro[self.l][self.c] ==  " c ":
            print("cavalo")

        elif self.tabuleiro[self.l][self.c] == ">B " or self.tabuleiro[self.l][self.c] ==  ">b " or self.tabuleiro[self.l][self.c] == ">B " or self.tabuleiro[self.l][self.c] == " B<" or self.tabuleiro[self.l][self.c] ==  " b<":
            print("bispo")

        elif self.tabuleiro[self.l][self.c] == "D " or self.tabuleiro[self.l][self.c] ==  " d ":
            print("Dama")

        elif self.tabuleiro[self.l][self.c] == "R " or self.tabuleiro[self.l][self.c] == " r ":
            print("Rei")

