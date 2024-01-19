# game_config.py

class GameConfig:
    # Configurações gerais do jogo

    # Tamanho da tela
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Tamanho do bloco
    BLOCK_WIDTH = SCREEN_WIDTH // 9
    BLOCK_HEIGHT = SCREEN_HEIGHT // 7

    # Tamanho do menu superior e inferior
    TOP_MENU_HEIGHT = SCREEN_HEIGHT // 10
    BOTTOM_MENU_HEIGHT = SCREEN_HEIGHT // 10

    # Espaço para inimigos
    ENEMY_AREA_WIDTH = SCREEN_WIDTH - BLOCK_WIDTH * 2
    ENEMY_AREA_HEIGHT = SCREEN_HEIGHT - TOP_MENU_HEIGHT - BOTTOM_MENU_HEIGHT - BLOCK_HEIGHT * 2

    # Número de inimigos por bloco
    ENEMIES_PER_BLOCK = 5

    # Número de inimigos em fila
    ENEMIES_IN_LINE = 5

    # Centro do bloco A8 (exemplo)
    A8_CENTER = (BLOCK_WIDTH * 7 + BLOCK_WIDTH // 2, BLOCK_HEIGHT * 1 + BLOCK_HEIGHT // 2)
