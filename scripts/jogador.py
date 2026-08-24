import pygame

class Jogador:
    def __init__(self, tela, x, y):
        self.posicao = [x, y]
        self.tamanho = [32, 32]
        self.rect = pygame.Rect(self.posicao, self.tamanho)

        self.contador = 0
        self.imagemAtual = 0
        self.tela = tela
        self.listaImagens = []

        # Carrega as 3 imagens do pássaro
        for i in range(3):
            imagem = pygame.image.load(f'assets/passaro-{i}.png')
            imagem = pygame.transform.scale(imagem, self.tamanho)
            self.listaImagens.append(imagem)

        self.velocidadeAtual = 0
        self.gravidade = 1/60 * 10  # Força da gravidade
        self.velocidadeMaxima = 1/60 * 100  # Velocidade máxima de queda

        # Variáveis para controle de bordas
        self.altura_tela = tela.get_height()

    def desenhar(self):
        # Animação: troca de imagem a cada 5 frames
        self.contador += 1
        if self.contador > 5:
            self.contador = 0
            self.imagemAtual = (self.imagemAtual + 1) % 3

        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao)

    def atualizar(self):
        # Aplica gravidade
        self.velocidadeAtual = min(self.velocidadeAtual + self.gravidade, self.velocidadeMaxima)

        # Atualiza posição
        self.posicao = [self.posicao[0], self.posicao[1] + self.velocidadeAtual]
        self.rect = pygame.Rect(self.posicao, self.tamanho)

        # Pula quando pressiona ESPAÇO
        self.teclas = pygame.key.get_pressed()
        if self.teclas[pygame.K_SPACE]:
            self.velocidadeAtual = -self.velocidadeMaxima * 2

    def getRect(self):
        return pygame.Rect(self.posicao, self.tamanho)

    def get_posicao_y(self):
        """Retorna a posição Y do pássaro (usado para verificar bordas)"""
        return self.posicao[1]