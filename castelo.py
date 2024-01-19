import pygame

class Castelo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((128, 128, 128))  # Cor cinza para representar o castelo
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hp = 100  # Pontos de vida do castelo

    def sofrer_dano(self, dano):
        self.hp -= dano
        if self.hp <= 0:
            # Implemente aqui a lógica de derrota ou fim de jogo
            pass
