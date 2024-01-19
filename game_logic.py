# game_logic.py
import pygame
from elements import Torre, Inimigo, InterfaceUsuario
from elements import PosicaoTorre

# Defina as porcentagens para cada seção da tela
MENU_SUPERIOR_PORCENTAGEM = 10
MENU_INFERIOR_PORCENTAGEM = 10
AREA_COMBATE_PORCENTAGEM = 80

# Porcentagens para subdivisões dentro da área de combate
CORREDOR_PORCENTAGEM = 30
AREA_TORRES_PORCENTAGEM = 70

# Cores
COR_MENU = (100, 100, 100)
COR_AREA_COMBATE = (255, 255, 255)
COR_CORREDOR = (200, 200, 200)
COR_AREA_TORRES = (150, 150, 150)

def calcular_tamanho_tela():
    largura_tela = pygame.display.Info().current_w
    altura_tela = pygame.display.Info().current_h
    return largura_tela, altura_tela

def calcular_dimensoes(largura_tela, altura_tela):
    menu_superior_altura = altura_tela * MENU_SUPERIOR_PORCENTAGEM / 100
    menu_inferior_altura = altura_tela * MENU_INFERIOR_PORCENTAGEM / 100
    area_combate_altura = altura_tela * AREA_COMBATE_PORCENTAGEM / 100

    corredor_altura = area_combate_altura * CORREDOR_PORCENTAGEM / 100
    area_torres_altura = area_combate_altura * AREA_TORRES_PORCENTAGEM / 100

    return {
        "menu_superior": pygame.Rect(0, 0, largura_tela, menu_superior_altura),
        "menu_inferior": pygame.Rect(0, altura_tela - menu_inferior_altura, largura_tela, menu_inferior_altura),
        "area_combate": pygame.Rect(0, menu_superior_altura, largura_tela, area_combate_altura),
        "corredor": pygame.Rect(0, menu_superior_altura, largura_tela, corredor_altura),
        "area_torres": pygame.Rect(0, menu_superior_altura + corredor_altura, largura_tela, area_torres_altura),
    }

def run_game(tela):
    pygame.init()

    largura_tela, altura_tela = calcular_tamanho_tela()
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Tower Defense Game")

    dimensoes = calcular_dimensoes(largura_tela, altura_tela)

    # Criar os elementos do jogo usando as dimensões calculadas
    todos_sprites = pygame.sprite.Group()  # Criar a variável todos_sprites
    posicoes_torres = [
        PosicaoTorre(largura_tela * 0.2, dimensoes["area_torres"].top),
        PosicaoTorre(largura_tela * 0.8, dimensoes["area_torres"].top),
    ]

    torres = pygame.sprite.Group()
    for posicao in posicoes_torres:
        torre = Torre(posicao.rect.x, posicao.rect.y)
        todos_sprites.add(torre)
        torres.add(torre)

    interface = InterfaceUsuario()
    todos_sprites.add(interface)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        todos_sprites.update()

        tela.fill(COR_MENU, dimensoes["menu_superior"])
        tela.fill(COR_MENU, dimensoes["menu_inferior"])
        tela.fill(COR_AREA_COMBATE, dimensoes["area_combate"])
        tela.fill(COR_CORREDOR, dimensoes["corredor"])
        tela.fill(COR_AREA_TORRES, dimensoes["area_torres"])

        todos_sprites.draw(tela)

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    run_game()
