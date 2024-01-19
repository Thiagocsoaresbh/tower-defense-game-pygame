import pygame
from elements import Torre, Projetil
from posicao_torre import PosicaoTorre

def handle_events(posicoes_torres, torres, todos_sprites, projeteis, mensagem_criar_torre):
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