import pygame

class PosicaoTorre(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.ocupada = False

    def reset(self):
        self.ocupada = False
        self.image.fill((0, 255, 0))  # Reset para a cor verde
