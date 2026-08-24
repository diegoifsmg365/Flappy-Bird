import pygame
from scripts.cano import Cano
from scripts.jogador import Jogador
from scripts.interfaces import Texto, Botao, GameOver

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 100)
        self.cano = Cano(tela)
        self.estado = "partida"
        self.contador = 0
        self.pontosValor = 0
        self.pontosTexto = Texto(tela, "0", 10, 10, (255, 255, 255), 30)
        
        # Para controle do Game Over
        self.mostrar_game_over = False
        self.tempo_game_over = 0
        self.game_over_texto = GameOver(tela)

    def atualizar(self):
        # Se estiver mostrando Game Over, não atualiza o jogo
        if self.mostrar_game_over:
            self.game_over_texto.desenhar()
            self.tempo_game_over += 1
            
            # Após 60 frames (1 segundo), volta ao menu
            if self.tempo_game_over > 60:
                self.mostrar_game_over = False
                self.tempo_game_over = 0
                self.estado = "menu"
                self.jogador.posicao = [100, 100]  # Reseta posição
                self.cano.x = self.tela.get_width()  # Reseta cano
                self.pontosValor = 0  # Reseta pontos
            return self.estado

        self.estado = "partida"
        
        # Atualiza jogador e cano
        self.jogador.atualizar()
        self.cano.atualizar()

        # Verifica colisão com as bordas (cima e baixo)
        altura_tela = self.tela.get_height()
        pos_y = self.jogador.get_posicao_y()
        
        # Se o pássaro tocou o topo (y < 0) ou o chão (y + altura > altura_tela)
        if pos_y < 0 or pos_y + self.jogador.tamanho[1] > altura_tela:
            self.mostrar_game_over = True
            self.tempo_game_over = 0
            return self.estado

        # Contador de pontos (a cada 60 frames = 1 segundo)
        self.contador += 1
        if self.contador > 60:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizar(str(self.pontosValor))

        # Desenha tudo
        self.jogador.desenhar()
        self.cano.desenhar()
        self.pontosTexto.desenhar()

        # Verifica colisão com os canos
        if self.cano.detectarColisao(self.jogador.getRect()):
            self.mostrar_game_over = True
            self.tempo_game_over = 0
            return self.estado

        return self.estado


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "Flappy Bird", 150, 50, (255, 255, 255), 60)
        self.subtitulo = Texto(tela, "Pressione ESPAÇO para jogar", 150, 120, (255, 255, 200), 30)
        self.estado = "menu"

    def atualizar(self):
        self.estado = "menu"
        
        # Desenha o menu
        self.titulo.desenhar()
        self.subtitulo.desenhar()

        # Verifica se a tecla ESPAÇO foi pressionada
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:  # K_SPACE é a tecla Espaço
            self.estado = "partida"

        return self.estado