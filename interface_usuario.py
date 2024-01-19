import pygame

class InterfaceUsuario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fonte = pygame.font.Font(None, 36)
        self.image = self.fonte.render("Nivel da Torre: 1", True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=(10, 10))

    def atualizar_nivel_torre(self, nivel):
        self.image = self.fonte.render(f"Nivel da Torre: {nivel}", True, (255, 255, 255))
