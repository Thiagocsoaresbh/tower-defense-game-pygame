import pygame
from elements import Torre, Inimigo

pygame.init()

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Tower Defense Game")

todos_sprites = pygame.sprite.Group()
torres = pygame.sprite.Group()
inimigos = pygame.sprite.Group()

torre = Torre(100, 100)
inimigo = Inimigo()

torres.add(torre)
inimigos = Inimigo()
todos_sprites.add(torre, inimigo)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((255, 255, 255))
    todos_sprites.draw(tela)
    
    pygame.display.flip()
    
    clock.tick(60)
