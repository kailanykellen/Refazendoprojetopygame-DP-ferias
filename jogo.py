# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha') #trocamos o titulo

# ----- Inicia assets
METEOR_WIDTH = 50 #largura meteoro
METEOR_HEIGHT = 38 #altura meteoro
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/starfield.png').convert() #imagem da tela que em breve será substituida
meteor_img = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha() #transparencia na imagem de meteoro
meteor_img_small = pygame.transform.scale(meteor_img, (METEOR_WIDTH, METEOR_HEIGHT)) #diminuindo o tamanho do meteoro

# ----- Inicia estruturas de dados
game = True
meteor_x = random.randint(0, WIDTH-METEOR_WIDTH)
# y negativo significa que está acima do topo da janela. O meteoro começa fora da janela
meteor_y = random.randint(-100, -METEOR_HEIGHT ) #começar a cima da tela
meteor_speedx = random.randint(-3,3) #velocidade x
meteor_speedy = random.randint(2,9) #velocidade y

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    meteor_x += meteor_speedx
    meteor_y += meteor_speedy
    # Se o meteoro passar do final da tela, volta para cima
    if meteor_y > HEIGHT or meteor_x + METEOR_WIDTH < 0 or meteor_x > WIDTH:
        meteor_x = random.randint(0, WIDTH-METEOR_WIDTH)
        meteor_y = random.randint(-100, -METEOR_HEIGHT )
        meteor_speedx = random.randint(-3,3) #velocidade x
        meteor_speedy = random.randint(2,9) #velocidade y

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(meteor_img_small, (meteor_x, meteor_y))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

