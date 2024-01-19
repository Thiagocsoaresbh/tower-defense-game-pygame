import pygame
import random

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
    
class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(random.randint(50, 750), 0))
        self.velocidade = 1
        
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.x = random.randint(50, 750)
            
class InterfaceUsuario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fonte = pygame.font.Font(None, 36)
        self.image = self.fonte.render("Nivel da Torre: 1", True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=(10, 10))
        
    def atualizar_nivel_torre(self, nivel):
        self.image = self.fonte.render(f"Nivel da Torre: {nivel}", True, (255, 255, 255))
