import pygame
import random

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(random.randint(50, 750), 0))
        self.velocidade = 1
        self.vida = 2

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y > 600:
            self.reset()

    def reset(self):
        self.rect.y = 0
        self.rect.x = random.randint(50, 750)

class InterfaceUsuario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fonte = pygame.font.Font(None, 36)
        self.image = self.fonte.render("Nivel da Torre: 1", True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=(10, 10))
        self.vidas = 3  # Adicionamos um contador de vidas
        self.inimigos_atingiram_g8 = 0  # Contador de inimigos que atingiram G8

    def atualizar_nivel_torre(self, nivel):
        self.image = self.fonte.render(f"Nivel da Torre: {nivel}", True, (255, 255, 255))

    def perder_vida(self):
        self.vidas -= 1
        if self.vidas <= 0:
            pygame.quit()
            exit()

    def inimigo_atingiu_g8(self):
        self.inimigos_atingiram_g8 += 1
        if self.inimigos_atingiram_g8 >= 3:
            self.vidas = 0  # Perder todas as vidas ao atingir 3 inimigos em G8
            self.perder_vida()  # Ativar a lógica de perder vida
