import pygame
import random

class Torre(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
            
    def update(self):
        pass
    
class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(random.randint(50, 750), 0))
        self.velocidade = random.randint(1, 3)
        
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.x = random.randint(50, 750)
            
            

