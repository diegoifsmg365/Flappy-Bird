import pygame
from scripts.cenas import Partida 
# from scripts.jogador import Jogador
# from scripts.cano import Cano

pygame.init()

tamanhoTela = [600,400]
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("FlappyBird")
relogio = pygame.time.Clock()
corFundo = (255, 191, 55)
# jog = Jogador(tela, 100, 100)
# cano = Cano(tela)

listaCenas = {
    'partida': Partida(tela),
}

cenaAtual = 'partida'

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    tela.fill(corFundo)

    # jog.atualizar()
    # jog.desenhar()
    # cano.atualizar()
    # cano.desenhar()

    cenaAtual = listaCenas[cenaAtual].atualizar()

    relogio.tick(60)
    pygame.display.flip()
