import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor, tamanho):
        self.tela = tela
        self.texto = texto
        self.posicao = (x, y)
        self.cor = cor
        self.tamanho = tamanho

        pygame.font.init()
        self.fonte = pygame.font.Font(None, self.tamanho)
        self.imagemTexto = self.fonte.render(self.texto, False, self.cor)

    def desenhar(self):
        self.tela.blit(self.imagemTexto, self.posicao)

    def atualizar(self, novoTexto):
        """Atualiza o texto (usado para a pontuação)"""
        self.imagemTexto = self.fonte.render(novoTexto, False, self.cor)


class Botao:
    def __init__(self, tela, texto, x, y, tamanho, corFundo, corTexto):
        self.tela = tela
        self.texto = Texto(tela, texto, x, y, corTexto, tamanho)
        self.posicao = (x, y)
        self.corFundo = corFundo

    def desenhar(self):
        # Cria um retângulo ao redor do texto
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())
        # Desenha o fundo do botão
        pygame.draw.rect(self.tela, self.corFundo, rect)
        # Desenha o texto por cima
        self.texto.desenhar()

    def get_click(self):
        """Verifica se o botão foi clicado"""
        posicaoMouse = pygame.mouse.get_pos()
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())
        if rect.collidepoint(posicaoMouse) and pygame.mouse.get_pressed()[0]:
            return True
        return False


class GameOver:
    """Classe para exibir a mensagem de Game Over"""
    def __init__(self, tela):
        self.tela = tela
        self.texto_game_over = Texto(tela, "GAME OVER!", 150, 150, (255, 0, 0), 60)
        self.texto_reiniciar = Texto(tela, "", 100, 220, (255, 255, 255), 30)

    def desenhar(self):
        self.texto_game_over.desenhar()
        self.texto_reiniciar.desenhar()