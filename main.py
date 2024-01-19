import pygame
from elements import Torre, Inimigo, InterfaceUsuario
from posicao_torre import PosicaoTorre
from castelo import Castelo

pygame.init()

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Tower Defense Game")

castelo = Castelo(350, 500)

todos_sprites = pygame.sprite.Group()
torres = pygame.sprite.Group()
inimigos = pygame.sprite.Group()

torre = Torre(200, 300)
inimigo = Inimigo()

torres.add(torre)
inimigos.add(inimigo)
todos_sprites.add(torre, inimigo)

posicoes_torres = [
    PosicaoTorre(400, 300),
    PosicaoTorre(600, 300),
]

todos_sprites.add(posicoes_torres)

interface = InterfaceUsuario()
todos_sprites.add(interface)

clock = pygame.time.Clock()

# Adicione ao início do loop principal em main.py
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
                else:
                    mensagem_criar_torre = "Posição inválida para criar torre"

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

    pygame.display.flip()

    clock.tick(60)
