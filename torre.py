import pygame

class Torre(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.nivel = 1
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.atualizar_aparencia()
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass

    def evoluir(self):
        self.nivel += 1
        self.atualizar_aparencia()

    def atualizar_aparencia(self):
        cores = [(255, 0, 0), (255, 165, 0), (255, 255, 0)]
        self.image.fill(cores[self.nivel - 1])
