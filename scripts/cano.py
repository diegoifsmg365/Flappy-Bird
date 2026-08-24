import pygame
import random

class Cano:
    def __init__(self, tela):
        self.imagem = pygame.image.load('assets/cano.png')
        self.tela = tela
        self.altura_base = random.randint(100, 300)
        self.x = tela.get_width()
        self.distancia = 45
        self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
        self.cano_baixo = self.altura_base + self.distancia
        self.velocidade = 2

    def atualizar(self):
        self.x -= self.velocidade
        if self.x < -self.imagem.get_width():
            self.x = self.tela.get_width()
            self.altura_base = random.randint(100, 300)
            self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
            self.cano_baixo = self.altura_base + self.distancia

    def desenhar(self):
        imagem_invertida = pygame.transform.flip(self.imagem, False, True)
        self.tela.blit(imagem_invertida, (self.x, self.cano_cima))
        self.tela.blit(self.imagem, (self.x, self.cano_baixo))
