import pygame

# RGB Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
# objetos e seus respectivos tamanhos
screen_width = 800
screen_height = 600
block_width = 70
block_height = 70
arrow_width = 30
arrow_height = 5
obstaculo_width = 50
obstaculo_height = 58
# dimensoes do jogo
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
# imagens
background = pygame.image.load("Background.bmp")
pygame.display.set_caption("Friamente Calculado")
obstaculo1 = pygame.image.load("pato1.bmp")
obstaculo2 = pygame.image.load("pato2.bmp")
obstaculo3 = pygame.image.load("pato3.bmp")
bow = pygame.image.load("Arco.bmp")
block = pygame.image.load("block.bmp")

# definindo FPS
clock = pygame.time.Clock()
# inicio no pygame
pygame.init()
# fonte de texto
font = pygame.font.SysFont(None, 25)

# definindo texto que mostra na tela
def messagetoscreen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_width / 2 - 250, screen_height / 2])


def gameLoop():
    # definindo posicoes:
    # alvo
    block_x = screen_width / 1.2307
    block_y = screen_height / 2.5
    block_speed = screen_height / 100
    # primeiro pato
    obstaculo1x = screen_width / 4
    obstaculo1y = screen_height / 2
    obstaculo1_speed = screen_height / 240
    # segundo pato
    obstaculo2x = screen_width / 2.2857
    obstaculo2y = screen_height / 1.20
    obstaculo2_speed = screen_height / 240
    # terceiro pato
    obstaculo3x = screen_width / 1.6
    obstaculo3y = screen_height / 4
    obstaculo3_speed = screen_height / 240
    # projetil
    arrow_x = screen_width / 20
    arrow_y = screen_height / 1.9672
    arrow_speedx = 0
    arrow_speedy = 0
    # tentativas utilizadas
    chances = 0
    #s = fase(qual dificuldade)
    s = 1
    # acelerecao no eixo Y implementada para as dificuldades > 1
    PARAMETER = 0
    # parametersong: define limite quando ha o som, e apenas uma vez tocado
    PARAMETERSONG = 0

    # estados do jogo
    gameWin = False
    gameExit = False
    gameThree = False

    while not gameExit:
        # definindo a vitoria em dada dificuldade
        while gameWin == True:
            screen.fill(black)
            messagetoscreen("Vencedor! Pressione C para continuar a jogar ou S para sair", blue)
            pygame.display.update()
            if PARAMETERSONG == 1:
                if s == 1:
                    pygame.mixer.music.load("Nivel1.mp3")
                    pygame.mixer.music.play()
                if s == 2:
                    pygame.mixer.music.load("Nivel2.mp3")
                    pygame.mixer.music.play()
                if s == 3:
                    pygame.mixer.music.load("Nivel3.mp3")
                    pygame.mixer.music.play()
                if s == 4:
                    pygame.mixer.music.load("Nivel4.mp3")
                    pygame.mixer.music.play()
                if s == 5:
                    pygame.mixer.music.load("Nivel5.mp3")
                    pygame.mixer.music.play()
            # sair do Loop de audio
            PARAMETERSONG = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameWin = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        gameExit = True
                        gameWin = False

                    if event.key == pygame.K_c:
                        gameLoop()
        # definindo as tres tentativas sem acerto utilizadas
        while gameThree == True:
            screen.fill(black)
            messagetoscreen("Acabaram suas chances! Pressione C para continuar ou S para sair", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameThree = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        gameExit = True
                        gameThree = False

                    if event.key == pygame.K_c:
                        gameLoop()

        # fonte de texto importada para descrever dificuldade / tentativas
        fontScoot = pygame.font.Font("scootchover-sans.ttf", 24)
        # apresentando imagens presentes (exemplo: background, patos)
        screen.blit(background, (0, 0))
        screen.blit(block, (block_x, block_y))
        screen.blit(bow, (screen_width / 80, int(screen_height / 2.4)))
        screen.blit(obstaculo1, (obstaculo1x, obstaculo1y))
        screen.blit(obstaculo2, (obstaculo2x, obstaculo2y))
        screen.blit(obstaculo3, (obstaculo3x, obstaculo3y))
        # definindo comandos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    arrow_speedx = screen_width / 55
                    arrow_speedy = PARAMETER
            # nivel 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    block_speed = screen_height / 100
                    s = 1
                    chances = 0
                    obstaculo1_speed = screen_height / 240
                    obstaculo2_speed = screen_height / 240
                    obstaculo3_speed = screen_height / 240
                    PARAMETER = 0
            # nivel 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2:
                    block_speed = screen_height / 40
                    s = 2
                    chances = 0
                    obstaculo1_speed = screen_height / 120
                    obstaculo2_speed = screen_height / 90
                    obstaculo3_speed = screen_height / 60
                    PARAMETER = 1
            # nivel 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    block_speed = screen_height / 40
                    s = 3
                    chances = 0
                    obstaculo1_speed = screen_height / 90
                    obstaculo2_speed = screen_height / 40
                    obstaculo3_speed = screen_height / 60
                    PARAMETER = 2
            # nivel 4
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    block_speed = screen_height / 40
                    s = 4
                    chances = 0
                    obstaculo1_speed = screen_height / 60
                    obstaculo2_speed = screen_height / 45
                    obstaculo3_speed = screen_height / 45
                    PARAMETER = 3
            # nivel 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    block_speed = int(screen_height / 35)
                    s = 5
                    chances = 0
                    obstaculo1_speed = screen_height / 40
                    obstaculo2_speed = screen_height / 45
                    obstaculo3_speed = screen_height / 45
                    PARAMETER = 5

        # definindo os limites do projetil
        if arrow_x - arrow_width >= screen_width - (screen_width / 8) or arrow_y - arrow_height >= screen_height:
            pygame.mixer.music.load("Errou.mp3")
            pygame.mixer.music.play()
            chances += 1
            arrow_x = screen_width / 20
            arrow_y = int(screen_height / 1.967)
            arrow_speedx = 0
            arrow_speedy = 0

        if chances >= 3:
            gameThree = True

        # definindo movimentacoes dos obstaculos/alvo
        # definindo o retorno quando chega ao limite
        if block_y <= screen_height / 6:
            block_speed *= -1
            block_y = screen_height / 6
        if block_y >= screen_height - block_height:
            block_speed *= -1
            block_y = screen_height - block_height
        if obstaculo1y <= screen_height / 6:
            obstaculo1_speed *= -1
            obstaculo1y = screen_height / 6
        if obstaculo1y >= screen_height - (screen_height / 10):
            obstaculo1_speed *= -1
            obstaculo1y = screen_height - (screen_height / 10)
        if obstaculo2y <= screen_height / 6:
            obstaculo2_speed *= -1
            obstaculo2y = screen_height / 6
        if obstaculo2y >= screen_height - (screen_height / 10):
            obstaculo2_speed *= -1
            obstaculo2y = screen_height - (screen_height / 10)
        if obstaculo3y <= screen_height / 6:
            obstaculo3_speed *= -1
            obstaculo3y = screen_height / 6
        if obstaculo3y >= screen_height - (screen_height / 10):
            obstaculo3_speed *= -1
            obstaculo3y = screen_height - (screen_height / 10)

        # Movimentos aplicados
        obstaculo1y -= obstaculo1_speed
        obstaculo2y += obstaculo2_speed
        obstaculo3y -= obstaculo3_speed
        block_y += block_speed
        arrow_x += arrow_speedx
        arrow_y += arrow_speedy

        # posicao relativa do centro da flecha(x,y)
        CENTERARROWX = (arrow_width / 2) + arrow_x
        CENTERARROWY = (arrow_height / 2) + arrow_y
        # geometria para acertar o alvo
        CENTERBLOCKX = (block_width / 2) + block_x
        CENTERBLOCKY = (block_height / 2) + block_y
        DIAGONAL = ((block_width ** 2) + (block_height ** 2)) ** 0.5
        DISTANCE = ((((CENTERBLOCKX - CENTERARROWX) ** 2)) + ((CENTERBLOCKY - CENTERARROWY) ** 2)) ** 0.5
        # geometria para acertar os patos
        # pato 1
        CENTERBLOCKX2 = (obstaculo_width / 2) + obstaculo1x
        CENTERBLOCKY2 = (obstaculo_height / 2) + obstaculo1y
        DIAGONAL2 = ((obstaculo_width ** 2) + (obstaculo_height ** 2)) ** 0.5
        DISTANCE2 = ((((CENTERBLOCKX2 - CENTERARROWX) ** 2)) + ((CENTERBLOCKY2 - CENTERARROWY) ** 2)) ** 0.5
        # pato 2
        CENTERBLOCKX3 = (obstaculo_width / 2) + obstaculo2x
        CENTERBLOCKY3 = (obstaculo_height / 2) + obstaculo2y
        DIAGONAL3 = ((obstaculo_width ** 2) + (obstaculo_height ** 2)) ** 0.5
        DISTANCE3 = ((((CENTERBLOCKX3 - CENTERARROWX) ** 2)) + ((CENTERBLOCKY3 - CENTERARROWY) ** 2)) ** 0.5
        # pato 3
        CENTERBLOCKX4 = (obstaculo_width / 2) + obstaculo3x
        CENTERBLOCKY4 = (obstaculo_height / 2) + obstaculo3y
        DIAGONAL4 = ((obstaculo_width ** 2) + (obstaculo_height ** 2)) ** 0.5
        DISTANCE4 = ((((CENTERBLOCKX4 - CENTERARROWX) ** 2)) + ((CENTERBLOCKY4 - CENTERARROWY) ** 2)) ** 0.5

        # acertando o alvo
        if DISTANCE <= int(DIAGONAL / 2) and arrow_x + arrow_width > block_x and (
                abs(CENTERBLOCKY - CENTERARROWY) <= arrow_height and abs(CENTERBLOCKX - CENTERARROWX)) <= arrow_width:
            gameWin = True
            PARAMETERSONG = 1
        # acertando o primeiro pato (da esquerda para a direita)
        if DISTANCE2 <= int(DIAGONAL2 / 2) and arrow_x + arrow_width > obstaculo1x and(
                abs(CENTERBLOCKY2 - CENTERARROWY) <= arrow_height and abs(CENTERBLOCKX2 - CENTERARROWX)) <= arrow_width:
            pygame.mixer.music.load("Errou.mp3")
            pygame.mixer.music.play()
            chances += 1
            arrow_x = screen_width / 20
            arrow_y = int(screen_height / 1.967)
            arrow_speedx = 0
            arrow_speedy = 0

        # acertando o segundo pato (da esquerda para a direita)
        if DISTANCE3 <= int(DIAGONAL3 / 2) and arrow_x + arrow_width > obstaculo2x and(
                abs(CENTERBLOCKY3 - CENTERARROWY) <= arrow_height and abs(CENTERBLOCKX3 - CENTERARROWX)) <= arrow_width:
            pygame.mixer.music.load("Errou.mp3")
            pygame.mixer.music.play()
            chances += 1
            arrow_x = screen_width / 20
            arrow_y = int(screen_height / 1.967)
            arrow_speedx = 0
            arrow_speedy = 0

        # acertando o terceiro pato (da esquerda para a direita)
        if DISTANCE4 <= int(DIAGONAL4 / 2) and arrow_x + arrow_width > obstaculo3x and(
                abs(CENTERBLOCKY4 - CENTERARROWY) <= arrow_height and abs(CENTERBLOCKX4 - CENTERARROWX)) <= arrow_width:
            pygame.mixer.music.load("Errou.mp3")
            pygame.mixer.music.play()
            chances += 1
            arrow_x = screen_width / 20
            arrow_y = int(screen_height / 1.967)
            arrow_speedx = 0
            arrow_speedy = 0

        # metodo utilizado para fonte com variaveis (tentativas, dificuldade, gravidade)
        s1 = 66
        s2 = 66
        s3 = 66
        score = fontScoot.render("Dificuldade: " + str(s), 1, (s1, s2, s3))
        tries = fontScoot.render("Tentativas: " + str(chances), 1, (s1, s2, s3))
        gravity = fontScoot.render("Gravidade: " + str(PARAMETER), 1, (s1, s2, s3))
        # projetil se baseia em um retangulo
        pygame.draw.rect(screen, orange, [arrow_x, arrow_y, arrow_width, arrow_height])
        # desenhando as tentativas e dificuldade na tela
        screen.blit(score, (screen_width / 40, screen_height / 6))
        screen.blit(tries, (screen_width / 40, int(screen_height / 4.8)))
        screen.blit(gravity, (screen_width / 40, int(screen_height / 4)))
        pygame.display.update()
        # definindo FPS/Clock
        clock.tick(60)

    pygame.quit()
    quit()


gameLoop()