import pygame
import random

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(random.randint(50, 750), random.randint(0, 50)))
        self.velocidade = 1
        self.vida = 2

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.x = pygame.math.Vector2(50, 750).rotate(random.randint(0, 90))
    
    def reset(self):
        self.vida = 2