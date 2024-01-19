import pygame
from elements import Torre, Inimigo, InterfaceUsuario, PosicaoTorre, Projetil

pygame.init()

# Definindo as cores
COR_MENU = (100, 100, 100)
COR_AREA_COMBATE = (0, 255, 255)
COR_CORREDOR = (255, 200, 200)
COR_AREA_TORRES = (250, 150, 150)

# Função para calcular dimensões da tela
# Função para calcular dimensões da tela
def calcular_dimensoes(largura_tela, altura_tela):
    menu_superior_altura = altura_tela * 0.1
    menu_inferior_altura = altura_tela * 0.1
    area_combate_altura = altura_tela * 0.8

    corredor_altura = area_combate_altura * 0.2
    area_torres_altura = area_combate_altura * 0.8

    corredor_esquerdo = pygame.Rect(0, menu_superior_altura, largura_tela * 0.2, corredor_altura)
    corredor_central = pygame.Rect(largura_tela * 0.2, menu_superior_altura, largura_tela * 0.6, corredor_altura)
    corredor_direito = pygame.Rect(largura_tela * 0.8, menu_superior_altura, largura_tela * 0.2, corredor_altura)

    area_torres = pygame.Rect(largura_tela * 0.2, menu_superior_altura + corredor_altura, largura_tela * 0.6, area_torres_altura)

    return {
        "menu_superior": pygame.Rect(0, 0, largura_tela, menu_superior_altura),
        "menu_inferior": pygame.Rect(0, altura_tela - menu_inferior_altura, largura_tela, menu_inferior_altura),
        "area_combate": pygame.Rect(0, menu_superior_altura, largura_tela, area_combate_altura),
        "corredor_esquerdo": corredor_esquerdo,
        "corredor_central": corredor_central,
        "corredor_direito": corredor_direito,
        "area_torres": area_torres,
        "corredor": corredor_central,  # Adicionando chave para o corredor
    }


# Função para rodar o jogo
def run_game():
    largura_tela, altura_tela = 480, 800  # Defina o tamanho desejado para um celular
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Tower Defense Game")

    dimensoes = calcular_dimensoes(largura_tela, altura_tela)

    todos_sprites = pygame.sprite.Group()
    torres = pygame.sprite.Group()
    projeteis = pygame.sprite.Group()

    posicoes_torres = [
        PosicaoTorre(largura_tela * 0.2, dimensoes["area_torres"].top),
        PosicaoTorre(largura_tela * 0.8, dimensoes["area_torres"].top),
    ]

    interface = InterfaceUsuario()
    todos_sprites.add(interface)

    clock = pygame.time.Clock()

    mensagem_criar_torre = "Clique para criar uma torre"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                for posicao in posicoes_torres:
                    if posicao.rect.collidepoint(posicao_mouse) and not posicao.ocupada:
                        torre = Torre(posicao.rect.x, posicao.rect.y)
                        todos_sprites.add(torre)
                        torres.add(torre)
                        posicao.ocupada = True

                        projetil = Projetil(torre.rect.centerx, torre.rect.centery)
                        projeteis.add(projetil)
                    else:
                        mensagem_criar_torre = "Posição inválida para criar torre"

        # Lógica do jogo continua aqui...

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
