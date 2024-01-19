import pygame
import random

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(random.randint(50, 750), 0))
        self.velocidade = random.uniform(0.5, 1.5)  # Ajuste o intervalo conforme necessário

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.x = pygame.math.Vector2(50, 750).rotate(random.randint(0, 90))
