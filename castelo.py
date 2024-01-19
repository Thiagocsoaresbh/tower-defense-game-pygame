import pygame

class Castelo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((350, 350))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hp = 1000

    def sofrer_dano(self, dano):
        self.hp -= dano
        self.hp = max(0, self.hp)
        if self.hp == 0:
            pass
