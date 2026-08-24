import pygame
from scripts.cano import Cano
from scripts.jogador import Jogador

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 100)
        self.cano = Cano(tela)
        self.estado = "partida"

    def atualizar(self):
        self.estado = "partida"
        self.jogador.atualizar()
        self.cano.atualizar()

        self.jogador.desenhar()
        self.cano.desenhar()

        return self.estado