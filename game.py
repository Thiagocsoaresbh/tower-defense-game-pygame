import pygame
from elements import Torre, Inimigo, InterfaceUsuario
from posicao_torre import PosicaoTorre
from castelo import Castelo
from projetil import Projetil

class Game:
    def __init__(self):
        pygame.init()
        self.largura_tela = 480  # Ajustado para uma largura adequada para celular
        self.altura_tela = 800   # Ajustado para uma altura adequada para celular
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Tower Defense Game")

        # Ajustado para um castelo menor para se adequar ao novo layout
        self.castelo = Castelo(self.largura_tela // 2, self.altura_tela - 50)
        self.todos_sprites = pygame.sprite.Group()
        self.torres = pygame.sprite.Group()
        self.inimigos = pygame.sprite.Group()
        self.projeteis = pygame.sprite.Group()

        self.torre = Torre(200, 300)
        self.inimigo = Inimigo()

        self.torres.add(self.torre)
        self.inimigos.add(self.inimigo)
        self.todos_sprites.add(self.torre, self.inimigo)

        # Ajuste das posições das torres conforme o novo layout
        posicoes_torres = [
            PosicaoTorre(self.largura_tela // 3, self.altura_tela // 2),
            PosicaoTorre(2 * self.largura_tela // 3, self.altura_tela // 2),
        ]

        self.todos_sprites.add(*posicoes_torres)

        # Ajustado para uma interface mais compacta
        self.interface = InterfaceUsuario()
        self.todos_sprites.add(self.interface)

        self.clock = pygame.time.Clock()

        # Adicione ao início do loop principal em game.py
        self.mensagem_criar_torre = "Clique para criar uma torre"

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    posicao_mouse = pygame.mouse.get_pos()
                    for posicao in posicoes_torres:
                        if posicao.rect.collidepoint(posicao_mouse) and not posicao.ocupada:
                            torre = Torre(posicao.rect.x, posicao.rect.y)
                            self.todos_sprites.add(torre)
                            self.torres.add(torre)
                            posicao.ocupada = True

                            projetil = Projetil(torre.rect.centerx, torre.rect.centery)
                            self.projeteis.add(projetil)
                        else:
                            self.mensagem_criar_torre = "Posição inválida para criar torre"

            self.todos_sprites.update()
            self.tela.fill((255, 255, 255))
            self.todos_sprites.draw(self.tela)


            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
