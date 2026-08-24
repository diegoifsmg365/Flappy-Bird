import pygame
import random

class Cano:
    def __init__(self, tela):
        self.imagem = pygame.image.load('assets/cano.png')
        self.tela = tela
        self.altura_base = random.randint(100, 300)
        self.x = tela.get_width()
        self.distancia = 45  # Distância entre o cano de cima e de baixo
        self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
        self.cano_baixo = self.altura_base + self.distancia
        self.velocidade = 2

    def atualizar(self):
        # Move o cano para a esquerda
        self.x -= self.velocidade

        # Se o cano saiu totalmente da tela, reposiciona na direita com nova altura
        if self.x < -self.imagem.get_width():
            self.x = self.tela.get_width()
            self.altura_base = random.randint(100, 300)
            self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
            self.cano_baixo = self.altura_base + self.distancia

    def desenhar(self):
        # Inverte a imagem para o cano de cima
        imagem_invertida = pygame.transform.flip(self.imagem, False, True)
        self.tela.blit(imagem_invertida, (self.x, self.cano_cima))
        self.tela.blit(self.imagem, (self.x, self.cano_baixo))

    def detectarColisao(self, rect_jogador):
        """Verifica se o jogador colidiu com algum dos canos"""
        rect_cano_cima = pygame.Rect(self.x, self.cano_cima, self.imagem.get_width(), self.imagem.get_height())
        rect_cano_baixo = pygame.Rect(self.x, self.cano_baixo, self.imagem.get_width(), self.imagem.get_height())
        
        if rect_jogador.colliderect(rect_cano_cima) or rect_jogador.colliderect(rect_cano_baixo):
            return True
        return False