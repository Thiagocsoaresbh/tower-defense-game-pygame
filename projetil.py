import pygame

class Projetil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))  # Cor vermelha para representar o projetil
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidade = 5  # Ajuste a velocidade do projetil conforme necessário

    def update(self):
        self.rect.y -= self.velocidade
