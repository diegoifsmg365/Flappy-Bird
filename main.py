import pygame
from scripts.jogador import Jogador

pygame.init()

tamanhoTela = [600,400]
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("FlappyBird")
relogio = pygame.time.Clock()
corFundo = (255, 191, 55)
jog = Jogador(tela, 100, 100)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    tela.fill(corFundo)

    jog.atualizar()
    jog.desenhar()

    relogio.tick(60)
    pygame.display.flip()
    