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
        self.cooldown = 30  # Tempo de espera entre disparos
        self.tempo_ultimo_disparo = pygame.time.get_ticks()
            
    def update(self):
        pass
    
    def evoluir(self):
        self.nivel += 1
        self.atualizar_aparencia()
    
    def atualizar_aparencia(self):
        cores = [(255, 0, 0), (255, 165, 0), (255, 255, 0)]
        self.image.fill(cores[self.nivel - 1])

    def disparar(self):
        agora = pygame.time.get_ticks()
        if agora - self.tempo_ultimo_disparo > self.cooldown:
            self.tempo_ultimo_disparo = agora
            projetil = Projetil(self.rect.centerx, self.rect.centery)
            projeteis.add(projetil)

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
            self.rect.y = 0
            self.rect.x = pygame.math.Vector2(50, 750).rotate(random.randint(0, 90))

    def reset(self):
        self.vida = 2

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

class InterfaceUsuario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fonte = pygame.font.Font(None, 36)
        self.image = self.fonte.render("Nivel da Torre: 1", True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=(10, 10))
        
    def atualizar_nivel_torre(self, nivel):
        self.image = self.fonte.render(f"Nivel da Torre: {nivel}", True, (255, 255, 255))

class Projetil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))  # Cor vermelha para representar o projetil
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidade = 5  # Ajuste a velocidade do projetil conforme necessário

    def update(self):
        self.rect.y -= self.velocidade
