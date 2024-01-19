import pygame
from elements import Torre, Inimigo, InterfaceUsuario
from posicao_torre import PosicaoTorre
from castelo import Castelo
from projetil import Projetil

pygame.init()

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Tower Defense Game")

todos_sprites = pygame.sprite.Group()  # Mova esta linha para cima
castelo = Castelo(350, 500)
todos_sprites.add(castelo)

torres = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
projeteis = pygame.sprite.Group()

torre = Torre(200, 300)
inimigo = Inimigo()

torres.add(torre)
inimigos.add(inimigo)
todos_sprites.add(torre, inimigo)

posicoes_torres = [
    PosicaoTorre(400, 300),
    PosicaoTorre(600, 300),
]

todos_sprites.add(*posicoes_torres)

interface = InterfaceUsuario()
todos_sprites.add(interface)

clock = pygame.time.Clock()

mensagem_criar_torre = "Clique para criar uma torre"

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
                    todos_sprites.add(torre)
                    torres.add(torre)
                    posicao.ocupada = True

                    projetil = Projetil(torre.rect.centerx, torre.rect.centery)
                    projeteis.add(projetil)
                else:
                    mensagem_criar_torre = "Posição inválida para criar torre"
                    
    colisoes_castelo = pygame.sprite.spritecollide(castelo, inimigos, False)
    for inimigo in colisoes_castelo:
        inimigo.velocidade = 0
        inimigo.rect.y -= 1

        castelo.sofrer_dano(1)

    todos_sprites.update()
    tela.fill((255, 255, 255))
    todos_sprites.draw(tela)

    interface.atualizar_nivel_torre(torre.nivel)
    if not torres:
        mensagem_criar_torre_surface = interface.fonte.render(mensagem_criar_torre, True, (255, 0, 0))
        tela.blit(mensagem_criar_torre_surface, (200, altura_tela - 40))

    colisoes_castelo = pygame.sprite.spritecollide(castelo, inimigos, True)
    if colisoes_castelo:
        castelo.sofrer_dano(1)

    projeteis.update()
    projeteis.draw(tela)
    
    pygame.display.flip()

    clock.tick(60)
